from flask import Flask, render_template, request
from integrate_AI_to_flask import llama2_model

app = Flask(__name__)
@app.route('/')


def ask():
    prompt = "You are a customer service representative. Please introduce yourself."
    result = llama2_model.generate_text(prompt)
    # result = mixtral_model.generate_text(prompt)
    return result
    
if __name__ == '__main__':
    app.run(debug=True)