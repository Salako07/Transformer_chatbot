from flask import Flask, request, jsonify
from transformers import pipeline

#inintialize the Flask app

app = Flask(__name__)

chatbot_model = pipeline('text-generation', model= "gpt2")

@app.route('/chat', methods=['POST'])

def chatbot():

    data = request.get_json()
    user_message = data.get('message', "")

    bot_response = chatbot_model(user_message, max_length = 20, num_return_sequence=1)
    return jsonify({"response": bot_response[0]['generated_text']})

if __name__ == '__main__':
    app.run(debug=True)