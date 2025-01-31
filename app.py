from config import app


@app.route('/')
def home():
    return "Hello, NBA Stats!"


if __name__ == '__main__':
    app.run(debug=True)