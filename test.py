from flask import Flask, request
from telegram import Update, Bot

app = Flask(__name__)
bot_token = '6540700565:AAFmBjE3LXyZlx4USqc5xfD8MP5OD4z5-Qs'
bot = Bot(token=bot_token)

@app.route('/refresh', methods=['POST'])
def refresh():
    # Tambahkan logika pembaruan halaman web di sini
    # Misalnya, Anda dapat menggunakan JavaScript untuk merefresh halaman.

    return "Halaman web diperbarui!"

@app.route(f'/{bot_token}', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(), bot)
    
    if update.message.text == "/refresh":
        # Tanggapi perintah /refresh dengan mengirim pesan yang sesuai ke bot Telegram.
        bot.send_message(chat_id=update.message.chat_id, text="Merefresh halaman web...")
    
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
