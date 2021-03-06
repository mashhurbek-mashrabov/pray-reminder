import os

from django.db import models

BOT_TOKEN = os.getenv('BOT_TOKEN')
CONFIRMATION_CHANNEL_ID = os.getenv('CONFIRMATION_CHANNEL_ID')
MAIN_CHANNEL_ID = os.getenv('MAIN_CHANNEL_ID')
GREETING_VOICE = os.getenv('GREETING_VOICE')
CHANNEL_PHOTO = os.getenv('CHANNEL_PHOTO')
EXCEPTION_CHANNEL_ID = os.getenv('EXCEPTION_CHANNEL_ID')
PHOTO_STORAGE_CHANNEL = os.getenv('PHOTO_STORAGE_CHANNEL')
CHAT_GROUP_USERNAME = os.getenv('CHAT_GROUP_USERNAME')
# GROUP_CHAT_ID = os.getenv('GROUP_CHAT_ID')

messages = {
    'greeting': 'π Assalom alaykum, xush kelibsiz! Men sizga kunlik namoz vaqtlarini yuborib tuaraman.',
    'uzbek': 'πΊπΏ O`zbek tili',
    'russian': 'π·πΊ Π ΡΡΡΠΊΠΈΠΉ',
    'confirm emoji': 'β',
    'decline emoji': 'β',
    'send message': "π€ Xabar jo'natish",
    'main menu': 'βοΈ Asosiy menu',
    'back_button': 'β¬οΈ Ortga',
    'cancel': 'β Bekor qilish',
    'write message': "β Xabarni kiriting",
    'confirm message': "Ushbu xabarni tasdiqlaysizmi ?",
    'declined': "β Bekor qilindi",
    'confirmed': "β Tasdiqlandi",
    'successful': "β Yetkazildi : ",
    'unsuccessful': "β Yetkazilmadi : ",
    'uz': {
        'language flag': 'πΊπΏ',
        'back_button': 'β¬οΈ Ortga',
    },

    'ru': {
        'language flag': 'π·πΊ',
        'back_button': 'β¬οΈ Ortga',
    }

}


class CallbackData:
    main_menu_button = 'main menu'
    back_button = 'back button'
    confirm = 'confirm'
    decline = 'decline'
    sold_out = 'sold_out'


class BotUserSteps:
    MAIN_MENU = 1
    GET_MSG = 2
    ASK_CONFIRMATION = 3


class BotUserLanguageChoices(models.TextChoices):
    UZBEK = 'uz'
    RUSSIAN = 'ru'


class Moderators:
    admins_id = [
        1004815988,
        1004815988
    ]
