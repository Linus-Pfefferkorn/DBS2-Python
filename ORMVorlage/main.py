from checker import handleInputInteger
from logicNiederlassung import getNiederlassung
from logicMitarbeiter import getMitarbeiter
from logicAuftrag import getAuftrag, anlegenAuftrag, planenAuftrag
from logicErsatzteile import getErsatzteile, getErsatzteil2

# Aufruf der Ablauflogik
while True:
    print('')
    print('1 - Daten anzeigen')
    print('2 - Neuen Auftrag anlegen')
    print('3 - Auftrag planen')
    print('4 - Ersatzteile anzeigen')
    wastun = handleInputInteger('Aktion wählen')
    print()
    
    if wastun == 1:
        nlnr = getNiederlassung()            # Niederlassung aus Niederlassungsliste auswählen
        while nlnr > 0:
            print()
            mitnr = getMitarbeiter(nlnr)     # Mitarbeiter aus Mitarbeiterliste auswählen
            while mitnr > 0:
                print()
                getAuftrag(mitnr)            # Aufträge des Mitarbeiters anzeigen
                mitnr = getMitarbeiter(nlnr)
                aufnr = getAuftrag(mitnr)    # Auftrag aus Auftragsliste auswählen
                while aufnr > 0:
                    getErsatzteil2(aufnr)# neuen Mitarbeiter aus Mitarbeiterliste auswählen
            nlnr = getNiederlassung()        # neue Niederlassung aus Niederlassungsliste auswählen

    elif wastun == 2:
        print('Daten einfügen')
        anlegenAuftrag()
        
    elif wastun == 3:
        print('Auftrag planen')
        planenAuftrag()

    elif wastun == 4:
        print('Ersatzteile anzeigen')
        getErsatzteile()    
    
    else:
        break

