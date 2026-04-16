from flask import Flask

app = Flask(__name__)

# Default route
@app.route('/')
def index():
    return "Welcome to Flatiron Cars"


# Model-specific route
@app.route('/<model>')
def car_model(model):
    if model == "Crossroads":
        return f"Flatiron {model} is in our fleet!"
    else:
        return f"No models called {model} exists in our catalog"


if __name__ == '__main__':
    app.run(debug=True)