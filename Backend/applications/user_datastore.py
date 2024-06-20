from flask_security import SQLAlchemySessionUserDatastore
from applications.database import db
from applications.model import User,Role

user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)
