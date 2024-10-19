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
    
    def get_color(self) -> str:
        return self.color

    def get_speed(self) -> int:
        return self.speed    
    
    def get_size(self) -> int:        
        return self.size

         
    def set_message(self, new_message: str) -> None:
        """Modifie le message affiché par l'écran"""
        #print( re.search(r"[^ \w+]", new_message) )
        if isinstance(new_message, str) == False:
            raise ScreenError("Message is not a string")
        elif len(new_message) > 50:
            raise ScreenError("Message is too long")
        elif re.search(r"[^ \w+]", new_message) is not None:
            raise ScreenError("Message must contains only numbers and letters")
        else:
            self.message = new_message
    
    def set_color(self, new_color: str) -> None:
        """Modifie la couleur du message affiché"""        
        if isinstance(new_color, str) == False:
            raise ScreenError("Color is not a string")
        elif re.match(r"^#([0-9a-fA-F]{6})$", new_color) is None:
            raise ScreenError("Color must follow the HTML color format")        
        else:            
            self.color = new_color

    def set_speed(self, new_speed: int) -> None:
        """Modifie la durée d'affichage du message"""
        if isinstance(new_speed, int) == False:
            raise ScreenError("Speed is not an integer")
        elif new_speed < 5 or new_speed > 20:
            raise ScreenError("Speed must be between 5s and 20s")        
        else:            
            self.speed = new_speed

    def set_size(self, new_size):
        self.size = new_size


if __name__ == "__main__":
    # Tests unitaires
    s1 = Screen("...", "#ff0000", 10, 1)

    #s1.set_message("Hello world")
    #s1.set_message("sdddddddddddddddddddddddddddddddddddddddtggggggggggggggggggggggggggggst")
    #s1.set_message("<script></script>")

    s1.set_color("#00000t")