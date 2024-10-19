"""
Simulateur de journal lumineux ou écran d'accueil
Application web
18/10/2024

curl -X POST https://reqbin.com/echo/post/json
  -H 'Content-Type: application/json'
  -d '{"login":"my_login","password":"my_password"}'
"""

# Librairie(s) utilisée(s)
from flask import Flask, request, render_template, jsonify
from screen import Screen, ScreenError
   		

# Création des objets de l'application
app = Flask(__name__)
screen = Screen("Here is your scrolling message...", "#000000", 10, 1)


# Définitions des routes
@app.route("/")
@app.route("/index")
def index():
    return render_template(
        "accueil.html",
        base_url=request.base_url
    )

@app.route("/api/json/get-state")
def get_state():
    reponse = {
        "status": "OK",
        "message": screen.get_message(),
        "color": screen.get_color(),
        "speed": screen.get_speed()
    }
    return jsonify(reponse)

@app.route("/api/json/set-message", methods=["POST", "GET"])
def set_message_from_api():
    """Gère le changement de message
    
    curl -X POST http://127.0.0.1:5000/api/set-message \
    -H 'Content-Type: application/json' \
    -d '{"message":"Hello world les amis"}'
    """
    if request.method == "POST":
        # Récupération des données JSON
        donnees = request.json
        nouveau_message = donnees.get("message")

        if nouveau_message is not None:
            try:
                screen.set_message(nouveau_message)
                reponse = {
                    "status": "OK",
                    "error": "...",
                }
                return jsonify(reponse)
            except ScreenError as erreur:
                reponse = {
                    "status": "NOK",
                    "error": erreur.message,
                }
                return jsonify(reponse)
        else:
            reponse = {
                "status": "NOK",
                "error": "Cannot find message in JSON",
            }
            return jsonify(reponse)
    else:
        reponse = {
            "status": "NOK",
            "error": "Only POST method is allowed",
        }
        return jsonify(reponse)
    

        


# Lancement
if __name__ == "__main__":
	app.run("0.0.0.0", debug=True)