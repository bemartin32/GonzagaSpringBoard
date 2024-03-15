import React from "react";
import "./App.css";
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";

import Chips from "./chips";
import Candy from "./candy";
import Pop from "./pop";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/chips" element={<Chips />} />
          <Route path="/candy" element={<Candy />} />
          <Route path="/pop" element={<Pop />} />
        </Routes>
        <img src="https://giphy.com/gifs/season-3-the-simpsons-3x3-3orieSZhqmslIgWTlu" />
        <p>HELLO I AM A VENDING MACHINE. WHAT WOULD YOU LIKE TO EAT?</p>
      </BrowserRouter>
    </div>
  );
}

export default App;
