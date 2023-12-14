from telegram.ext import CallbackContext

from telegram import (
    Update,
    InputMediaAnimation,
    InputMediaAudio,
    InputMediaDocument,
    InputMediaPhoto,
    InputMediaVideo,
    
)



def start(update:Update, context: CallbackContext):
    user = update.message.from_user.full_name
    chat_id = update.message.chat.id
    
    welcome_msg = f'Hello  - {user} !!! There are problems with some of the sendContact,sendMediaGroup methods here. Are we fixing this?'
    
    bot = context.bot
    
    bot.send_message(chat_id=chat_id, text = welcome_msg)
    
def sendMessage(update:Update, context:CallbackContext):
    user = update.message.from_user
    message = update.message
    bot = context.bot
    bot.send_message(chat_id = user.id, text = message.text)
 
def sendFoto(update:Update,context:CallbackContext):
    chat_id = update.message.from_user.id
    photo = update.message.photo
    
    bot = context.bot
    
    bot.send_photo(chat_id=chat_id,photo=photo[-1])
    
def sendDocument(update:Update,context:CallbackContext):
    chat_id = update.message.from_user.id
    file = update.message.document
    
    bot = context.bot
    
    bot.send_document(chat_id=chat_id, document = file.file_id)
    
def sendAudio(update:Update,context:CallbackContext):
    chat_id = update.message.from_user.id
    audio = update.message.audio
    
    bot = context.bot
    
    bot.send_audio(chat_id=chat_id, audio=audio)
    
def sendVideo(update:Update, context:CallbackContext):
    chat_id = update.message.from_user.id
    video = update.message.video
    
    bot = context.bot
    
    bot.send_video(chat_id=chat_id, video=video)
    
def sendAnimation(update:Update, context:CallbackContext):
    chat_id = update.message.from_user.id
    animation = update.message.animation
    
    bot = context.bot
    
    bot.send_animation(chat_id=chat_id, animation=animation)
    
def sendVoice(update:Update,context:CallbackContext):
    chat_id = update.message.from_user.id
    voice = update.message.voice
    
    bot = context.bot
    
    bot.send_voice(chat_id=chat_id, voice=voice)
    
def sendVideoNote(update:Update,context:CallbackContext):
    chat_id = update.message.from_user.id
    video = update.message.video_note
    
    bot = context.bot
    
    bot.send_video_note(chat_id=chat_id,video_note=video)
    
def sendMediaGroup(update:Update,context:CallbackContext):
    chat_id = update.message.from_user.id
    media = update.message.media_group_id
    
    bot = context.bot
    
    bot.send_media_group(chat_id=chat_id, media=media)
    
    
def sendLocation(update:Update, context:CallbackContext):
    chat_id = update.message.from_user.id
    latitude = update.message.location.latitude
    longitude = update.message.location.longitude
    
    bot = context.bot
    bot.send_location(chat_id=chat_id,latitude=latitude,longitude=longitude)
    
def sendContact(update:Update, context:CallbackContext):
    chat_id = update.message.chat.id
    phone_number = update.message.contact.phone_number
    first_name = update.message.contact.first_name
   
    
    bot = context.bot
    bot.send_contact(chat_id=chat_id, phone_number=phone_number, first_name=first_name)
    
def sendDice(update:Update, context:CallbackContext):
    chat_id = update.message.from_user.id
    emoji = update.message.animation
    
    bot = context.bot
    bot.send_dice(chat_id=chat_id,emoji=emoji)

def sendSticker(update:Update,context:CallbackContext):
    chat_id = update.message.from_user.id
    sticker = update.message.sticker
    
    bot = context.bot
    bot.send_sticker(chat_id = chat_id,sticker=sticker)