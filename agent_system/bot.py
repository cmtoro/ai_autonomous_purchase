import telebot
import os
import logging
# use package import so bot.py can be imported from outside the folder
from agent_system.engine import agent

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Retrieve token from environment variables
TOKEN = os.getenv('TELEGRAM_TOKEN')
logger.info(f"TELEGRAM_TOKEN configured: {bool(TOKEN)}")
# Delay bot creation until we know a token is present; importing this
# module in a test or from another package shouldn't attempt to connect.
if TOKEN:
    bot = telebot.TeleBot(TOKEN)
    logger.info("Telegram bot initialized successfully")
else:
    bot = None
    logger.warning("No TELEGRAM_TOKEN found, bot not initialized")

# Handlers are only registered if we have a bot instance
if bot is not None:
    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        logger.info(f"Received command: {message.text} from user {message.from_user.id}")
        bot.reply_to(message, "Hello! I'm your AI Architect. Give me instructions to modify your app.")
        logger.info("Sent welcome message")

    # In agent_system/bot.py
    @bot.message_handler(func=lambda message: True)
    def handle_instruction(message):
        logger.info(f"Received instruction: '{message.text}' from user {message.from_user.id}")
        instruction = message.text
        prompt = (
            "Your goal is to implement features requested by the user and ensure the code is functional. "
            f"Task: {instruction} "
            "Use the provided tools to modify the repository code."
        )
        logger.info("Constructed prompt for agent")
        # The agent graph returned by `create_agent` no longer has a `run` helper.
        # We need to invoke it with the structured input it expects (a list of
        # messages).  We'll pass our prompt as a single HumanMessage and extract
        # the content of the resulting AIMessage.
        from langchain_core.messages import HumanMessage

        try:
            logger.info("Invoking agent with prompt")
            result = agent.invoke({"messages": [HumanMessage(content=prompt)]})
            logger.info("Agent invocation completed")
            # result typically looks like {'messages': [AIMessage(...)]}
            messages = result.get("messages", [])
            if messages:
                ai_msg = messages[-1]
                bot_response = getattr(ai_msg, "content", str(ai_msg))
                logger.info(f"Agent response: {bot_response[:100]}...")  # Log first 100 chars
            else:
                bot_response = str(result)
                logger.warning("No messages in agent result")
        except Exception as e:
            logger.error(f"Error running agent: {e}")
            bot_response = f"Error running agent: {e}"

        bot.reply_to(message, f"Agent Response: {bot_response}")
        logger.info("Sent response to user")

    if __name__ == "__main__":
        logger.info("Starting bot polling")
        bot.polling()
        logger.info("Bot polling stopped")
else:
    # no token; the module can still be imported safely without creating a bot
    def send_welcome(*args, **kwargs):
        raise RuntimeError("Telegram token not configured")
    def handle_instruction(*args, **kwargs):
        raise RuntimeError("Telegram token not configured")
