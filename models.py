
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'Users'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

class Category(db.Model):
    __tablename__ = 'Categories'
    category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

class Product(db.Model):
    __tablename__ = 'Products'
    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('Categories.category_id'), nullable=True)
    image_url = db.Column(db.String(255))

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "description": self.description,
            "price": float(self.price),
            "category_id": self.category_id,
            "image_url": self.image_url
        }

class Order(db.Model):
    __tablename__ = 'Orders'
    order_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'), nullable=False)
    total_price = db.Column(db.Numeric(10, 2), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

class OrderDetail(db.Model):
    __tablename__ = 'OrderDetails'
    order_detail_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('Orders.order_id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('Products.product_id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)

class Cart(db.Model):
    __tablename__ = 'Cart'
    cart_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('Products.product_id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
