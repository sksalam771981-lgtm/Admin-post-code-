import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
    ConversationHandler,
)

# Logging setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# States
WAITING_FOR_TITLE = 1

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Welcome! Please send me a video.')

async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    video = update.message.video
    context.user_data['video_file_id'] = video.file_id
    await update.message.reply_text('এখন ভিডিওর Title লিখুন।')
    return WAITING_FOR_TITLE

async def handle_title(update: Update, context: ContextTypes.DEFAULT_TYPE):
    title = update.message.text
    file_id = context.user_data.get('video_file_id')
    
    # ইউনিক লিঙ্ক তৈরি করা (আপনার উদাহরণ অনুযায়ী)
    unique_link = f"https://t.me/PrivateVideoXBot?start={file_id[-10:]}"
    
    await update.message.reply_text(
        f"✅ Video Uploaded Successfully\n\n"
        f"🎬 Title: {title}\n\n"
        f"🔗 Share Link:\n{unique_link}"
    )
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Cancelled.')
    return ConversationHandler.END

def main():
    # এখানে আপনার টেলিগ্রাম বটের টোকেন বসাবেন
    application = Application.Builder().token('8162257584:AAGu6N2FrHhkVUWF67ifGQmbD_0V-5m_UAI').build()

    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(filters.VIDEO, handle_video)],
        states={
            WAITING_FOR_TITLE: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_title)],
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    application.add_handler(CommandHandler('start', start))
    application.add_handler(conv_handler)

    application.run_polling()

if __name__ == '__main__':
    main()
