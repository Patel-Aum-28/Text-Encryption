from flask import Flask, render_template, request
from cryptography.fernet import Fernet

app = Flask(__name__)

key = Fernet.generate_key()
cipher_suite = Fernet(key)

@app.route("/")
def home():
    return render_template("index.html", result="")

@app.route("/encrypt", methods=["POST"])
def encrypt():
    if request.method == "POST":
        data = request.form["data"].encode("utf-8")
        encrypted_data = cipher_suite.encrypt(data)
        return encrypted_data.decode("utf-8")
    return ""

@app.route("/decrypt", methods=["POST"])
def decrypt():
    if request.method == "POST":
        data = request.form["data"].encode("utf-8")
        decrypted_data = cipher_suite.decrypt(data)
        return decrypted_data.decode("utf-8")
    return ""

if __name__ == "__main__":
    app.run(debug=False)
