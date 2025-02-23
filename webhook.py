from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json  # Capture JSON payload
    received_url = data.get("url", "No URL found")  # Extract the URL
    print("Received URL:", received_url)  # Print it for debugging

    return jsonify({"status": "success", "url": received_url}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
