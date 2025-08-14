from flask import Flask, request
import csv
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/subscribe", methods=["POST"])
def subscribe():
    email = request.form.get("email")
    if email:
        with open("subscribers.csv", "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([email])
        return "Suscripción exitosa", 200
    return "Falta el correo", 400

if __name__ == "__main__":
    app.run(debug=True)
















