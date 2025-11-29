# Synapse Monitoring Bot

A Telegram bot for monitoring Synapse Protocol infrastructure across multiple blockchain networks. This bot provides real-time information about gas balances, token balances, and circulating supply across all supported chains.

## Features

The bot monitors Synapse Protocol across **20+ blockchain networks** including:
- Arbitrum, Aurora, Avalanche, Base, Blast, Boba, BSC
- Canto, Cronos, DFK, Dogechain, Ethereum, Fantom
- Harmony, Klaytn, Metis, Moonriver, Moonbeam
- Optimism, Polygon

### Available Commands

- `/start` - Start the bot and get a welcome message
- `/balance` - Check native gas balances on bridge contracts across all chains
- `/rewards` - Check SYN token balances in MiniChef reward contracts
- `/executor` - Check executor gas balances across all chains
- `/circulatingSupply` - Check total circulating supply of SYN tokens across all chains
- `/cctp` - Check CCTP (Cross-Chain Transfer Protocol) relayer gas balances

## Setup

### Prerequisites

- Python 3.10+
- A Telegram Bot Token (obtain from [@BotFather](https://t.me/botfather))

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Defi-Moses/synapse-monitoring-bot.git
cd synapse-monitoring-bot
```

2. Create a virtual environment:
```bash
python3 -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure your Telegram bot token in `bot.py`:
   - Replace the token in line 31 with your own bot token from BotFather

## Configuration

The bot uses `config.py` to store chain configurations including:
- RPC endpoints for each chain
- Bridge contract addresses
- MiniChef contract addresses
- SYN token contract addresses
- CCTP relayer addresses

To add or modify chains, edit the `chains` dictionary in `config.py`.

## Usage

1. Start the bot:
```bash
python bot.py
```

2. Open Telegram and find your bot

3. Send `/start` to begin

4. Use any of the available commands to check Synapse Protocol status across chains

### Example Usage

```
/balance
# Returns gas balances for bridge contracts on all chains

/rewards
# Returns SYN token balances in MiniChef contracts

/circulatingSupply
# Returns total SYN circulating supply across all chains
```

## Project Structure

```
.
├── bot.py              # Telegram bot handlers and command definitions
├── main.py             # Core monitoring functions
├── config.py           # Chain configurations and contract addresses
├── requirements.txt    # Python dependencies
├── Procfile           # Heroku deployment configuration
└── bridges-server/    # Additional bridge server codebase
```

## Deployment

The bot can be deployed to Heroku using the included `Procfile`. Make sure to:

1. Set your Telegram bot token as an environment variable (recommended) or update `bot.py`
2. Deploy using Heroku CLI or GitHub integration

## Dependencies

Key dependencies include:
- `python-telegram-bot` - Telegram bot framework
- `web3` - Ethereum and EVM chain interaction
- `requests` - HTTP requests for RPC calls

See `requirements.txt` for the complete list.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available for use.

## Support

For issues or questions, please open an issue on GitHub.
