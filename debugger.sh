# Archivo para ejecutar con shell
# Ejecuta el modo debugger de app
# Hay que ir a la url 127.0.0.1:5000
cd ~/public_html
source si1pyenv/bin/activate
PYTHONPATH=. python -m app
# para que funcione el siguiente comando, agregar ampersand en el anterior
# firefox 127.0.0.1:5000
