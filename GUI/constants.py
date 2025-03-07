import os
from kivy.config import Config

width, height = 1920, 1080

Config.set('graphics','width',width)
Config.set('graphics','height',height)
Config.set('graphics','fullscreen','False')


# Aquí se deben definir las claves de API necesarias para la aplicación.
# Asegúrate de que estas claves estén en el archivo .env.

EMAIL = os.environ.get("EMAIL")  # Correo electrónico para el envío de correos
PASSWORD = os.environ.get("PASSWORD")  # Contraseña para el correo electrónico

IP_ADDR_API_URL = os.environ.get("IP_ADDR_API_URL")  # URL para obtener la dirección IP
NEWS_FETCH_API_URL = os.environ.get("NEWS_FETCH_API_URL")  # URL para obtener noticias
NEWS_FETCH_API_KEY = os.environ.get("NEWS_FETCH_API_KEY")  # Clave de API para el servicio de noticias
WEATHER_FORECAST_API_URL = os.environ.get("WEATHER_FORECAST_API_URL")  # URL para el pronóstico del tiempo
WEATHER_FORECAST_API_KEY = os.environ.get("WEATHER_FORECAST_API_KEY")  # Clave de API para el servicio de pronóstico del tiempo
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")  # Clave de API para el servicio Gemini



SMTP_URL = os.environ.get("SMTP_URL")
SMTP_PORT = os.environ.get("SMTP_PORT")

SCREEN_WIDTH = Config.getint('graphics','width')
SCREEN_HEIGHT = Config.getint('graphics','height')

random_text = [
    "Estoy aquí para ayudarte.",
    "¿En qué puedo asistirte hoy?",
    "Siempre listo para ayudar.",
    "¿Qué necesitas, amigo?",
    "Estoy a tu servicio."
]
