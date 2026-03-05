import telebot
import os

# Retrieve token from environment variables
TOKEN = os.getenv('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I'm your AI Architect. Give me instructions to modify your app.")

@bot.message_handler(func=lambda message: True)
def handle_instruction(message):
    # This is where the LLM Agent will come into action later
    instruction = message.text
    bot.reply_to(message, f"Received. I will analyze how to implement: '{instruction}'")

bot.polling()