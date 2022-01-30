// server/index.js

const express = require("express");
const PORT = process.env.PORT || 3001;
const app = express();

const { MongoClient } = require("mongodb");
const uri = "mongodb+srv://freeride_website:JmtYkC65cKBFQIeZ@freeride.szxuf.mongodb.net/leaderboards?retryWrites=true&w=majority";
const client = new MongoClient(uri);
client.connect();
const db = client.db('leaderboards');

app.get("/api", (req, res) => {
    //rows = getLeaderboards().then(console.log).catch(console.error).finally(() => client.close());
    console.log("GET request");
    // db.collection('original_map').find().next().then((records) => {
    //   res.send(JSON.stringify(records))
    // });
    db.collection('original_map').find().toArray().then((records) => {
      //res.send(JSON.parse(JSON.stringify(records)));
      res.json(records);
    });
});

app.listen(PORT, () => {
  console.log(`Server listening on ${PORT}`);
});