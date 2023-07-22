import requests

def handle_get_price(message, bot, endpoints, api_key, images, format_balance):
    # Inicializamos el texto del mensaje
    price_text = ''

    # Hacemos una solicitud HTTP para obtener el precio y el número del último bloque para cada cadena
    for chain, endpoint in endpoints.items():
        # Construir la URL de la API para obtener el número del último bloque
        api_url = f'https://{endpoint}/api/scan/blocks'
        # Configurar los encabezados de la solicitud HTTP con el tipo de contenido y la clave de la API
        headers = {
            'Content-Type': 'application/json',
            'X-API-Key': api_key
        }
        # Parámetros para la solicitud HTTP
        params = {
            'row': 1,
            'page': 0
        }
        try:
            # Realizar una solicitud POST a la API para obtener el número del último bloque
            response = requests.post(api_url, headers=headers, json=params)
            # Verificar si hubo errores en la solicitud
            response.raise_for_status()
            # Convertir la respuesta JSON en un objeto Python
            data = response.json()
            # Comprobamos si la solicitud fue exitosa y si contiene el número del último bloque
            if 'code' in data and data['code'] == 0 and 'data' in data and 'blocks' in data['data']:
                latest_block_number = data['data']['blocks'][0]['block_num']

                # Construir la URL de la API para obtener el precio
                api_url_price = f'https://{endpoint}/api/open/price'
                # Parámetros para la solicitud HTTP de precio con el número del último bloque
                params_price = {
                    'time': latest_block_number
                }
                # Realizar una solicitud POST a la API para obtener el precio
                response_price = requests.post(api_url_price, headers=headers, json=params_price)
                # Convertir la respuesta JSON en un objeto Python
                data_price = response_price.json()
                # Comprobamos si la solicitud fue exitosa y si contiene el precio
                if 'code' in data_price and data_price['code'] == 0 and 'data' in data_price and 'price' in data_price['data']:
                    price = data_price['data']['price']
                    # Convertimos el precio a un número flotante antes de aplicar el formateo
                    price = float(price)
                    explorer_url = f'https://{endpoint.replace("api.", "")}'
                    # Formateamos el precio para mostrar solo 2 decimales
                    formatted_price = "{:.2f}".format(price)

                    # Concatenamos el precio y el número del último bloque en un solo mensaje
                    message_text = f'Precio: ${formatted_price}\n'
                    message_text += f'Segun el bloque: {format(latest_block_number, ",")}\n'
                    message_text += f'[View on {chain} Explorer]({explorer_url})\n'
                    # Enviamos el mensaje con la imagen y el texto
                    with open(images[chain], 'rb') as photo:
                        bot.send_photo(message.chat.id, photo)
                        bot.send_message(message.chat.id, message_text, parse_mode='Markdown')
                else:
                    # En caso de que no se obtenga el precio, se muestra un mensaje de error
                    price_text += f'{chain}: ❌Error al obtener el precio\n'
            else:
                # En caso de que no se obtenga el número del último bloque, se muestra un mensaje de error
                price_text += f'{chain}: ❌Error al obtener el número del último bloque\n'

        except requests.exceptions.RequestException:
            # En caso de que ocurra un error en la solicitud, se muestra un mensaje de error
            price_text += f'{chain}: ❌Error al obtener el número del último bloque\n'

    return price_text
