from dbConnect import sessionLoader
from mapper import Montage, Auftrag, Ersatzteil
from checker import handleInputInteger


def getErsatzteilFromAuftrag(p_aufnr):
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

    if len(auftrag.ListeMontage) > 0:
        # Definition der Liste für die Ersatzteilnummern aus dem Auftrag,  1. Element 0
        liste_mon = [0]    
        for mon in auftrag.ListeMontage:
            print(f' {mon.EtID} - {mon.Anzahl} - {mon.Ersatzteil.EtBezeichnung}')  # Ausgabe der Daten
            liste_mon.append(int(mon.Anzahl))                     # Anhängen der Ersatzteilnummer an die Liste
        print()

    else:
        print('Es gibt keine Ersatzteile für den Auftrag.')
        session.close()
        return 0
    session.close()
