const fruit = [
  "Apple",
  "Apricot",
  "Avocado 🥑",
  "Banana",
  "Bilberry",
  "Blackberry",
  "Blackcurrant",
  "Blueberry",
  "Boysenberry",
  "Currant",
  "Cherry",
  "Coconut",
  "Cranberry",
  "Cucumber",
  "Custard apple",
  "Damson",
  "Date",
  "Dragonfruit",
  "Durian",
  "Elderberry",
  "Feijoa",
  "Fig",
  "Gooseberry",
  "Grape",
  "Raisin",
  "Grapefruit",
  "Guava",
  "Honeyberry",
  "Huckleberry",
  "Jabuticaba",
  "Jackfruit",
  "Jambul",
  "Juniper berry",
  "Kiwifruit",
  "Kumquat",
  "Lemon",
  "Lime",
  "Loquat",
  "Longan",
  "Lychee",
  "Mango",
  "Mangosteen",
  "Marionberry",
  "Melon",
  "Cantaloupe",
  "Honeydew",
  "Watermelon",
  "Miracle fruit",
  "Mulberry",
  "Nectarine",
  "Nance",
  "Olive",
  "Orange",
  "Clementine",
  "Mandarine",
  "Tangerine",
  "Papaya",
  "Passionfruit",
  "Peach",
  "Pear",
  "Persimmon",
  "Plantain",
  "Plum",
  "Pineapple",
  "Pomegranate",
  "Pomelo",
  "Quince",
  "Raspberry",
  "Salmonberry",
  "Rambutan",
  "Redcurrant",
  "Salak",
  "Satsuma",
  "Soursop",
  "Star fruit",
  "Strawberry",
  "Tamarillo",
  "Tamarind",
  "Yuzu",
];

const input = document.querySelector("#fruit");
const suggestions = document.querySelector(".suggestions ul");

input.addEventListener("keyup", searchHandler);
input.addEventListener("keydown", search);
suggestions.addEventListener("click", useSuggestion);

function search(str) {
  let results = [];
  for (let i = 0; i < fruit.length; i++) {
    if (fruit[i].toLowerCase().includes(str)) {
      results.push(fruit[i]);
    }
  }
  return results;
}

function searchHandler() {
  let userInput = input.value.toLowerCase();
  let results = search(userInput);
  showSuggestions(results);
}

function showSuggestions(results) {
  const list = document.querySelector("ul");
  list.innerHTML = "";
  for (let i = 0; i < results.length; i++) {
    let fruitList = document.createElement("li");
    fruitList.textContent = results[i];
    list.appendChild(fruitList);
  }
}

function useSuggestion(e) {
  if (e.target.tagName === "LI") {
    let selectFruit = e.target.textContent;
    input.value = selectFruit;
    suggestions.innerHTML = "";
  }
}
