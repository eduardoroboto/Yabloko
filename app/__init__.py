from flask import Flask
from flask_migrate import Migrate
from .model import configure as config_db
from .serializer import configure as config_ma
import secrets



# Create a flask app
def create_app():
  app = Flask(__name__,template_folder='templates')
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  secret = secrets.token_urlsafe(32)
  app.secret_key = secret
  #vou fazer aqui por enquanto
  
  config_db(app)
  config_ma(app)

  Migrate(app, app.db)

  from .tickets import bp_tickets
  app.register_blueprint(bp_tickets)

  from .clerks import bp_clerks
  app.register_blueprint(bp_clerks)

  from .history import bp_history
  app.register_blueprint(bp_history)


  from .tickets_view import fe_tickets
  app.register_blueprint(fe_tickets)

  from .clerk_view import fe_clerk
  app.register_blueprint(fe_clerk)

  return app


# Run the Flask app
#if __name__ == "__main__":
#  app = create_app()
#  app.run(host='0.0.0.0', debug=True, port=8000)
