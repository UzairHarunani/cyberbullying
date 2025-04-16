# app.py  
from flask import Flask, request, render_template, jsonify  
import re  
import random  

app = Flask(__name__)  

# Predefined responses for cyberbullying questions  
responses = {  
    "what is cyberbullying": [  
        "Cyberbullying is bullying that takes place over digital devices like computers and mobile phones.",  
        "It's when someone uses electronic communication to bully, harass or embarrass another person."  
    ],  
    "how can i recognize cyberbullying": [  
        "Look for signs such as sudden changes in behavior, avoidance of social situations, or becoming withdrawn.",  
        "Signs can include not wanting to go to school or having trouble sleeping."  
    ],  
    "what should i do if i'm being cyberbullied": [  
        "Talk to a trusted adult about what’s happening.",  
        "Document the incidents and report the bullying to the platform."  
    ],  
    "what can i do to prevent cyberbullying": [  
        "Educate yourself and others about safe online practices.",  
        "Encourage respectful communication and monitor online activities."  
    ],  
    "where can i get help for cyberbullying": [  
        "You can reach out to organizations like StopBullying.gov or the Cyberbullying Research Center.",  
        "There are resources available online and hotlines to provide support."  
    ],  
    "why do people do cyberbullying": [  
        "People may engage in cyberbullying due to feelings of insecurity, a desire for power, or because they believe they can act without consequences.",  
        "Sometimes, they might be repeating behavior they see in others or trying to fit in with a group."  
    ],  
}  

def preprocess_input(user_input):  
    """Process user input to a simpler format."""  
    user_input = user_input.lower()  # Convert to lowercase  
    user_input = re.sub(r'[^\w\s]', '', user_input)  # Remove punctuation  
    return user_input  

@app.route('/')  
def home():  
    return render_template('index.html')  

@app.route('/ask', methods=['POST'])  
def ask():  
    user_question = request.form['question']  
    processed_question = preprocess_input(user_question)  
    
    # Attempt to find a relevant response  
    for key in responses:  
        if key in processed_question:  
            answer = random.choice(responses[key])  
            return jsonify({'answer': answer})  

    # Default response if no match found  
    default_response = "I'm sorry, I don't have an answer for that. Can you ask something else about cyberbullying?"  
    return jsonify({'answer': default_response})  

if __name__ == '__main__':  
    app.run(debug=True)  