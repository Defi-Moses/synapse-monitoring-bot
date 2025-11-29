import logging
from telegram import Update
from telegram.error import Conflict
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from main import checkGasBalances, checkMiniChefBalances, checkExecutorBalances, checkCirculatingSupply, checkCCTPBalances

# Configure logging - suppress httpx INFO messages to reduce noise
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logging.getLogger('httpx').setLevel(logging.WARNING)
logging.getLogger('telegram').setLevel(logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=checkGasBalances())

async def rewards(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=checkMiniChefBalances())

async def executor(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=checkExecutorBalances())

async def circulatingSupply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=checkCirculatingSupply())

async def cctp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=checkCCTPBalances())

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle errors gracefully, especially Conflict errors from multiple bot instances."""
    error = context.error
    
    if isinstance(error, Conflict):
        # Another bot instance is running - this is expected in some deployment scenarios
        # Log at debug level instead of error to reduce noise
        logging.debug(f"Conflict error (another bot instance may be running): {error}")
        return
    
    # Log other errors normally
    logging.error(f"Update {update} caused error {error}", exc_info=error)

async def post_init(application):
    """Set bot description and short description on startup."""
    try:
        short_desc = "Monitor Synapse Protocol infrastructure across 20+ chains"
        full_desc = """Monitor Synapse Protocol infrastructure across 20+ blockchain networks.

Commands:
/balance - Check gas balances on bridge contracts
/rewards - Check SYN token balances in MiniChef
/executor - Check executor gas balances
/circulatingSupply - Check total SYN circulating supply
/cctp - Check CCTP relayer gas balances

Monitors: Arbitrum, Aurora, Avalanche, Base, Blast, Boba, BSC, Canto, Cronos, DFK, Dogechain, Ethereum, Fantom, Harmony, Klaytn, Metis, Moonriver, Moonbeam, Optimism, Polygon"""
        
        await application.bot.set_my_short_description(short_description=short_desc)
        await application.bot.set_my_description(description=full_desc)
        logging.info("Bot description updated successfully")
    except Exception as e:
        logging.warning(f"Could not set bot description: {e}")

if __name__ == '__main__':
    application = ApplicationBuilder().token('6238485166:AAHY3jVaTFFi4uBa5j5ZD58IyGygsYkeD44').post_init(post_init).build()
    
    # Add error handler
    application.add_error_handler(error_handler)
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    gasBalance_handler = CommandHandler('balance', balance)
    application.add_handler(gasBalance_handler)

    minichefBalance_handler = CommandHandler('rewards', rewards)
    application.add_handler(minichefBalance_handler)

    executorBalance_handler = CommandHandler('executor', executor)
    application.add_handler(executorBalance_handler)

    circulatingSupply_handler = CommandHandler('circulatingSupply', circulatingSupply)
    application.add_handler(circulatingSupply_handler)

    cctp_handler = CommandHandler('cctp', cctp)
    application.add_handler(cctp_handler)
    
    # Run with drop_pending_updates to avoid processing old updates
    application.run_polling(drop_pending_updates=True)