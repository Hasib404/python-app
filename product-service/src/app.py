from flask import Flask, jsonify, request

products = [
    {'id': 1, 'name': 'Product 1'},
    {'id': 2, 'name': 'Product 2'}
]

app = Flask(__name__)


@app.route('/products')
def get_products():
    return jsonify(products)


@app.route('/product/<int:id>')
def get_product(id):
    product_list = [product for product in products if product['id'] == id]
    if len(product_list) == 0:
        return f'Product with id {id} not found', 404
    return jsonify(product_list[0])

    
@app.route('/product', methods=['POST'])
def post_product():
    # Retrieve the product from request body
    request_product = request.json

    # generate an ID fro the post
    new_id = max([product['id'] for product in products]) + 1

    #create a new product
    new_product = {
        'id': new_id,
        'name': request_product['name']
    }

    #append the new product to our product list
    products.append(new_product)

    # Return new product back to the client
    return jsonify(new_product), 201\


@app.route('/product/<int:id>', methods=['PUT'])
def put_product(id):
    #Get the request payload
    Updated_product = request.json

    #Find the product with the specified ID
    for product in products:
        if product['id'] == id:
            #Update the product name
            product['name'] = Updated_product['name']
            return jsonify(product), 200
    
    return f'Product with id {id} not found', 404


@app.route('/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    #Find the product with the specified id
    product_list = [product for product in products if product['id'] == id]
    if len(product_list) == 1:
        products.remove(product_list[0])
        return f'Product with id {id} deleted', 200

    return f'Product with id {id} not found', 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
