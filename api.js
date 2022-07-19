const express = require("express");
const fs = require("fs");

const path = "./potter.json";

const app = express();

let json = fs.readFileSync(path, { encoding: "utf-8" });

app.get("/", (req, res) => {
  let { spells } = JSON.parse(json);
  let randomIndex = Math.floor(Math.random() * spells.length - 1);
  let random = spells[randomIndex];
  res.json(random);
});

app.use("/:any", (req, res) => {
  res.redirect("/");
});

app.listen(process.env.PORT || 3000);
