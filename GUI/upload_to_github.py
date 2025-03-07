import os
import subprocess

# Configura la URL de tu repositorio de GitHub
REPO_URL = "https://github.com/H4RLEST/Jarvis-AI"  # Reemplaza esto con la URL de tu repositorio


# Inicializa el repositorio si no está inicializado
if not os.path.exists('.git'):
    subprocess.run(["git", "init"])

# Agrega todos los archivos al repositorio
subprocess.run(["git", "add", "."])

# Realiza un commit
subprocess.run(["git", "commit", "-m", "Primer commit de la aplicación Jarvis AI"])

# Conecta el repositorio local con el remoto
subprocess.run(["git", "remote", "add", "origin", REPO_URL])

# Sube el código al repositorio de GitHub
subprocess.run(["git", "push", "-u", "origin", "master"])
