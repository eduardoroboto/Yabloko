from flask import Flask
from flask_migrate import Migrate
from .model import configure as config_db
from .serializer import configure as config_ma

# Create a flask app
def create_app():
  app = Flask(__name__)
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  #vou fazer aqui por enquanto
  
  config_db(app)
  config_ma(app)

  Migrate(app, app.db)

  from .tickets import bp_tickets
  app.register_blueprint(bp_tickets)

  from .clerks import bp_clerks
  app.register_blueprint(bp_clerks)

  return app


# Run the Flask app
#if __name__ == "__main__":
#  app = create_app()
#  app.run(host='0.0.0.0', debug=True, port=8000)
