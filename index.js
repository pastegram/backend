import express from "express";
import cors from "cors";

const app = express();

app.use(cors());
app.use(express.json());

app.get("/", (req, res) => {
  res.json("Hello");
});

app.listen(process.env.PORT || 8000, () => {
  console.log("Running :)");
});
