# Polkabot

Polkabot es un bot de Telegram que proporciona información sobre saldos de criptomonedas en las redes Polkadot y Kusama. Puedes interactuar con el bot para obtener el saldo de una dirección, el precio actual de las criptomonedas y la información detallada de un token específico.

## Configuración

Antes de usar el bot, asegúrate de configurar los siguientes parámetros:

1. **Token del bot de Telegram**: Reemplaza `TU_BOT_TOKEN` con el token de tu propio bot de Telegram. Si aún no tienes un bot, puedes crear uno siguiendo las instrucciones en la documentación de Telegram.

2. **Clave API de Subscan**: Reemplaza `TU_API_KEY` con tu propia clave de API de Subscan. Puedes obtener una clave API registrándote en el sitio web de Subscan.

## Comandos

El bot admite los siguientes comandos:

1. `/get_balance dirección`: Obtiene el saldo de una dirección en las redes Polkadot y Kusama.

2. `/get_price`: Obtiene el precio actual de las criptomonedas en las redes Polkadot y Kusama.

3. `/token_info`: Obtiene información detallada sobre el token DOT en la red Polkadot.

## Cómo usar

1. Abre Telegram y busca el nombre de tu bot para iniciar una conversación con él.

2. Usa los comandos mencionados anteriormente para obtener la información que necesitas.

3. El bot te mostrará el saldo, el precio y la información detallada del token según el comando utilizado.

## Código fuente

El bot fue desarrollado utilizando el módulo `telebot` para interactuar con la API de Telegram. Los siguientes archivos contienen el código fuente del bot:

1. `main.py`: Contiene la configuración principal del bot y la lógica para manejar los comandos `/get_balance`, `/get_price` y `/token_info`.

2. `balance.py`: Contiene la lógica para obtener y formatear el saldo de una dirección en las redes Polkadot y Kusama.

3. `price.py`: Contiene la lógica para obtener y mostrar el precio actual de las criptomonedas en las redes Polkadot y Kusama.

4. `token_info.py`: Contiene la lógica para obtener y mostrar información detallada sobre el token DOT en la red Polkadot.

## Agradecimientos

Agradecemos a la comunidad de desarrolladores de Polkadot y Kusama, así como a Subscan por proporcionar las APIs necesarias para obtener la información utilizada en este bot.

¡Esperamos que encuentres útil este bot y que te ayude a estar informado sobre las criptomonedas en las redes Polkadot y Kusama!
