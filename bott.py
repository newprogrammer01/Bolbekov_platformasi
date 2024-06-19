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
        ["Ma'ruzalar", 'Laboratoriyalar'],
        ['Mustaqil ish mavzulari'],
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
def laboratoriyalar(update:Update, context:CallbackContext):
    chat_id=update.message.chat_id
    bot=context.bot
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(text="1-laboratoriya", callback_data='lbir'),InlineKeyboardButton(text="2-laboratoriya", callback_data='likki'),InlineKeyboardButton(text="3-laboratoriya", callback_data='luch')],
        [InlineKeyboardButton(text="4-laboratoriya", callback_data='lturt'),InlineKeyboardButton(text="5-laboratoriya", callback_data='lbesh'),InlineKeyboardButton(text="6-laboratoriya", callback_data='lolti')],
        [InlineKeyboardButton(text="7-laboratoriya", callback_data='lyetti'),InlineKeyboardButton(text="8-laboratoriya", callback_data='lsakkiz'),InlineKeyboardButton(text="9-laboratoriya", callback_data='ltuqqiz')],
        [InlineKeyboardButton(text="10-laboratoriya", callback_data='lun'),InlineKeyboardButton(text="11-laboratoriya", callback_data='lunbir'),InlineKeyboardButton(text="12-laboratoriya", callback_data='lunikki')],
        [InlineKeyboardButton(text="13-laboratoriya", callback_data='lunuch'),InlineKeyboardButton(text="14-laboratoriya", callback_data='lunturt'),InlineKeyboardButton(text="15-laboratoriya", callback_data='lunbesh')],
    ])
    bot.sendMessage(chat_id=chat_id, reply_markup=keyboard, text='Laboratoriya darsliklari fayllari.')


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


# def query(update: Update, context: CallbackContext):
#     query = update.callback_query
#     chat_id = query.message.chat.id
#     data = query.data
#     bot = context.bot
    
#     # Fayllar joylashgan papka
#     pdf_directory = 'maruzalar'
    
#     # Callback data bilan fayl nomlarini bog'lash
#     pdf_files = {
#         'bir': '1.pdf',
#         'ikki': '2.pdf',
#         'uch': '3.pdf',
#         'turt': '4.pdf',
#         'besh': '5.pdf',
#         'olti': '6.pdf',
#         'yetti': '7.pdf',
#         'sakkiz': '8.pdf',
#         'tuqqiz': '9.pdf',
#         'un': '10.pdf',
#         'unbir': '11.pdf',
#         'unikki': '12.pdf',
#         'unuch': '13.pdf',
#         'unturt': '14.pdf',
#         'unbesh': '15.pdf'
#     }

#     if data in pdf_files:
#         file_path = os.path.join(pdf_directory, pdf_files[data])
#         with open(file_path, 'rb') as f:
#             bot.sendDocument(chat_id=chat_id, document=f)

def query(update: Update, context: CallbackContext):
    query = update.callback_query
    chat_id = query.message.chat.id
    data = query.data
    bot = context.bot
    
    # Fayllar joylashgan papkalar
    pdf_directory_maruzalar = 'maruzalar'
    pdf_directory_laboratoriyalar = 'laboratoriyalar'
    
    # Callback data bilan fayl nomlarini bog'lash
    pdf_files = {
        'bir': ('maruzalar', '1.pdf'),
        'ikki': ('maruzalar', '2.pdf'),
        'uch': ('maruzalar', '3.pdf'),
        'turt': ('maruzalar', '4.pdf'),
        'besh': ('maruzalar', '5.pdf'),
        'olti': ('maruzalar', '6.pdf'),
        'yetti': ('maruzalar', '7.pdf'),
        'sakkiz': ('maruzalar', '8.pdf'),
        'tuqqiz': ('maruzalar', '9.pdf'),
        'un': ('maruzalar', '10.pdf'),
        'unbir': ('maruzalar', '11.pdf'),
        'unikki': ('maruzalar', '12.pdf'),
        'unuch': ('maruzalar', '13.pdf'),
        'unturt': ('maruzalar', '14.pdf'),
        'unbesh': ('maruzalar', '15.pdf'),
        'lbir': ('laboratoriyalar', '1.pdf'),
        'likki': ('laboratoriyalar', '2.pdf'),
        'luch': ('laboratoriyalar', '3.pdf'),
        'lturt': ('laboratoriyalar', '4.pdf'),
        'lbesh': ('laboratoriyalar', '5.pdf'),
        'lolti': ('laboratoriyalar', '6.pdf'),
        'lyetti': ('laboratoriyalar', '7.pdf'),
        'lsakkiz': ('laboratoriyalar', '8.pdf'),
        'ltuqqiz': ('laboratoriyalar', '9.pdf'),
        'lun': ('laboratoriyalar', '10.pdf'),
        'lunbir': ('laboratoriyalar', '11.pdf'),
        'lunikki': ('laboratoriyalar', '12.pdf'),
        'lunuch': ('laboratoriyalar', '13.pdf'),
        'lunturt': ('laboratoriyalar', '14.pdf'),
        'lunbesh': ('laboratoriyalar', '15.pdf')
    }

    if data in pdf_files:
        directory, file_name = pdf_files[data]
        file_path = os.path.join(directory, file_name)
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
dp.add_handler(MessageHandler(Filters.text('Laboratoriyalar'), laboratoriyalar))



updater.start_polling()
updater.idle()
