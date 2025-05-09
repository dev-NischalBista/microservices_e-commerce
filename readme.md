# 🛒 E-commerce Microservices

A modular e-commerce backend built using microservices architecture. Each service is independently deployed and managed, ensuring scalability and maintainability.

---

## 🧱 Architecture Diagram

> (Add your diagram image or link here. You can use tools like [Excalidraw](https://excalidraw.com/) or [Lucidchart](https://www.lucidchart.com/) to create one.)

[Client] --> [API Gateway] --> [Auth Service] --> [Users DB]
[Product Service] --> [Products DB]
[Order Service] --> [Orders DB]

---

## 🔧 Services List

### 1. **User Service**

- Handles registration, login, JWT authentication
- Role-based access control (RBAC)

### 2. **Order Service**

- Manages cart, order creation, order history
- Validates product availability and user identity

### 3. **Product Service**

- Product listing, filtering, categories
- Admin APIs for adding/editing products

---

## 🧰 Prerequisites

Make sure you have these installed:

- [Node.js](https://nodejs.org/) (v18 or later)
- [MongoDB](https://www.mongodb.com/)
- [Docker](https://www.docker.com/) (for containerization)
- [Python](https://www.python.org/) (for FastAPI microservices)
- [FastAPI](https://fastapi.tiangolo.com/) (used in Python-based services)
- [Mongoose](https://mongoosejs.com/) (for MongoDB ODM)

---

## 🚀 How to Run the Project

### 1. Clone the Repository

git clone https://github.com/dev-NischalBista/microservices_e-commerce
