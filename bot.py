import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from main import checkGasBalancesTest


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=checkGasBalancesTest())

if __name__ == '__main__':
    application = ApplicationBuilder().token('6238485166:AAHY3jVaTFFi4uBa5j5ZD58IyGygsYkeD44').build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    gasBalance_handler = CommandHandler('balance', balance)
    application.add_handler(gasBalance_handler)
    
    application.run_polling()