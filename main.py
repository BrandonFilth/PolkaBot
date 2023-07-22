# Importamos el módulo telebot
import telebot
from src import balance
from src import price
from src import token_info


# Definimos el token del bot de Telegram y creamos una instancia de TeleBot con ese token.
bot_token = 'TU_BOT_TOKEN'
bot = telebot.TeleBot(bot_token)

# Creamos los diccionarios con los nombres de los endpoints de API para Polkadot y Kusama.
endpoints = {
    'Polkadot': 'polkadot.api.subscan.io',
    'Kusama': 'kusama.api.subscan.io',
}

# Creamos el diccionario con los nombres de las imágenes de Polkadot y Kusama.
images = {
    'Polkadot': 'img/polkadot.jpg',
    'Kusama': 'img/kusama.jpg',
}
# Reemplaza esto con tu clave API de Subscan
api_key = 'TU_API_KEY'


# Definimos una función llamada format_balance que toma un saldo y un número de decimales, y formatea el saldo 
# dividiéndolo por 10 elevado a la potencia de los decimales. Luego, se devuelve el saldo formateado con dos decimales.
def format_balance(balance, decimals):
    formatted_balance = float(balance) / 10 ** decimals
    return '{:,.2f}'.format(formatted_balance)


# Creamos el Comando /get_balance
@bot.message_handler(commands=['get_balance'])
def handle_get_balance_command(message):
    # Llamamos a la función handle_get_balance
    balance.handle_get_balance(message, bot, endpoints, images, api_key, format_balance)

# Creamos el Comando /get_price
@bot.message_handler(commands=['get_price'])
def handle_get_price_command(message):
    # Llamamos a la función handle_get_price en price.py y pasamos el objeto 'bot' como argumento
    price.handle_get_price(message, bot, endpoints, api_key, images, format_balance)

# Creamos el Comando /get_token
@bot.message_handler(commands=['token_info'])
def handle_get_token_info_command(message):
    token_info.handle_get_token_info(message, bot, api_key, images, format_balance)


# Ejecutar el bot
bot.polling()
