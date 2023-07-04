#Importamos los módulos requests y telebot, que se utilizarán para realizar solicitudes HTTP y para interactuar con la API de Telegram, respectivamente.
import requests
import telebot
#Definimos el token del bot de Telegram y creamos una instancia de TeleBot con ese token.
bot_token = 'TU_BOT_TOKEN'
bot = telebot.TeleBot(bot_token)

#Creamos un diccionario llamado endpoints que contiene los nombres de los endpoints de API para Polkadot y Kusama.
endpoints = {
    'Polkadot': 'polkadot.api.subscan.io',
    'Kusama': 'kusama.api.subscan.io',
}
#Creamos un conjunto llamado images que contiene los nombres de las imágenes de Polkadot y Kusama.
images = {
    'polkadot.jpg',
    'kusama.jpg',
    
    
}
# Reemplaza esto con tu clave de API
api_key = 'TU_API_KEY'  

# Definimos una función llamada format_balance que toma un saldo y un número de decimales, y formatea el saldo 
# dividiéndolo por 10 elevado a la potencia de los decimales. Luego, se devuelve el saldo formateado con dos decimales.
def format_balance(balance, decimals):
    formatted_balance = float(balance) / 10 ** decimals
    return '{:,.2f}'.format(formatted_balance)


# creamos el Comando /get_balance
@bot.message_handler(commands=['get_balance'])
def handle_get_balance(message):
    image = 0
    # Obtener los parámetros después del comando /get_balance "dirección"
    command = message.text.split()
    #Verificamos si el usuario proporciono una billetera 
    if len(command) > 1:
        #si el usuario ingreso una billetera se guarda en la segunda posicion del
        #command ya que la posicion0 estaria ocupada por el comando 
        address = command[1]
        # Iterar sobre las imágenes y endpoints al mismo tiempo usando la funcion zip para crear una secuencia de tuplas
        #y asi incrementar el indice en cada iteracion
        for image, (chain, endpoint) in zip(images, endpoints.items()):
            # Inicializar una cadena vacía para almacenar el texto del saldo
            balance_text = ''
            # Construir la URL de la API para obtener los tokens de la cuenta
            api_url = f'https://{endpoint}/api/scan/account/tokens'
            # Construir la URL del explorador de bloques para mostrar enlaces a la cuenta
            explorer_url = f'https://{endpoint.replace("api.", "")}/account/{address}'
            # Configurar los encabezados de la solicitud HTTP con el tipo de contenido y la clave de la API
            headers = {
                'Content-Type': 'application/json',
                'X-API-Key': api_key
            }
            try:
                # Realizar una solicitud POST a la API para obtener los tokens de la cuenta
                response = requests.post(api_url, headers=headers, json={'address': address})
                # Verificar si hubo errores en la solicitud
                response.raise_for_status()
                 # Convertir la respuesta JSON en un objeto Python
                data = response.json()
                #comprueba si el diccionario data contiene las claves 'data' y 'native'. Si ambas claves están presentes, la condición será verdadera 
                if 'data' in data and 'native' in data['data']:
                    #guardamos los valores encontrados dentro de data y native
                    balances = data['data']['native']
                    #iteramos los items encontrados y almacenados en balance
                    #ademas de eso los guardamos en una variable y les damos formato con la funcion anterior
                    for balance in balances:
                        symbol = balance['symbol']
                        balance_value = format_balance(balance['balance'], balance['decimals'])
                        lock_value = format_balance(balance['lock'], balance['decimals'])
                        reserved_value = format_balance(balance['reserved'], balance['decimals'])
                        bonded_value = format_balance(balance['bonded'], balance['decimals'])
                        unbonding_value = format_balance(balance['unbonding'], balance['decimals'])
                        democracy_lock_value = format_balance(balance['democracy_lock'], balance['decimals'])
                        election_lock_value = format_balance(balance['election_lock'], balance['decimals'])

                        #concatenamos los resultados en un solo mensaje y el cual sera mostrado mas adelante entonces esto es una funcion que se encarga de mostrar los valores 
                        balance_text += f'💰Symbol: {symbol}\n'
                        balance_text += f'💵Balance: {balance_value} {symbol}\n'
                        balance_text += f'🔒Lock: {lock_value}\n'
                        balance_text += f'🔐Reserved: {reserved_value}\n'
                        balance_text += f'🔒Bonded: {bonded_value}\n'
                        balance_text += f'⏳Unbonding: {unbonding_value}\n'
                        balance_text += f'🗳Democracy Lock: {democracy_lock_value}\n'
                        balance_text += f'📩Election Lock: {election_lock_value}\n'
                        balance_text += f'[View on {chain} Explorer]({explorer_url})\n'

                #en caso de que no haya encontrado los apartados data y native dentro de el diccionario 
                else:
                    #indicamos en cual de las redes fue el error y de igual manera concatenamos el mensaje
                    balance_text += f'🌐Chain: {chain}\n'
                    balance_text += f'❌Error: No se pudo obtener el saldo\n'
                    balance_text += f'[View on {chain} Explorer]({explorer_url})\n'

                # abrimos la imagen en modo de lectura binaria 
                with open(image, 'rb') as photo:
                    #enviamos el mensaje con la foto
                    bot.send_photo(message.chat.id, photo)
                    #enviamos un mensaje con el texto y lo parseamos a markdown para poder hacer un hipervinculo 
                    bot.send_message(message.chat.id, balance_text, parse_mode='Markdown')

            #En caso de que la solicitud haya concluido sin exito mostramos en que red ha pasado el error
            except requests.exceptions.RequestException:
                balance_text += f'🌐Chain: {chain}\n'
                balance_text += f'❌Error: Ocurrió un error al realizar la solicitud\n'
                balance_text += f'[View on {chain} Explorer]({explorer_url})\n'

                # Enviamos la imagen y el mensaje al indicar en cual red ocurrio el error
                with open(image, 'rb') as photo:
                    bot.send_photo(message.chat.id, photo)
                    bot.send_message(message.chat.id, balance_text, parse_mode='Markdown')
    #en caso de que el usuario no añada un argumento 
    else:
        bot.reply_to(message, "Agrega la dirección de la billetera. Ejemplo: /get_balance 1qnJN7FViy3HZaxZK9tGAA71zxHSBeUweirKqCaox4t8GT7")

# Ejecutar el bot
bot.polling()