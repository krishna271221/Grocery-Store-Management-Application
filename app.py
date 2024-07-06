from flask import Flask, render_template, request, jsonify
from sql_connection import get_sql_connection
import product_DAO
import order_DAO
import unit_DAO

app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

@app.route('/')
def home():
    connection = get_sql_connection()
    orders = order_DAO.get_all_orders(connection)
    connection.close()
    return render_template('index.html', orders=orders)

@app.route('/manageProducts')
def manage_products():
    return render_template('manage_products.html')

@app.route('/newOrder')
def new_order():
    return render_template('new_order.html')

@app.route('/getProducts')
def get_products():
    connection = get_sql_connection()
    products = product_DAO.get_all_products(connection)
    connection.close()  # Close connection after use
    return jsonify(products)

@app.route('/getProduct/<int:product_id>')
def get_product(product_id):
    connection = get_sql_connection()
    product = product_DAO.get_product_by_id(connection, product_id)
    connection.close()  # Close connection after use
    return jsonify(product)

@app.route('/getUnits')
def get_units():
    connection = get_sql_connection()
    units = unit_DAO.get_units(connection)
    connection.close()
    return jsonify(units)


@app.route('/insertProduct', methods=['POST'])
def insert_product():
    connection = get_sql_connection()
    product = request.get_json()
    product_id = product_DAO.insert_new_products(connection, product)
    connection.close()  # Close connection after use
    return jsonify({'product_id': product_id})

@app.route('/deleteProduct/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    connection = get_sql_connection()
    product_DAO.delete_products(connection, product_id)
    connection.close()  # Close connection after use
    return jsonify({'product_id': product_id})

@app.route('/insertOrder', methods=['POST'])
def insert_order():
    connection = get_sql_connection()
    order = request.get_json()
    order_id = order_DAO.insert_order(connection, order)
    order_details = order_DAO.get_order_details(connection, order_id)
    connection.close()  # Close connection after use
    return jsonify(order_details)

@app.route('/deleteOrder/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    connection = get_sql_connection()
    order_DAO.delete_order(connection, order_id)
    connection.close()
    return jsonify({'order_id': order_id})
if __name__ == '__main__':
    app.run(debug=True)
