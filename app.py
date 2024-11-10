from flask import Flask, render_template, request
from model import generate_poem  # Import the poem generation function from generate.py

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate_poem', methods=['POST'])
def generate_poem_route():
    prompt = request.form.get('prompt')

    # Generate the poem using the generate_poem function from generate.py
    try:
        generated_poem = generate_poem(prompt)
        return render_template('index.html', poem=generated_poem)
    except Exception as e:
        return f"An error occurred: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)
