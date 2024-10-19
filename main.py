"""
Simulateur de journal lumineux ou écran d'accueil
Application web
18/10/2024
"""

# Librairie(s) utilisée(s)
from flask import Flask, request, render_template, jsonify
from screen import Screen

   		

# Création des objets de l'application
app = Flask(__name__)
screen = Screen("Here your scrolling message...", "#000000", 10, 1)

# Définitions des routes
@app.route("/")
@app.route("/index")
def index():
    return render_template(
        "accueil.html",
        base_url=request.base_url
    )

@app.route("/api/get-state")
def get_state():
    reponse = {
        "message": screen.get_message(),
        "color": screen.get_color(),
        "speed": screen.get_speed()
    }
    return jsonify(reponse)

@app.route("/api/set-message", methods=["POST"])
def set_message_from_api():
    pass


# Lancement
if __name__ == "__main__":
	app.run("0.0.0.0", debug=True)