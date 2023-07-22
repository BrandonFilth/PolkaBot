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

## Librerías necesarias

El bot utiliza las siguientes librerías de Python:

- `telebot`: Esta librería se utiliza para interactuar con la API de Telegram y es necesaria para crear y manejar el bot de Telegram.

- `requests`: Se utiliza para realizar solicitudes HTTP a las APIs de Subscan y obtener la información necesaria.

## Instalación de las librerías

Para instalar las librerías necesarias, puedes utilizar `pip`, el gestor de paquetes de Python. Ejecuta los siguientes comandos en tu terminal o línea de comandos:

```bash
pip install pyTelegramBotAPI
pip install requests
```
## Requisitos del bot de Telegram

Para utilizar el bot de Telegram, debes asegurarte de tener lo siguiente:

- **Una cuenta de Telegram**: Debes tener una cuenta de Telegram para crear y administrar el bot.

- **Token del bot**: Debes obtener el token de tu bot de Telegram al crearlo en el BotFather de Telegram.

## Licencias

Este proyecto utiliza licencias de código abierto. A continuación, se muestran las licencias de las librerías utilizadas:

- `pyTelegramBotAPI`: Licencia MIT. Puedes encontrar más información en [https://github.com/eternnoir/pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI).

- `requests`: Licencia Apache 2.0. Puedes encontrar más información en [https://github.com/psf/requests](https://github.com/psf/requests).

## Código fuente

El bot fue desarrollado utilizando las librerías mencionadas y los siguientes archivos contienen el código fuente del bot:

1. `main.py`: Contiene la configuración principal del bot y la lógica para manejar los comandos `/get_balance`, `/get_price` y `/token_info`.

2. `balance.py`: Contiene la lógica para obtener y formatear el saldo de una dirección en las redes Polkadot y Kusama.

3. `price.py`: Contiene la lógica para obtener y mostrar el precio actual de las criptomonedas en las redes Polkadot y Kusama.

4. `token_info.py`: Contiene la lógica para obtener y mostrar información detallada sobre el token DOT en la red Polkadot.

## Agradecimientos

Agradecemos a la comunidad de desarrolladores de Polkadot y Kusama, así como a Subscan por proporcionar las APIs necesarias para obtener la información utilizada en este bot.

¡Esperamos que encuentres útil este bot y que te ayude a estar informado sobre las criptomonedas en las redes Polkadot y Kusama!
