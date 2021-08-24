from sqlalchemy import engine_from_config
from helloworld import SQLALCHEMY_URL
from helloworld.models import Base
import os



#def main():
settings = {'sqlalchemy.url': SQLALCHEMY_URL}
engine = engine_from_config(settings, prefix='sqlalchemy.')

#Base.metadata.drop_all(engine)
if bool(os.environ.get('DEBUG', '')):
    Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
print("Database initialized")