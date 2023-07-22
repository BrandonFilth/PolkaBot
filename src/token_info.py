import requests

def handle_get_token_info(message, bot, api_key, images, format_balance):
    # URL de la API para obtener la información del token
    api_url = 'https://polkadot.api.subscan.io/api/scan/token'
    symbol = 'DOT'
    # Encabezados de la solicitud HTTP con el tipo de contenido y la clave de la API
    headers = {
        'Content-Type': 'application/json',
        'X-API-Key': api_key
    }
    try:
        # Datos a enviar en la solicitud HTTP (solo se necesita el símbolo del token)
        data = {
            'token': [symbol]
        }
        # Realizar la solicitud HTTP POST a la API
        response = requests.post(api_url, headers=headers, json=data)
        # Verificar si hubo errores en la solicitud
        response.raise_for_status()
        # Convertir la respuesta JSON en un objeto Python
        data = response.json()
        # Comprobar si la solicitud fue exitosa y si contiene los datos del token
        if 'code' in data and data['code'] == 0 and 'data' in data and 'detail' in data['data']:
            tokens_detail = data['data']['detail']
            # Verificar si el símbolo del token existe en la respuesta y mostrar su información
            if symbol in tokens_detail:
                token_detail = tokens_detail[symbol]
                # Crear el mensaje de Telegram con la información del token
                message_text = f'💠 Symbol: {token_detail["symbol"]}\n'
                message_text += f'📝 Display Name: {token_detail["display_name"]}\n'
                message_text += f'🔢 Token Decimals: {token_detail["token_decimals"]}\n'
                message_text += f'💲 Total Issuance: {format_balance(token_detail["total_issuance"], token_detail["token_decimals"])}\n'
                message_text += f'💵 Price: {token_detail["price"]}\n'
                message_text += f'📈 Price Change: {token_detail["price_change"]}\n'
                message_text += f'💰 Free Balance: {format_balance(token_detail["free_balance"], token_detail["token_decimals"])}\n'
                message_text += f'💳 Available Balance: {format_balance(token_detail["available_balance"], token_detail["token_decimals"])}\n'
                message_text += f'🔒 Validator Bonded: {format_balance(token_detail["validator_bonded"], token_detail["token_decimals"])}\n'
                message_text += f'🤝 Nominator Bonded: {format_balance(token_detail["nominator_bonded"], token_detail["token_decimals"])}\n'
                message_text += f'🔒 Locked Balance: {format_balance(token_detail["locked_balance"], token_detail["token_decimals"])}\n'
                message_text += f'🔒 Bonded Locked Balance: {format_balance(token_detail["bonded_locked_balance"], token_detail["token_decimals"])}\n'
                message_text += f'🔒 Unbonded Locked Balance: {format_balance(token_detail["unbonded_locked_balance"], token_detail["token_decimals"])}\n'
                message_text += f'🗳️ Democracy Locked Balance: {format_balance(token_detail["democracy_locked_balance"], token_detail["token_decimals"])}\n'
                message_text += f'💼 Reserved Balance: {format_balance(token_detail["reserved_balance"], token_detail["token_decimals"])}\n'
                message_text += f'📅 Election Locked Balance: {format_balance(token_detail["election_locked_balance"], token_detail["token_decimals"])}\n'
                message_text += f'💼 Vesting Balance: {format_balance(token_detail["vesting_balance"], token_detail["token_decimals"])}\n'
                message_text += f'💹 Inflation: {token_detail["inflation"]}\n'

                # Abrir la imagen del token correspondiente y enviar el mensaje de Telegram
                with open('img/polkadot.jpg', 'rb') as photo:
                    bot.send_photo(message.chat.id, photo)
                    bot.send_message(message.chat.id, message_text, parse_mode='Markdown')
            else:
                # Si el símbolo del token no está en la respuesta, mostrar un mensaje de error
                bot.send_message(message.chat.id, f'❌ No se encontró el token con el símbolo {symbol}')
        else:
            # Si la solicitud no fue exitosa, mostrar un mensaje de error
            bot.send_message(message.chat.id, '❌ Error al obtener la información del token')
    except requests.exceptions.RequestException:
        # Si ocurre un error en la solicitud, mostrar un mensaje de error
        bot.send_message(message.chat.id, '❌ Error al conectarse a la API')

# Luego en el archivo main.py, debes importar la función get_token_info y llamarla en la parte donde procesas el comando "/token_info"
