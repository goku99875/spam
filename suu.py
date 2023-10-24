import random
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Function to generate random data
def generate_random_data():
    random_name = generate_random_name()
    random_phone = generate_random_phone_number("US", "({area_code}) {local_number}")
    random_address = generate_random_address()
    random_card_number = generate_random_card_number()
    random_expiration_date = generate_random_expiration_date()
    random_cvv = generate_random_cvv()
    
    return f"Name: {random_name}\nPhone Number: {random_phone}\nAddress: {random_address}\nCard Number: {random_card_number}\nExpiration Date: {random_expiration_date}\nCVV: {random_cvv}"

# Initialize the Telegram bot
updater = Updater(token='6541468487:AAFCJf2YY0sS7htgjo-35dRqw8bGEgrwQ24', use_context=True)
dispatcher = updater.dispatcher

# Define a command handler to trigger the data generation
def start(update: Update, context: CallbackContext):
    random_data = generate_random_data()
    context.bot.send_message(chat_id=update.effective_chat.id, text=random_data)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# Define a message handler to respond to user messages
def respond_to_message(update: Update, context: CallbackContext):
    if any(keyword in update.message.text.lower() for keyword in ['random', 'generate']):
        random_data = generate_random_data()
        context.bot.send_message(chat_id=update.effective_chat.id, text=random_data)

message_handler = MessageHandler(Filters.text & (~Filters.command), respond_to_message)
dispatcher.add_handler(message_handler)

# Start the bot
updater.start_polling()
updater.idle()
