from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

Base = declarative_base()


class Dostawa(Base):
    __tablename__ = 'dostawa'

    id = Column(Integer, primary_key=True)
    adresDostawcy = Column(String)
    nazwaDostawcy = Column(String)
    dataDostawy = Column(String)
    ocenaDostawy = Column(Integer)

    produkty = relationship("Produkt")

    def __init__(self, adresDostawcy, nazwaDostawcy, dataDostawy):
        self.adresDostawcy = adresDostawcy
        self.nazwaDostawcy = nazwaDostawcy
        self.dataDostawy = dataDostawy

    def __repr__(self):
        return "<Dostawa(adresDostawcy='%s', nazwaDostawcy='%s', dataDostawy='%s')>" % (
                                         self.adresDostawcy, self.nazwaDostawcy, self.dataDostawy)

class Produkt(Base):
    __tablename__ = 'produkt'

    id = Column(Integer, primary_key=True)
    liczbaNaStanie = Column(Integer)
    typ = Column(Integer, ForeignKey('typProduktu.id'))

    def __init__(self, liczbaNaStanie, typ):
        self.liczbaNaStanie = liczbaNaStanie
        self.typ = typ

    def __repr__(self):
        return "<Produkt(liczbaNaStanie = %d, typ='%d')>" % (
            self.liczbaNaStanie, self.typ)

class TypProduktu(Base):
    __tablename__ = 'typProduktu'

    id = Column(Integer, primary_key=True)
    nazwa = Column(String)

    def __init__(self, nazwa):
        self.nazwa = nazwa

    def __repr__(self):
        return "<TypProduktu(nazwa = %s)>" % (
            self.nazwa)

engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()