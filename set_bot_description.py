#!/usr/bin/env python3
"""Script to set the Telegram bot description."""
import asyncio
import os
from telegram import Bot

# Load environment variables from .env file if it exists (for local development)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # python-dotenv not installed, skip loading .env file
    pass

# Get bot token from environment variable
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
if not BOT_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN environment variable is not set")

# Short description (shown in chat list and bot profile)
SHORT_DESCRIPTION = "Monitor Synapse Protocol infrastructure across 20+ chains"

# Full description (shown in bot's "About" section)
DESCRIPTION = """Monitor Synapse Protocol infrastructure across 20+ blockchain networks.

Commands:
/balance - Check gas balances on bridge contracts
/rewards - Check SYN token balances in MiniChef
/executor - Check executor gas balances
/circulatingSupply - Check total SYN circulating supply
/cctp - Check CCTP relayer gas balances

Monitors: Arbitrum, Aurora, Avalanche, Base, Blast, Boba, BSC, Canto, Cronos, DFK, Dogechain, Ethereum, Fantom, Harmony, Klaytn, Metis, Moonriver, Moonbeam, Optimism, Polygon"""

async def set_bot_description():
    """Set the bot's short description and full description."""
    bot = Bot(token=BOT_TOKEN)
    
    try:
        # Set short description (bio)
        result_short = await bot.set_my_short_description(short_description=SHORT_DESCRIPTION)
        print(f"✓ Short description set: {result_short}")
        
        # Set full description (about)
        result_full = await bot.set_my_description(description=DESCRIPTION)
        print(f"✓ Full description set: {result_full}")
        
        print("\nBot description updated successfully!")
        
    except Exception as e:
        print(f"Error setting bot description: {e}")

if __name__ == '__main__':
    asyncio.run(set_bot_description())

