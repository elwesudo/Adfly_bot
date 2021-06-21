echo "Instalando paquetes"
pkg install python3 tor -y
pip3 install tbselenium
echo 'Abra otra ventana y ejecute "tor"'
python3 Adfly_bot.py
