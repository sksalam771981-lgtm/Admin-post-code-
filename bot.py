import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Welcome! Please send me a video.')

async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    video = update.message.video
    await update.message.reply_text('Video received! Now please reply with a title for this video.')

if __name__ == '__main__':
    application = ApplicationBuilder().token('8162257584:AAGu6N2FrHhkVUWF67ifGQmbD_0V-5m_UAI').build()
    
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.VIDEO, handle_video))
    
    application.run_polling()
