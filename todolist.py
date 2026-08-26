import json
import os

FILE_DATI = "attivita.json"

if os.path.exists(FILE_DATI):
    with open(FILE_DATI, "r", encoding="utf-8") as f:
        attivita = json.load(f)
else:
    attivita = []
    

while True:
    print("\n---TO DO LIST---")
    print("1 - Aggiungi attività")
    print("2 - Mostra attività")
    print("3 - Completa attività")
    print("4 - Chiudi il programma")

    i = 0
    scelta = input("Scegli un'opzione: ")

    while scelta not in ("1", "2", "3", "4"):
        print("ATTENZIONE! Inserisci un numero collegato ad un'istruzione")
        scelta = input("Scegli un'opzione: ")

    if scelta == "1":
        nuova_attivita = input("Inserisci la nuova attività: ")
        attivita.append(nuova_attivita)
        with open(FILE_DATI, "w", encoding="utf-8") as f:
            json.dump(attivita, f, ensure_ascii=False, indent=4)
        print("Attivita aggiunta")

    elif scelta == "2":
        if len(attivita) == 0:
            print("Nessuna attività")
        else:
            while i < len(attivita):
                print(str(i+1) + " " + attivita[i])
                i = i + 1
                

    elif scelta == "3":
        if len(attivita) == 0:
            print("Niente da completare.")
        else:
            numero = int(input("Numero attività da completare: "))
            if 1 <= numero <= len(attivita):
                completata = attivita.pop(numero - 1)
                with open(FILE_DATI, "w", encoding="utf-8") as f:
                    json.dump(attivita, f, ensure_ascii=False, indent=4)
                print(f"Hai completato: {completata}")
            else:
                print("Numero non valido.")

    elif scelta == "4":
        exit()
