from sql_connection import get_sql_connection

def get_all_products(connection):
    cursor = connection.cursor()
    query = ("SELECT products.product_id, products.name, products.unit_id, products.price_per_unit, unit.unit_name "
             "FROM products INNER JOIN unit ON products.unit_id=unit.unit_id")
    cursor.execute(query)
    response = []
    for (product_id, name, unit_id, price_per_unit, unit_name) in cursor:
        response.append({
            'product_id': product_id,
            'name': name,
            'unit_id': unit_id,
            'price_per_unit': price_per_unit,
            'unit_name': unit_name
        })
    cursor.close()  # Close the cursor after fetching data
    return response

def get_product_by_id(connection, product_id):
    cursor = connection.cursor()
    query = ("SELECT product_id, name, unit_id, price_per_unit FROM products WHERE product_id=%s")
    cursor.execute(query, (product_id,))
    product = cursor.fetchone()
    cursor.close()
    if product:
        return {
            'product_id': product[0],
            'name': product[1],
            'unit_id': product[2],
            'price_per_unit': product[3]
        }
    return None

def insert_new_products(connection, products):
    cursor = connection.cursor()
    query = ("INSERT INTO products "
             "(name, unit_id, price_per_unit)"
             "VALUES (%s, %s, %s)")
    data = (products['name'], products['unit_id'], products['price_per_unit'])

    cursor.execute(query, data)
    connection.commit()
    cursor.close()  # Close the cursor after the operation

    return cursor.lastrowid

def delete_products(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products WHERE product_id=%s")
    cursor.execute(query, (product_id,))
    connection.commit()
    cursor.close()  # Close the cursor after the operation

    return cursor.lastrowid

if __name__ == '__main__':
    connection = get_sql_connection()
    # print(get_all_products(connection))
    # print(insert_new_products(connection, {
    #     'products_name': 'potatoes',
    #     'unit_id': '1',
    #     'price_per_unit': 10
    # }))
    print(insert_new_products(connection, {
        'products_name': 'spinach',
        'unit_id': '2',
        'price_per_unit': 5
    }))
