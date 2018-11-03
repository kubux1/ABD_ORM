from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

Base = declarative_base()


class Gym(Base):
    __tablename__ = 'gyms'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    roomsQuantity = Column(Integer)

    groupClass = relationship("GroupClass")
    coach = relationship("Coach")

    def __init__(self, name, address, roomsQuantity):
        self.name = name
        self.address = address
        self.roomsQuantity = roomsQuantity

    def __repr__(self):
        return "<Gym(name='%s', address='%s', roomsQuantity='%d')>" % (
                                         self.name, self.address, self.roomsQuantity)


class Coach(Base):
    __tablename__ = 'coaches'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    gymFKID = Column(Integer, ForeignKey('gyms.id'))

    gym = relationship("Gym", backref=backref('coaches', order_by=id))
    groupClass = relationship("GroupClass")

    def __init__(self, id, name, surname):
        self.id = id
        self.name = name
        self.surname = surname

    def __repr__(self):
        return "<Coach(id = %d, name='%s', surname='%s')>" % (


self.id, self.name, self.surname)

class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    sex = Column(String)
    age = Column(Integer)
    enrollment = relationship("Enrollment")

    def __init__(self, id, name, surname, sex, age):
        self.id = id
        self.name = name
        self.surname = surname
        self.sex = sex
        self.age = age

    def __repr__(self):
        return "<Client(id=%d, name='%s', surname='%s', Sex='%s', Age='%d')>" % (
                                         self.id, self.name, self.surname, self.sex, self.age)


class GroupClass(Base):
    __tablename__ = 'groupClasses'

    id = Column(Integer, primary_key=True)
    className = Column(String)
    maxSeats = Column(Integer)
    gymID = Column(Integer, ForeignKey('gyms.id') )
    coachID = Column(Integer, ForeignKey('coaches.id'))
    term = relationship("Term")

    def __init__(self, className, maxSeats):
        self.className = className
        self.maxSeats = maxSeats

    def __repr__(self):
        return "<GroupClass(className='%s', maxSeats='%d')>" % (
                                         self.className, self.maxSeats)


class Term(Base):
    __tablename__ = 'terms'

    id = Column(Integer, primary_key=True)
    classDate = Column(String)
    duration = Column(Integer)
    groupClassID = Column(Integer, ForeignKey('groupClasses.id'))
    enrollment = relationship("Enrollment")

    def __init__(self, classDate, duration):
        self.classDate = classDate
        self.duration = duration

    def __repr__(self):
        return "<GroupClass(classDate='%s', duration='%d')>" % (
                                         self.classDate, self.duration)


class Enrollment(Base):
    __tablename__ = 'enrollments'

    id = Column(Integer, primary_key=True)
    clientID = Column(Integer, ForeignKey('clients.id'))
    termID = Column(Integer, ForeignKey('terms.id'))

    def __init__(self, clientID, termID):
        self.clientID = clientID
        self.termID = termID

    def __repr__(self):
        return "<Enrollment(clientID='%d', termID='%d')>" % (
            self.clientID, self.termID)


engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()