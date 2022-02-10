// server/index.js

const express = require("express");
const path = require('path')
const PORT = process.env.PORT || 3001;
const app = express();

const { MongoClient } = require("mongodb");
const uri = "mongodb+srv://freeride_website:JmtYkC65cKBFQIeZ@freeride.szxuf.mongodb.net/leaderboards?retryWrites=true&w=majority";
const client = new MongoClient(uri);
client.connect();
const db = client.db('leaderboards');

app.use(express.static(path.resolve(__dirname, '../frontend/build')))

app.get("/api", (req, res) => {
    console.log("GET request");
    db.collection('original_map').find().toArray().then((records) => {
      res.json(records);
    });
});

app.get('*', (req, res) => {
  res.sendFile(path.resolve(__dirname, '../frontend/build', 'index.html'));
})

app.listen(PORT, () => {
  console.log(`Server listening on ${PORT}`);
});