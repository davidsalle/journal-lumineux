"""
Simulateur de journal lumineux ou écran d'accueil
Gestion des paramètres de l'écran
18/10/2024
"""

class Screen:
    """Représente l'écran et ses paramètres"""

    def __init__(self, message, color, speed, size):
        """Initialise l'écran avec ses paramètres"""
        self.message = message
        self.color = color
        self.speed = speed
        self.size = size

    def get_message(self):
        return self.message
    
    def get_color(self):
        return self.color
    
    def get_speed(self):
        return self.speed
    
    def get_size(self):
        return self.size
         
    def set_message(self, new_message):
        self.message = new_message    
    
    def set_color(self, new_color):
        self.color = new_color

    def set_speed(self, new_speed):
        self.speed = new_speed

    def set_size(self, new_size):
        self.size = new_size