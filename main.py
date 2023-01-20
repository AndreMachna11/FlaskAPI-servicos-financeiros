from src import app
from src import routes
from flask_cors import CORS 

CORS(app)

if __name__ == '__main__':
    app.run(debug=True)

