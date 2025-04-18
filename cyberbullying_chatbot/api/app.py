from flask import Flask, request, jsonify, render_template  
import random  

app = Flask(__name__)  

# Predefined responses for known questions  
responses = {  
    "what is cyberbullying": [  
        "Cyberbullying is bullying that occurs through digital platforms.",  
        "Cyberbullying involves using technology to harass, embarrass, or harm others.",  
        "It can happen through social media, text messages, or websites."  
    ],  
    "how can i prevent cyberbullying": [  
        "Encourage open communication about online experiences.",  
        "Educate about the importance of not sharing personal information online.",  
        "Report and block bullies on platforms and encourage others to do the same."  
    ],  
    "what should i do if i'm being bullied": [  
        "Talk to a trusted adult about your experience.",  
        "Document the instances of bullying.",  
        "Consider reporting the behavior to the platform."  
    ],  
}  

@app.route('/')  
def home():  
    return render_template('index.html')  # Serve the HTML file  

@app.route('/api/ask', methods=['POST'])  # API endpoint for questions  
def ask():  
    user_question = request.form['question'].lower()  # Get user question in lowercase  
    print(f"Received question: {user_question}")  # Debugging statement  

    for key in responses:  
        if key in user_question:  # Check if the question is in the predefined responses  
            answer = random.choice(responses[key])  # Randomly select a response  
            return jsonify({'answer': answer})  # Return the answer in JSON  

    return jsonify({'answer': "I'm sorry, I don't have an answer for that."})  # Default response  

# Vercel runs the app  
if __name__ == "__main__":  
    app.run()  