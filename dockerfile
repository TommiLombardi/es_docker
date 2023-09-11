FROM python:3.9

WORKDIR /app

# Copia le dipendenze e installale 
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copia tutto il contenuto della directory corrente nel container
COPY . .

# Usa CMD per eseguire web_app.py quando il container viene avviato
# CMD [ "flask","--app", "web_app" , "run"]
CMD ["python", "web_app.py"]
