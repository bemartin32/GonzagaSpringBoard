from flask import Flask, request, redirect, render_template

# from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///blogly"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "ihaveasecret"

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# toolbar = DebugToolbarExtension(app)

with app.app_context():
    connect_db(app)
    db.create_all()


@app.route("/")
def root():
    """Homepage redirects to list of users."""

    return redirect("/users")


##############################################################################
# User route


@app.route("/users")
def users_index():
    """Show a page with info on all users"""

    users = User.query.order_by(User.last_name, User.first_name).all()
    return render_template("/users.html", users=users)


@app.route("/users/new", methods=["GET"])
def users_new_form():
    """Show a form to create a new user"""

    return render_template("/create_user.html")


@app.route("/users/new", methods=["POST"])
def users_new():
    """Handle form submission for creating a new user"""

    new_user = User(
        first_name=request.form["first_name"],
        last_name=request.form["last_name"],
        image_url=request.form["image_url"] or None,
    )

    db.session.add(new_user)
    db.session.commit()

    return redirect("/users")


@app.route("/users/<int:user_id>")
def users_show(user_id):
    """Show a page with info on a specific user"""

    user = User.query.get_or_404(user_id)
    return render_template("/show_users.html", user=user)


@app.route("/users/<int:user_id>/edit")
def users_edit(user_id):
    """Show a form to edit an existing user"""

    user = User.query.get_or_404(user_id)
    return render_template("/edit_user.html", user=user)


@app.route("/users/<int:user_id>/edit", methods=["POST"])
def users_update(user_id):
    """Handle form submission for updating an existing user"""

    user = User.query.get_or_404(user_id)
    user.first_name = request.form["first_name"]
    user.last_name = request.form["last_name"]
    user.image_url = request.form["image_url"]

    db.session.add(user)
    db.session.commit()

    return redirect("/users")


@app.route("/users/<int:user_id>/delete", methods=["POST"])
def users_destroy(user_id):
    """Handle form submission for deleting an existing user"""

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect("/users")


##############################################################################
# Post route


@app.route("/users/<int:user_id>/posts/new")
def new_post(user_id):
    user = User.query.get_or_404(user_id)
    return render_template("/new_post.html", user=user)


@app.route("/users/<int:user_id>/posts/new", methods=["POST"])
def add_post(user_id):
    user = User.query.get_or_404(user_id)
    new_post = Post(
        title=request.form["title"],
        content=request.form["content"],
        user=user,
    )

    db.session.add(new_post)
    db.session.commit()

    return redirect(f"/{user.id}")


@app.route("/users/<int:post_id>")
def show_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("/show_post.html", post=post)


@app.route("/users/<int:post_id>/edit")
def edit_post(post_id):
    """Show a form to edit an existing post"""

    post = Post.query.get_or_404(post_id)
    return render_template("/edit_post.html", post=post)


@app.route("/users/<int:post_id>/edit", methods=["POST"])
def handle_edit_post(post_id):
    """Handle form submission for updating an existing post"""

    post = Post.query.get_or_404(post_id)
    post.title = request.form["title"]
    post.content = request.form["content"]

    db.session.add(post)
    db.session.commit()

    return redirect(f"/{post.user_id}")


@app.route("/users/<int:post_id>/delete", methods=["POST"])
def delete_post(post_id):
    """Handle form submission for deleting an existing post"""

    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()

    return redirect(f"/users/{post.user_id}")
