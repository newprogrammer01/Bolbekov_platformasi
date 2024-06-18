from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, CallbackQueryHandler
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
import os

TOKEN = os.environ['TOKEN']

def start(update: Update, context: CallbackContext):
    bot = context.bot
    user_id = update.message.from_user.id
    chat_id = update.message.chat_id
    first_name = update.message.from_user.first_name
    text = f'Assalomu alaykum {first_name}, botimizga xush kelibsiz! Bu bot sizga uz bilim va ko\'nikmalaringizni mustahkamlashingizga yordam beradi'
    keyboard = ReplyKeyboardMarkup([
        ["Ma'ruzalar", 'Mustaqil ish mavzulari'],
        
        ['Nazorat savollari', "O'quv Uslubiy Majmua"]
    ], resize_keyboard=True)
    bot.sendMessage(chat_id=chat_id, reply_markup=keyboard, text=text)

def maruzalar(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    bot = context.bot
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(text="1-ma'ruza", callback_data='bir'),InlineKeyboardButton(text="2-ma'ruza", callback_data='ikki'),InlineKeyboardButton(text="3-ma'ruza", callback_data='uch')],
        [InlineKeyboardButton(text="4-ma'ruza", callback_data='turt'),InlineKeyboardButton(text="5-ma'ruza", callback_data='besh'),InlineKeyboardButton(text="6-ma'ruza", callback_data='olti')],
        [InlineKeyboardButton(text="7-ma'ruza", callback_data='yetti'),InlineKeyboardButton(text="8-ma'ruza", callback_data='sakkiz'),InlineKeyboardButton(text="9-ma'ruza", callback_data='tuqqiz')],
        [InlineKeyboardButton(text="10-ma'ruza", callback_data='un'),InlineKeyboardButton(text="11-ma'ruza", callback_data='unbir'),InlineKeyboardButton(text="12-ma'ruza", callback_data='unikki')],
        [InlineKeyboardButton(text="13-ma'ruza", callback_data='unuch'),InlineKeyboardButton(text="14-ma'ruza", callback_data='unturt'),InlineKeyboardButton(text="15-ma'ruza", callback_data='unbesh')],
        
    ])
    bot.sendMessage(chat_id=chat_id, reply_markup=keyboard, text="Ma'ruzalar darsliklari fayllari.")



def mustaqil_ish_mavzulari(update, context):
    chat_id = update.message.chat_id
    bot = context.bot
    
    docx_file = 'mustaqil_ishlar/1_2.docx'  # Replace with your actual path to the specific .docx file
    
    with open(docx_file, 'rb') as f:
        bot.send_document(chat_id=chat_id, document=f)


def nazorat_savollari(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    bot = context.bot
    
    docx_file = 'KAKT Yakuniy savollar.docx'  # Replace with the actual path to your DOCX file
    
    with open(docx_file, 'rb') as f:
        bot.send_document(chat_id=chat_id, document=f)
def oquv_uslubiy_majmua(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    bot = context.bot
    
    docx_file = 'KAKT MAJMUA.docx'  # Replace with the actual path to your KAKt majuma.docx file
    
    with open(docx_file, 'rb') as f:
        bot.send_document(chat_id=chat_id, document=f)


def query(update: Update, context: CallbackContext):
    query = update.callback_query
    chat_id = query.message.chat.id
    data = query.data
    bot = context.bot
    
    # Fayllar joylashgan papka
    pdf_directory = 'maruzalar'
    
    # Callback data bilan fayl nomlarini bog'lash
    pdf_files = {
        'bir': '1.pdf',
        'ikki': '2.pdf',
        'uch': '3.pdf',
        'turt': '4.pdf',
        'besh': '5.pdf',
        'olti': '6.pdf',
        'yetti': '7.pdf',
        'sakkiz': '8.pdf',
        'tuqqiz': '9.pdf',
        'un': '10.pdf',
        'unbir': '11.pdf',
        'unikki': '12.pdf',
        'unuch': '13.pdf',
        'unturt': '14.pdf',
        'unbesh': '15.pdf'
    }

    if data in pdf_files:
        file_path = os.path.join(pdf_directory, pdf_files[data])
        with open(file_path, 'rb') as f:
            bot.sendDocument(chat_id=chat_id, document=f)

updater = Updater(token=TOKEN)
dp = updater.dispatcher

dp.add_handler(CommandHandler('start', start))
dp.add_handler(MessageHandler(Filters.text("Ma'ruzalar"), maruzalar))
dp.add_handler(CallbackQueryHandler(query))
dp.add_handler(MessageHandler(Filters.text("Mustaqil ish mavzulari"), mustaqil_ish_mavzulari))
dp.add_handler(MessageHandler(Filters.text("Nazorat savollari"), nazorat_savollari))
dp.add_handler(MessageHandler(Filters.text("O'quv Uslubiy Majmua"), oquv_uslubiy_majmua))




updater.start_polling()
updater.idle()
