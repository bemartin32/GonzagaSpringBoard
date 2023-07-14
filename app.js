const gifArea = document.getElementById("gif-area");
const searchInput = document.getElementById("search");

function addGif(res) {
  let numResults = res.data.length;
  if (numResults) {
    let randomIdx = Math.floor(Math.random() * numResults);
    let newCol = document.createElement("div");
    newCol.className = "col-md-4 col-12 mb-4";
    let newGif = document.createElement("img");
    newGif.src = res.data[randomIdx].images.original.url;
    newGif.className = "w-100";
    newCol.appendChild(newGif);
    gifArea.appendChild(newCol);
  }
}

document.querySelector("form").addEventListener("submit", async function (evt) {
  evt.preventDefault();

  let searchTerm = searchInput.value;
  searchInput.value = "";

  const response = await axios.get("http://api.giphy.com/v1/gifs/search", {
    params: {
      q: searchTerm,
      api_key: "MhAodEJIJxQMxW9XqxKjyXfNYdLoOIym",
    },
  });
  addGif(response.data);
});

document.getElementById("remove").addEventListener("click", function () {
  gifArea.innerHTML = "";
});
