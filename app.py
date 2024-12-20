import os  # Make sure to import os
from flask import Flask, request, jsonify
from transformers import pipeline

# Initialize the Flask app
app = Flask(__name__)

# Initialize the chatbot model using Hugging Face pipeline
chatbot_model = pipeline("text-generation", model="gpt2")

@app.route('/chat', methods=['POST'])
def chatbot():
    data = request.get_json()
    user_message = data.get('message', "")

    # Generate a response
    bot_response = chatbot_model(
        user_message,
        max_length=20,
        num_return_sequences=1
    )
    return jsonify({"response": bot_response[0]['generated_text']})

if __name__ == '__main__':
    # Use the PORT environment variable set by Render
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
