"""
Simulateur de journal lumineux ou écran d'accueil
"""

# Librairie(s) utilisée(s)
from flask import Flask, request, render_template, jsonify


# Création de l'application
app = Flask(__name__)

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
		"message": "Hello world !!!!",
		"color": "#ff0000",
		"speed": "10s"
	}
	return jsonify(reponse)


# Lancement
if __name__ == "__main__":
	app.run("0.0.0.0", debug=True)