import os 
TOKEN = os.getenv('TOKEN')

from telegram.ext import( 
                         
        Updater,
        CommandHandler,
        MessageHandler,
        Filters,
        
        
        
    )
from handlars import (
    start,
    sendMessage,
    sendFoto,
    sendDocument,
    sendAudio,
    sendVideo,
    sendAnimation,
    sendVoice,
    sendVideoNote,
    sendMediaGroup,
    sendLocation,
    sendContact,
    sendDice,
    sendSticker,
)

def main():
    
    updater = Updater(TOKEN)
    
    dp = updater.dispatcher
    
    dp.add_handler(handler=CommandHandler( command=['start'],callback=start))
    
    dp.add_handler(handler=MessageHandler(filters=Filters.text,callback=sendMessage))
    
    dp.add_handler(handler=MessageHandler(filters=Filters.photo, callback=sendFoto))
    
    dp.add_handler(handler=MessageHandler(filters=Filters.document, callback=sendDocument))
    
    dp.add_handler(handler=MessageHandler(filters=Filters.audio, callback=sendAudio))
    
    dp.add_handler(handler=MessageHandler(filters=Filters.video, callback=sendVideo))
    
    dp.add_handler(handler=MessageHandler(filters=Filters.animation, callback=sendAnimation))
    
    dp.add_handler(handler=MessageHandler(filters=Filters.voice, callback=sendVoice))
    
    dp.add_handler(handler=MessageHandler(filters=Filters.video_note, callback=sendVideoNote))
    
    dp.add_handler(handler=MessageHandler(filters=Filters.group, callback=sendMediaGroup))
    
    dp.add_handler(handler=MessageHandler(filters=Filters.location, callback=sendLocation))
    
    dp.add_handler(handler=MessageHandler(filters=Filters.contact , callback=sendContact))
    
    dp.add_handler(handler=MessageHandler(filters=Filters.animation,callback=sendDice))
    
    dp.add_handler(handler=MessageHandler(filters=Filters.sticker, callback=sendSticker))
    
    updater.start_polling()
    updater.idle()
    
main()