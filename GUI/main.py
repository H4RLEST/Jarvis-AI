from dotenv import load_dotenv
load_dotenv()
from kivy import app, clock
from jarvis import Jarvis

# Cambiar el idioma a español
import locale
locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')


class MykivyApp(app.App):
    def build(self):
        jarvis = Jarvis()  # Inicializar Jarvis sin el argumento de lenguaje


        jarvis.start_listening()
        
        self.update_event = clock.Clock.schedule_interval(jarvis.update_circle,1/60)
        self.btn_rotation_event = clock.Clock.schedule_interval(jarvis.circle.rotate_button,1/60)
        
        return jarvis
    
    
if __name__ == '__main__':
    MykivyApp = MykivyApp()
    MykivyApp.run()
