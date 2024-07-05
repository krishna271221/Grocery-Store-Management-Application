#
# from flask import Flask, request, jsonify,render_template
# from sql_connection import get_sql_connection
# import mysql.connector
# import json
#
# import products_DAO
# import orders_DAO
# import unit_DAO
#
# app = Flask(__name__)
#
# connection = get_sql_connection()
#
# @app.route('/getunit', methods=['GET'])
# def get_unit():
#     response = unit_DAO.get_units(connection)
#     response = jsonify(response)
#     response.headers.add('Access-Control-Allow-Origin', '*')
#
#
# @app.route('/getProducts', methods=['GET'])
# def get_products():
#     response = products_DAO.get_all_products(connection)
#     response = jsonify(response)
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response
#
# @app.route('/insertProduct', methods=['POST'])
# def insert_product():
#     request_payload = json.loads(request.form['data'])
#     products_id = products_DAO.insert_new_product(connection, request_payload)
#     response = jsonify({
#         'products_id': products_id
#     })
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response
#
# @app.route('/getAllOrders', methods=['GET'])
# def get_all_orders():
#     response = orders_DAO.get_all_orders(connection)
#     response = jsonify(response)
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response
#
# @app.route('/insertOrder', methods=['POST'])
# def insert_order():
#     request_payload = json.loads(request.form['data'])
#     order_id = orders_DAO.insert_order(connection, request_payload)
#     response = jsonify({
#         'order_id': order_id
#     })
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response
#
# @app.route('/deleteProduct', methods=['POST'])
# def delete_product():
#     return_id = products_DAO.delete_product(connection, request.form['products_id'])
#     response = jsonify({
#         'products_id': return_id
#     })
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response
#
# if __name__ == "__main__":
#     print("Starting Python Flask Server For Grocery Store Management System")
#     app.run(port=5000)


# from flask import Flask, render_template, request, jsonify
# from sql_connection import get_sql_connection
# import order_DAO
# import product_DAO
# import unit_DAO
#
# app = Flask(__name__)
# connection = get_sql_connection()
#
# @app.route('/')
# def home():
#     return render_template('index.html')
#
# @app.route('/manageProducts')
# def manage_products():
#     return render_template('manage_products.html')
#
# @app.route('/newOrder')
# def new_order():
#     return render_template('new_order.html')
#
# @app.route('/getAllOrders', methods=['GET'])
# def get_all_orders():
#     orders = order_DAO.get_all_orders(connection)
#     return jsonify(orders)
#
# @app.route('/getProducts', methods=['GET'])
# def get_products():
#     products = product_DAO.get_all_products(connection)
#     return jsonify(products)
#
# @app.route('/insertProduct', methods=['POST'])
# def insert_product():
#     request_payload = request.json
#     product_id = product_DAO.insert_new_products(connection, request_payload)
#     response = jsonify({
#         'product_id': product_id
#     })
#     return response
#
# @app.route('/deleteProduct', methods=['POST'])
# def delete_product():
#     request_payload = request.json
#     product_DAO.delete_products(connection, request_payload['product_id'])
#     return '', 204
#
# @app.route('/getUnits', methods=['GET'])
# def get_units():
#     units = unit_DAO.get_units(connection)
#     return jsonify(units)
#
# if __name__ == "__main__":
#     app.run(port=5000, debug=True)


# from flask import Flask, render_template, request, jsonify
# from sql_connection import get_sql_connection
# import product_DAO
# import order_DAO
# import unit_DAO
# 
# app = Flask(__name__)
# 
# @app.route('/')
# def home():
#     return render_template('index.html')
# 
# @app.route('/manageProducts')
# def manage_products():
#     return render_template('manage_products.html')
# 
# @app.route('/newOrder')
# def new_order():
#     return render_template('new_order.html')
# 
# @app.route('/getProducts')
# def get_products():
#     connection = get_sql_connection()
#     products = product_DAO.get_all_products(connection)
#     return jsonify(products)
# 
# @app.route('/getUnits')
# def get_units():
#     connection = get_sql_connection()
#     units = unit_DAO.get_units(connection)
#     return jsonify(units)
# 
# @app.route('/insertProduct', methods=['POST'])
# def insert_product():
#     connection = get_sql_connection()
#     product = request.get_json()
#     product_id = product_DAO.insert_new_products(connection, product)
#     return jsonify({'product_id': product_id})
# 
# @app.route('/deleteProduct/<int:product_id>', methods=['DELETE'])
# def delete_product(product_id):
#     connection = get_sql_connection()
#     product_DAO.delete_products(connection, product_id)
#     return jsonify({'product_id': product_id})
# 
# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, render_template, request, jsonify
# from sql_connection import get_sql_connection
# import product_DAO
# import order_DAO
# import unit_DAO
#
# app = Flask(__name__)
#
# @app.route('/')
# def home():
#     return render_template('index.html')
#
# @app.route('/manageProducts')
# def manage_products():
#     return render_template('manage_products.html')
#
# @app.route('/newOrder')
# def new_order():
#     return render_template('new_order.html')
#
# @app.route('/getProducts')
# def get_products():
#     connection = get_sql_connection()
#     products = product_DAO.get_all_products(connection)
#     connection.close()  # Close connection after use
#     return jsonify(products)
#
# @app.route('/getUnits')
# def get_units():
#     connection = get_sql_connection()
#     units = unit_DAO.get_units(connection)
#     connection.close()  # Close connection after use
#     return jsonify(units)
#
# @app.route('/insertProduct', methods=['POST'])
# def insert_product():
#     connection = get_sql_connection()
#     product = request.get_json()
#     product_id = product_DAO.insert_new_products(connection, product)
#     connection.close()  # Close connection after use
#     return jsonify({'product_id': product_id})
#
# @app.route('/deleteProduct/<int:product_id>', methods=['DELETE'])
# def delete_product(product_id):
#     connection = get_sql_connection()
#     product_DAO.delete_products(connection, product_id)
#     connection.close()  # Close connection after use
#     return jsonify({'product_id': product_id})
#
# if __name__ == '__main__':
#     app.run(debug=True)
#

from flask import Flask, render_template, request, jsonify
from sql_connection import get_sql_connection
import product_DAO
import order_DAO
import unit_DAO

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

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

@app.route('/insertProduct', methods=['POST'])
def insert_product():
    connection = get_sql_connection()
    product = request.get_json()
    product_id = product_DAO.insert_new_product(connection, product)
    connection.close()  # Close connection after use
    return jsonify({'product_id': product_id})

@app.route('/deleteProduct/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    connection = get_sql_connection()
    product_DAO.delete_product(connection, product_id)
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

if __name__ == '__main__':
    app.run(debug=True)
