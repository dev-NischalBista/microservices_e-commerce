const jwt = require("jsonwebtoken");

exports.protect = (req, res, next) => {
  const authHeader = req.headers.authorization;

  if (authHeader?.startsWith("Bearer ")) {
    const token = authHeader.split(" ")[1];

    try {
      const decoded = jwt.verify(token, process.env.JWT_ACCESS_SECRET);
      req.user = decoded;
      return next();
    } catch (err) {
      return res.status(401).json({ message: "Invalid token" });
    }
  }

  res.status(401).json({ message: "No token provided" });
};
