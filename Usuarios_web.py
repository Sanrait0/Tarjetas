from flask import Flask, redirect, url_for, render_template
from Genera_usuarios import Genera_usuarios
import random

from paquete.Usuario import usuario

app = Flask(__name__)

@app.route("/")
def home():
    users = [app.config['Users'][k].get_name() for k in app.config['Users']]
    return render_template("index.html", content=users)

@app.route("/<name>")
def user(name):
    if name in app.config['Users']:
        string = f"¡Bienvenid@ {name}!"
        values = app.config['Users'][name].__str__(False)
        reporte = "Reporte general de usuario: "
    else:
        string = f"El usuario {name} no está registrado."
        values = []
        reporte = ""
    return render_template("usuario.html", usuario=string, values=values, reporte=reporte)

@app.route("/<name>/<card>")
def tarjeta(name, card):
    if name in app.config['Users']:
        Lcards = [c.get_card_name() for c in app.config['Users'][name].get_cards()]  # Tarjetas del usuario
        if card in Lcards:
            str_card = f"Tarjeta localizada ({card})."
            idx = Lcards.index(card)
            tCredito =  app.config['Users'][name].get_cards()[idx]  # Seleccionando tarjeta correcta.
            values = tCredito.generar_reporte(False)
            reporte = "Reporte: "
        else:
            str_card = f"La tarjeta del banco {card} no fue localizada para el usuario {name}."
            values = []
            reporte = ""
    else:
        str_card = f"El usuario {name} no está registrado."
        values = []
        reporte = ""
    return render_template("tarjeta.html", usuario=str_card, values=values, reporte=reporte)

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

if __name__ == "__main__":
    n_user = random.randint(1, 8)  # Número aleatorio de usuarios
    app.config['Users'] = Genera_usuarios(n_user)
    app.run()