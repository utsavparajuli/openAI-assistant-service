from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/endpoint', methods=['POST'])
def handle_post_request():
    # Check if the request contains JSON data
    if request.is_json:
        # Get JSON data from the request
        data = request.get_json()

        # Process the received data
        # For demonstration, we'll just print the received data
        print("Received data from C# backend:")
        print(data)

        # Return a response (optional)
        response_data = {'message': 'Data received successfully'}
        return jsonify(response_data), 200
    else:
        return jsonify({'error': 'Request must contain JSON data'}), 400


if __name__ == '__main__':
    app.run()
