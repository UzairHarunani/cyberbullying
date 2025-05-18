import openai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 🔑 Paste your actual OpenAI API key here
openai.api_key = "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"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chatbot", methods=["POST"])
def chatbot():
    user_input = request.json.get("message", "")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Or use "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are a helpful and kind cyberbullying support assistant for children."},
                {"role": "user", "content": user_input}
            ],
            temperature=0.7
        )
        reply = response['choices'][0]['message']['content']
        return jsonify({"response": reply})

    except Exception as e:
        print(f"[ERROR] {e}")
        return jsonify({"response": "Sorry, I'm having trouble answering right now."})

if __name__ == "__main__":
    app.run(debug=True)
