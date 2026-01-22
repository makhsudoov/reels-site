rom flask import Flask, render_template, redirect, request
from datetime import datetime

app = Flask(__name__)

TELEGRAM_LINK = "https://t.me/xbetzone_ms"

def load_reels():
    with open("data/reels.txt", "r") as f:
        return [line.strip() for line in f if line.strip()]

@app.route("/")
def index():
    reels = load_reels()
    return render_template("index.html", reels=reels)

@app.route("/go")
def go():
    with open("clicks.log", "a") as f:
        f.write(f"{datetime.now()} | {request.remote_addr}\n")
    return redirect(TELEGRAM_LINK)

if __name__ == "__main__":
    app.run()
