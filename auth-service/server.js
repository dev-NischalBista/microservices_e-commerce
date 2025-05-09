const express = require("express");
const dotenv = require("dotenv");
const connectDB = require("./config/db");
const authRoutes = require("./routes/userRoutes");
const swaggerUI = require("swagger-ui-express");
const swaggerSpec = require("./swagger");

dotenv.config();
connectDB();

const app = express();
app.use(express.json());

app.use("/api-docs", swaggerUI.serve, swaggerUI.setup(swaggerSpec));

app.use("/api/auth", authRoutes);

const port = process.env.PORT || 5000;
app.listen(port, () => {
  console.log(`Auth Service running on port ${port}`);
});
