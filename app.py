from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey! Welcome to ArgoCD V4....checking CI/CD'
