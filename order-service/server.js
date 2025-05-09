const express = require("express");
const dotenv = require("dotenv");
const connectDB = require("./config/db");
const orderRoutes = require("./routes/orderRoutes");
const swaggerUI = require("swagger-ui-express");
const swaggerSpec = require("./swagger");
const { protect } = require("./middlewares/authMiddleware");

dotenv.config();
connectDB();

const app = express();
app.use(express.json());

app.use("/api-docs", swaggerUI.serve, swaggerUI.setup(swaggerSpec));

app.use("/api/orders", protect, orderRoutes);

const port = process.env.PORT || 3002;

app.listen(port, () => {
  console.log(`Order Service running on port ${port}`);
});
