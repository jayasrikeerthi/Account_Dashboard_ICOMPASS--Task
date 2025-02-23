from flask import Flask
from config import Config 
from extensions import db, migrate  # Import db and migrate from extensions.py
from flask_migrate import Migrate
from routes import routes_bp  

app = Flask(__name__, static_folder="static")

# Load configuration from Config class
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
migrate.init_app(app, db)

# Import and register Blueprint after initializing app
from routes import routes_bp  
app.register_blueprint(routes_bp)  

if __name__ == "__main__":
    app.run(debug=True)

