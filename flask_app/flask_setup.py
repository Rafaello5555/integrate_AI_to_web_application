from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Good to start'
if __name__ == '__main__':
    app.run(debug=True)