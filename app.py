from config import app
from players.utils import convert_to_json

@app.route('/')
def home():
    return "Hello, NBA Stats!"


convert_to_json()

if __name__ == '__main__':
    app.run(debug=True)