# Railway Deployment Setup

## Setting the Telegram Bot Token

To deploy this bot on Railway, you need to set the `TELEGRAM_BOT_TOKEN` environment variable:

1. Go to your Railway project dashboard
2. Click on your service
3. Go to the **Variables** tab
4. Click **+ New Variable**
5. Set:
   - **Variable Name**: `TELEGRAM_BOT_TOKEN`
   - **Value**: Your bot token from BotFather
6. Click **Add**
7. Railway will automatically redeploy with the new environment variable

## Local Development Setup

For local development, create a `.env` file in the project root:

```bash
TELEGRAM_BOT_TOKEN=your_bot_token_here
```

**Important**: 
- The `.env` file is already in `.gitignore` and will NOT be committed to the repository
- Never commit your bot token to the repository
- Always use environment variables for sensitive credentials

