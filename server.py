from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Deploying Flask Application using AWS ECR'
        
if __name__ == "__main__":
    app.run()