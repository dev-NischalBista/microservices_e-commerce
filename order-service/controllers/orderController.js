const Order = require("../models/Order");

// Create a new order
exports.createOrder = async (req, res) => {
  try {
    const orderData = {
      ...req.body,
      userId: req.user.id, // Attach the userId from decoded JWT
    };

    const newOrder = await Order.create(orderData);
    res.status(201).json(newOrder);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
};

// Get all orders (admin gets all, users get only their own)
exports.getOrders = async (req, res) => {
  try {
    const query =
      req.user.role === "admin"
        ? {} // Admin sees all orders
        : { userId: req.user.id }; // Regular users see only their orders

    const orders = await Order.find(query);
    res.json(orders);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

// Get a single order
exports.getOrderById = async (req, res) => {
  try {
    const order = await Order.findById(req.params.id);
    if (!order) return res.status(404).json({ message: "Order not found" });

    // Check ownership unless admin
    if (req.user.role !== "admin" && order.userId.toString() !== req.user.id) {
      return res.status(403).json({ message: "Access denied" });
    }

    res.json(order);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

// Update an order
exports.updateOrder = async (req, res) => {
  try {
    const order = await Order.findById(req.params.id);
    if (!order) return res.status(404).json({ message: "Order not found" });

    // Only admin can update orders
    if (req.user.role !== "admin") {
      return res.status(403).json({ message: "Access denied" });
    }

    const updatedOrder = await Order.findByIdAndUpdate(
      req.params.id,
      req.body,
      { new: true }
    );

    res.json(updatedOrder);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
};

// Delete an order
exports.deleteOrder = async (req, res) => {
  try {
    const order = await Order.findById(req.params.id);
    if (!order) return res.status(404).json({ message: "Order not found" });

    // Only admin can delete orders
    if (req.user.role !== "admin") {
      return res.status(403).json({ message: "Access denied" });
    }

    await order.deleteOne();
    res.json({ message: "Order deleted successfully" });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};
