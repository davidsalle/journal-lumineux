"""
Simulateur de journal lumineux ou écran d'accueil
Gestion des paramètres de l'écran
18/10/2024
"""

# Librarie(s) utilisée(s)
import re


class ScreenError(Exception):
    """Matérialise une erreur d'utilisation avec l'écran"""
    
    def __init__(self, message):
        """Initialise l'erreur"""
        self.message = message
        super().__init__(self.message)


class Screen:
    """Représente l'écran et ses paramètres"""

    def __init__(self, message, color, speed, size):
        """Initialise l'écran avec ses paramètres"""
        self.message = message
        self.color = color
        self.speed = speed
        self.size = size

    def get_message(self) -> str:
        return self.message
    
    def get_color(self) -> tuple:
        return self.color

    def get_speed(self) -> int:
        return self.speed    
    
    def get_size(self) -> int:        
        return self.size

         
    def set_message(self, new_message: str) -> None:
        """Modifie le message affiché par l'écran
         
        Liste des contraintes générant une erreur
        - longueur maximum = 50 caractères
        - uniquement des chiffres et des lettres (minuscules ou majuscules)
        """
        #print( re.search(r"[^ \w+]", new_message) )
        if len(new_message) > 50:
            raise ScreenError("Message is too long")
        elif re.search(r"[^ \w+]", new_message) is not None:
            raise ScreenError("Message must contains only numbers and letters")
        else:
            self.message = new_message
    
    def set_color(self, new_color):
        self.color = new_color

    def set_speed(self, new_speed):
        self.speed = new_speed

    def set_size(self, new_size):
        self.size = new_size


if __name__ == "__main__":
    # Tests unitaires
    s1 = Screen("...", (255, 0, 0), 10, 1)

    s1.set_message("Hello world")
    #s1.set_message("sdddddddddddddddddddddddddddddddddddddddtggggggggggggggggggggggggggggst")
    #s1.set_message("<script></script>")