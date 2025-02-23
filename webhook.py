from flask import Flask, request, jsonify

app = Flask(__name__)

# Store the latest received URL
latest_url = None

@app.route('/webhook', methods=['POST'])
def webhook():
    global latest_url
    data = request.json  # Capture JSON payload
    latest_url = data.get("url", "No URL found")  # Save the URL
    print("Received URL:", latest_url)  # Debugging log

    return jsonify({"status": "success", "url": latest_url}), 200

@app.route('/latest-url', methods=['GET'])
def get_latest_url():
    """ Endpoint to get the latest received URL """
    if latest_url:
        return jsonify({"latest_url": latest_url}), 200
    return jsonify({"error": "No URL received yet"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
