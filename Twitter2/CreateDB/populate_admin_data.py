__author__ = 'hkapadia'
#Run once after creating new db to populate admin data
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from createdb2 import Reliability, Category, City

db = create_engine('sqlite:///tutorial1.db',
                   echo=False, )
Base = declarative_base()
DBSession = sessionmaker(bind=db)
session = DBSession()

#Populate Admin Data
if session.query(Reliability).get(0) is None:
    reliability1 = Reliability(description='High')
    reliability2 = Reliability(description='Medium')
    reliability3 = Reliability(description='Low')
    session.add(reliability1)
    session.add(reliability2)
    session.add(reliability3)
    session.commit()
else:
    print "Reliability data already populated"

if session.query(Category).get(0) is None:
    category1 = Category(description='protest')
    category2 = Category(description='Bombblast')
    category3 = Category(description='killing')
    session.add(category1)
    session.add(category2)
    session.add(category3)
    session.commit()
else:
    print "Category data already populated"

if session.query(City).get(0) is None:
     City1 = City(name='Karachi')
     session.add(City1)
     session.commit()
else:
    print "City data already populated"