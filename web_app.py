import os
from flask import Flask
import psycopg2

app = Flask(__name__)

DATABASE_URL = os.environ['DATABASE_URL']
print("URL del database:", DATABASE_URL)  

@app.route('/')
def hello():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        print("Connesso al database")  # Feedback dopo una connessione riuscita
        
        cursor = conn.cursor()
        cursor.execute("SELECT nome FROM nomi LIMIT 1;")
        name = cursor.fetchone()[0]
        print(f"Nome recuperato: {name}")  # Feedback dopo aver recuperato un nome dal database
        
        conn.close()
    except Exception as e:
        print("Errore durante la connessione o l'interrogazione del database:", str(e))  # Stampa errori se si verificano

    return f"Hello, {name}!"

if __name__ == "__main__":
    print("Avvio dell'applicazione Flask")  # Feedback all'avvio dell'applicazione
    app.run(debug=True, host='0.0.0.0')