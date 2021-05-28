from flask_marshmallow import Marshmallow
from marshmallow import validates, ValidationError
from app.model import Ticket
from app.model import Clerk
from app.model import History

ma = Marshmallow()

def configure(app):
  ma.init_app(app)


class TicketSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = Ticket
    include_relationships = True
    load_instance = True

  @validates('id')
  def validade_id(self,value):
    raise ValidationError('Nao envie o id!')

class ClerkSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = Clerk
    include_relationships = True
    load_instance = True

  @validates('id')
  def validade_id(self, value):
    raise ValidationError('Nao envie o id!')


class HistorySchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = History
    include_relationships = True
    load_instance = True
    include_fk = True

  @validates('id')
  def validade_id(self, value):
    raise ValidationError('Nao envie o id!')
