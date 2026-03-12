# Image de base Python
FROM python:3.11-slim

# Répertoire de travail
WORKDIR /app

# Copie des fichiers
COPY requirements.txt .
COPY bot.py .

# Installation des dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Lancer le bot
CMD ["python", "bot.py"]