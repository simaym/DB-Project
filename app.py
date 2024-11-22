
from flask import Flask, jsonify, request
from models import db, User, Product, Category, Order, Cart, OrderDetail
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/ecommerce'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(username=data['username'], email=data['email'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products])

@app.route('/cart', methods=['POST'])
def add_to_cart():
    data = request.json
    cart_item = Cart(user_id=data['user_id'], product_id=data['product_id'], quantity=data['quantity'])
    db.session.add(cart_item)
    db.session.commit()
    return jsonify({'message': 'Item added to cart'}), 201

if __name__ == '__main__':
    app.run(debug=True)
