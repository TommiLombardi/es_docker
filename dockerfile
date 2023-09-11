FROM python:3.9

WORKDIR /app

# Copia le dipendenze e installale 
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copia tutto il contenuto della directory corrente nel container
COPY . .

# Usa CMD per eseguire web_app.py quando il container viene avviato
CMD [ "flask","--app", "./src/web_app" , "run", "--host=0.0.0.0"]

