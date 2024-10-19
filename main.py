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
    """Affiche l'écran d'information"""
    return render_template(
        "accueil.html",
        base_url=request.base_url
    )


@app.route("/api/json/get-screen", methods=["POST", "GET"])
def get_state():
    """Retourne les paramètres actuellement utilisés par l'écran"""
    if request.method == "GET":
        reponse = {
            "status": "OK",
            "message": screen.get_message(),
            "color": screen.get_color(),
            "speed": screen.get_speed()
        }
        return jsonify(reponse)
    else:
        reponse = {
            "status": "NOK",
            "error": "Only GET method is allowed",
        }
        return jsonify(reponse)


@app.route("/api/json/set-screen", methods=["POST", "GET"])
def set_message_from_api():
    """Gère le changement de message
    
    curl -X POST http://127.0.0.1:5000/api/json/set-screen \
    -H 'Content-Type: application/json' \
    -d '{"message":"Hello", "color":"#00ff00", "speed":10}'
    """
    if request.method == "POST":
        # Récupération des données JSON
        data = request.json
        new_message = data.get("message")
        new_color = data.get("color")
        new_speed = data.get("speed")

        if new_message is not None and new_color is not None and new_speed is not None:
            try:
                # Modification des caractéristiques du message
                screen.set_message(new_message)
                screen.set_color(new_color)
                screen.set_speed(new_speed)
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
                "error": "JSON format error, a field is missing",
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