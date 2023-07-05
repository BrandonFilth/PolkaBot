# Bot de Telegram para consultar saldos de Polkadot y Kusama

Este bot de Telegram te permite consultar los saldos de las criptomonedas Polkadot (DOT) y Kusama (KSM) en tiempo real.

## Configuración

Antes de utilizar el bot, asegúrate de seguir estos pasos de configuración:

1. Obtén un token para tu bot de Telegram siguiendo la guía oficial de Telegram.

2. Reemplaza `TU_BOT_TOKEN` en el código con el token que obtuviste en el paso anterior.

3. Registra una clave de API en el sitio web de Subscan y reemplaza `TU_API_KEY` en el código con tu clave de API.

4. Asegúrate de tener instaladas las dependencias necesarias ejecutando `pip install requests telebot`.

## Uso

1. Inicia el bot y agrégalo a un grupo o chatea directamente con él.

2. Usa el comando `/get_balance` seguido de una dirección de billetera para obtener el saldo. Por ejemplo: `/get_balance 1qnJN7FViy3HZaxZK9tGAA71zxHSBeUweirKqCaox4t8GT7`.

3. El bot buscará el saldo en las redes Polkadot y Kusama y te mostrará los detalles del saldo, incluyendo el símbolo, balance, bloqueo, reservas y más.

4. También se mostrará una imagen correspondiente a cada red junto con los resultados del saldo.

¡Disfruta de la consulta de saldos con el bot de Telegram!

## Contribuciones

Si deseas contribuir a este proyecto, siéntete libre de hacer un pull request.

## Licencia

Este proyecto se distribuye bajo la licencia MIT. Consulta el archivo `LICENSE` para obtener más información.

