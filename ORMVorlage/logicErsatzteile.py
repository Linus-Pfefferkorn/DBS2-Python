from dbConnect import sessionLoader
from mapper import Ersatzteil
from checker import handleInputInteger

def getErsatzteile():
    """ Definition der Funktion getErsatzteile
    Die Funktion ruft alle Ersatzteile ab und gibt sie tabellarisch aus.
    Der Benutzer wird aufgefordert eine Ersatzteilnummer einzugeben.

    :return eingabe_etnr - Ersatzteilnummer, die vom Benutzer eingegebn wurde
    :rtype  int
    """
    session = sessionLoader()
    # Abfrage aller Ersatzteile
    ersatzteile = session.query(Ersatzteil).all()

    # Abbruch, falls keine Ersatzteile vorhanden sind
    if len(ersatzteile) == 0:
        print('Es gibt keine Ersatzteile in der Datenbank.')
        session.close()
        return 0

    # Definition der Liste für die Ersatzteilnummern,  1. Element 0
    liste_et = [0]    
    for et in ersatzteile:
        print(f' {et.EtID} - {et.EtBezeichnung} - {et.EtPreis} -{et.EtAnzLager} - {et.EtBezeichnung}')  # Ausgabe der Daten
                   # Anhängen der Ersatzteilnummer an die Liste
    print()

def getErsatzteil2(p_aufnr):
    """ Definition der Funktion getErsatzteil
    Die Funktion ruft alle Ersatzteile mit der übergebenen Auftragsnummer ab und gibt
    sie tabellarisch aus.
    Der Benutzer wird aufgefordert eine Ersatzteilnummer einzugeben.

    .param  p_aufnr - Auftragsnummer
    :return eingabe_etnr - Ersatzteilnummer, die vom Benutzer eingegebn wurde
    :rtype  int
    """
    session = sessionLoader()
    # Abfrage der Auftrag für die übergebene Auftragsnummer
    auftrag = session.query(Auftrag).get(p_aufnr)

    # Abbruch, falls der Auftrag nicht vorhanden ist
    if isinstance(auftrag, type(None)):
        print(f'Auftrag mit der AufNr: {p_aufnr} existiert nicht in der Datenbank.')
        session.close()
        return 0

    if len(auftrag.ListeErsatzteile) > 0:
        # Definition der Liste für die Ersatzteilnummern aus dem Auftrag,  1. Element 0
        liste_et = [0]    
        for et in auftrag.ListeErsatzteile:
            print(f' {et.EtID} - {et.EtBezeichnung} - {et.EtPreis} -{et.EtAnzLager} - {et.EtBezeichnung}')  # Ausgabe der Daten
            liste_et.append(int(et.EtID))                     # Anhängen der Ersatzteilnummer an die Liste
        print()

       