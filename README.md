# To-Do List CLI

<img width="209" height="123" alt="image" src="https://github.com/user-attachments/assets/4d6b1de5-d2d6-4464-9a46-862145b529bb" />

Un semplice programma **CLI (Command Line Interface)** scritto in Python per gestire una lista di attività direttamente dal terminale.

A differenza della prima versione, questa versione salva automaticamente le attività in un file **JSON**, permettendo di ritrovarle anche dopo aver chiuso e riaperto il programma.

## Come usare

1. Apri il terminale o il tuo ambiente di sviluppo Python.
2. Esegui il file `to_do_list.py`.
3. Scegli un'opzione dal menu:

   - `1` – Aggiungi una nuova attività
   - `2` – Mostra tutte le attività
   - `3` – Completa un'attività
   - `4` – Chiudi il programma

4. Segui le istruzioni mostrate nel terminale.

Le attività vengono salvate automaticamente nel file `attivita.json`.

## Funzionalità principali

- Aggiunta di nuove attività.
- Visualizzazione delle attività presenti, numerate.
- Completamento e rimozione delle attività.
- Salvataggio automatico delle attività.
- Caricamento delle attività all'avvio del programma.
- Persistenza dei dati tramite file JSON.
- Controllo delle opzioni inserite nel menu.
- Possibilità di chiudere il programma direttamente dal menu.

## Salvataggio dei dati

Il programma utilizza il file:

`attivita.json`

All'avvio, il programma controlla se il file esiste:

- Se esiste, le attività vengono caricate.
- Se non esiste, viene creata una lista vuota.

Quando viene aggiunta o completata un'attività, il file JSON viene aggiornato automaticamente.

## Tecnologie utilizzate

- **Python 3**
- `json` – per salvare e caricare le attività.
- `os` – per verificare l'esistenza del file.
- `while` – per mantenere attivo il menu del programma.
- Liste Python – per gestire le attività.

## Requisiti

- Python 3.x
- Nessuna libreria esterna richiesta.
- Utilizza esclusivamente la libreria standard di Python.

## Possibili miglioramenti futuri

- [ ] Gestire input non numerici durante la scelta dell'attività.
- [ ] Aggiungere la possibilità di modificare un'attività.
- [ ] Aggiungere una funzione per eliminare un'attività senza completarla.
- [ ] Permettere di contrassegnare un'attività come completata senza rimuoverla.
- [ ] Separare il codice in più funzioni per rendere il programma più organizzato
