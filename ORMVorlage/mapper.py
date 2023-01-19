
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import max
from dbConnect import sessionLoader

# Definition von Base - Basisklasse für Definition der Mapping-Klassen
Base = declarative_base()

class Niederlassung(Base):
    """ Definition der Klasse "Niederlassung"
    Mappingklasse der DB-Tabelle Niederlassung"""
    # Definition des Zugriffes auf die Tabelle Niederlassung
    # Anlegen der Spalten mit den richtigen Datentypen
    # Solange die Daten nur angezeigt werden, müssen nicht alle Spalten definiert werden
    __tablename__ = 'Niederlassung'
    NlNr = Column('NLNr', Integer, primary_key=True, autoincrement=False)
    Ort  = Column('Ort', String(50))
    ListeMitarbeiter = relationship("Mitarbeiter", 
                                    back_populates="Niederlassung") 


class Mitarbeiter(Base):
    """ Definition der Klasse "Mitarbeiter"
    """
    __tablename__ = 'Mitarbeiter'
    MitId         = Column('MitID', String(3), primary_key=True, autoincrement=False)
    Name          = Column('MitName', String(20))
    Vorname       = Column('MitVorname', String(20))
    Geburtsdatum  = Column('MitGebDat', Date)
    Job           = Column('MitJob', String(20))
    Stundensatz   = Column('MitStundensatz', Float)
    NlNr          = Column('NLNr', Integer, ForeignKey(Niederlassung.NlNr))
    Niederlassung = relationship('Niederlassung', back_populates="ListeMitarbeiter")
    ListeAuftrag  = relationship("Auftrag", 
                                    back_populates="Mitarbeiter") 


class Kunde(Base):
    """ Definition der Klasse "Kunde"
    """
    __tablename__ = 'Kunde'
    KunNr   = Column('KunNr', Integer, primary_key=True, autoincrement=False)
    Name    = Column('KunName', String(20))
    Ort     = Column('KunOrt', String(20))
    Plz     = Column('KunPLZ', String(5))
    Strasse = Column('KunStrasse', String(20))
    ListeAuftrag  = relationship("Auftrag", 
                                    back_populates="Kunde") 

    # autoincrement=False MUSS für das Primärschlüsselfeld gesetzt werden, wenn Daten in der Tabelle hinzugefügt
    # werden sollen

    def __init__(self, kunname, kunort, kunplz, kunstrasse):
        """ Definition des Constructors der Klasse Kunde.

        Anlegen eines neuen Kunden

        :param self - Referenz auf die Klasse selbst
        :param kunname - Name des Kunden
        :param kunort - Ort des Kunden
        :param kunplz - Plz des Ortes des Kunden
        :param kunstrasse - Strasse des Kunden
        """
        # Ermitteln der nächsten Kundennummer
        session = sessionLoader()
        maxkunnr = session.query(max(Kunde.KunNr)).first()  # bisher größter Kundennummer
        self.KunNr = int(maxkunnr[0]) + 1                      # lesen des Wertes der Kundennummer plus 1
        session.close()

        self.Name = kunname
        self.Ort = kunort
        self.Plz= kunplz
        self.Strasse = kunstrasse


class Auftrag(Base):
    """ Definition der Klasse "Auftrag"
    """
    __tablename__ = 'Auftrag'
    AufNr            = Column('Aufnr', Integer, primary_key=True, autoincrement=False)
    MitId            = Column('MitID', String(3), ForeignKey(Mitarbeiter.MitId), nullable=True)
    KunNr            = Column('KunNr', Integer, ForeignKey(Kunde.KunNr))
    Auftragsdatum    = Column('AufDat', Date)
    Erledigungsdatum = Column('Erldat', Date, nullable=True)
    Dauer            = Column('Dauer', Float, nullable=True)
    Anfahrt          = Column('Anfahrt', Integer, nullable=True)
    Mitarbeiter = relationship('Mitarbeiter', back_populates="ListeAuftrag")
    Kunde       = relationship('Kunde', back_populates="ListeAuftrag")
    ListeMontage = relationship("Montage", back_populates="Auftrag")

    def __init__(self, kunnr, aufdat):
        """ Definition des Constructors der Klasse Auftrag.

        Anlegen eines neuen Auftrags mit Auftragsdatum, Kundennummer, Auftragsnummer. Die anderen Felder bleiben leer.

        :param self - Referenz auf die Klasse selbst
        :param kunnr - Nummer des Kunden
        :param aufdat - Datum des Auftragseinganges
        """
        # Ermitteln der neuen Auftragsnummer
        session = sessionLoader()
        maxaufnr = session.query(max(Auftrag.AufNr)).first()  # ermitteln der bisher größten Auftragsnummer
        self.AufNr = int(maxaufnr[0]) + 1                        # lesen des Wertes der Auftragsnummer plus 1
        session.close()

        self.KunNr = kunnr
        self.Auftragsdatum = aufdat

class Ersatzteil(Base):
    """ Definition der Klasse "Ersatzteile"
    """ 
    __tablename__ = 'Ersatzteil'
    EtID           = Column('EtID', Integer, primary_key=True, autoincrement=False)
    EtBezeichnung  = Column('EtBezeichnung', String(20))
    EtPreis        = Column('EtPreis', Float)
    EtAnzLager     = Column('EtAnzLager', Integer)  
    EtHersteller   = Column('EtHersteller', String(20))
    ListeMontage   = relationship("Montage", back_populates="Ersatzteil")

class Montage(Base):
    """ Definition der Klasse "Montage"
    """
    __tablename__ = 'Montage'
    EtID        = Column('EtId', Integer, ForeignKey(Ersatzteil.EtID), primary_key=True, autoincrement=False)
    AufNr       = Column('AufNr', Integer, ForeignKey(Auftrag.AufNr), primary_key=True, autoincrement=False)
    Anzahl      = Column('Anzahl', Float)
    Ersatzteil  = relationship('Ersatzteil', back_populates="ListeMontage")
    Auftrag     = relationship('Auftrag', back_populates="ListeMontage")




