from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Trinetra AI Server is Running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    # Placeholder for AI logic
    result = {"message": "This is a placeholder response", "received_data": data}
    return jsonify(result)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
