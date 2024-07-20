import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "")
    API_HASH  = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

    # database config
    DB_NAME = os.environ.get("DB_NAME","")     
    DB_URL  = os.environ.get("DB_URL","")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://graph.org/file/4b306f4b15c23a8f22e58.jpg")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]
    FORCE_SUB   = os.environ.get("FORCE_SUB", "") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
    
    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))


class Txt(object):
    # part of text configuration
        
    START_TXT = """<b>😊 ʜᴇʟʟᴏ</b> {} 
    
<b>➻ ᴛʜɪs ɪs ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀɴᴅ ʏᴇᴛ ᴘᴏᴡᴇʀғᴜʟ ʀᴇɴᴀᴍᴇ ʙᴏᴛ.</b>
    
<b>➻ ᴜsɪɴɢ ᴛʜɪs ʙᴏᴛ ʏᴏᴜ ᴄᴀɴ ᴀᴜᴛᴏ ʀᴇɴᴀᴍᴇ ᴏғ ʏᴏᴜʀ ғɪʟᴇs.</b>
    
<b>➻ ᴛʜɪs ʙᴏᴛ ᴀʟsᴏ sᴜᴘᴘᴏʀᴛs ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ᴀɴᴅ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ.</b>
    
<b>➻ ᴜsᴇ /tutorial ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ.</b>
    
<b>ʙᴏᴛ ɪs ᴍᴀᴅᴇ ʙʏ @AeroBots_Tm</b>"""
    
    FILE_NAME_TXT = """<b>sᴇᴛᴜᴘ ᴀᴜᴛᴏ ʀᴇɴᴀᴍᴇ ғᴏʀᴍᴀᴛ</b>

<b>ᴜsᴇ ᴛʜᴇsᴇ ᴋᴇʏᴡᴏʀᴅs ᴛᴏ sᴇᴛᴜᴘ ᴄᴜsᴛᴏᴍ ғɪʟᴇ ɴᴀᴍᴇ</b>

<b>✓ episode :- ᴛᴏ ʀᴇᴘʟᴀᴄᴇ ᴇᴘɪsᴏᴅᴇ ɴᴜᴍʙᴇʀ</b>
<b>✓ quality :- ᴛᴏ ʀᴇᴘʟᴀᴄᴇ ᴠɪᴅᴇᴏ ʀᴇsᴏʟᴜᴛɪᴏɴ</b>

<b>➻ Exᴀᴍᴘʟᴇ :</b> <code> /autorename [S1-Eepisode] [quality] Naruto Shippuden [@AeroBots_Tm] </code>

<b>➻ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ᴀᴜᴛᴏ ʀᴇɴᴀᴍᴇ ғᴏʀᴍᴀᴛ :</b> <code>{format_template}</code> """
    
    ABOUT_TXT = f"""<b>๏ ᴍʏ ɴᴀᴍᴇ :</b> <a href='https://t.me/Aero_Renamer_Probot'>ᴀᴜᴛᴏ ʀᴇɴᴀᴍᴇʀ ʙᴏᴛ</a>
<b>๏ ʟᴀɴɢᴜᴀɢᴇ :</b> <a href='https://python.org'>ᴘʏᴛʜᴏɴ 3</b></a>
<b>๏ ʟɪʙʀᴀʀʏ :</b> <a href='https://pyrogram.org'>ᴘʏʀᴏɢʀᴀᴍ 2.0</b></a>
<b>๏ sᴇʀᴠᴇʀ :</b> <a href='https://heroku.com'>ʜᴇʀᴏᴋᴜ</a>
<b>๏ ᴄʜᴀɴɴᴇʟ :</b> <a href='https://t.me/AeroBots_Tm'>ᴀᴇʀᴏ ʙᴏᴛs</b></a>
<b>๏ ᴅᴇᴠᴇʟᴏᴘᴇʀ :</b> <a href='https://t.me/Mikoyo'>ᴍɪᴋᴏʏᴏ</b></a>
    
<b>⌬ ʙᴏᴛ ᴍᴀᴅᴇ ʙʏ :</b> @AeroBots_Tm"""

    
    THUMBNAIL_TXT = """<b>🖼️  ʜᴏᴡ ᴛᴏ sᴇᴛ ᴛʜᴜᴍʙɴᴀɪʟ</b>
    
<b>⦿ ʏᴏᴜ ᴄᴀɴ ᴀᴅᴅ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ sɪᴍᴘʟʏ ʙʏ sᴇɴᴅɪɴɢ ᴀ ᴘʜᴏᴛᴏ ᴛᴏ ᴍᴇ....</b>
    
<b>⦿ /viewthumb - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ sᴇᴇ ʏᴏᴜʀ ᴛʜᴜᴍʙɴᴀɪʟ</b>
<b>⦿ /delthumb - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴛʜᴜᴍʙɴᴀɪʟ</b>"""

    CAPTION_TXT = """<b>📝  ʜᴏᴡ ᴛᴏ sᴇᴛ ᴄᴀᴘᴛɪᴏɴ</b>
    
⦿ /set_caption - <b>ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ sᴇᴛ ʏᴏᴜʀ ᴄᴀᴘᴛɪᴏɴ</b>
⦿ /see_caption - <b>ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ sᴇᴇ ʏᴏᴜʀ ᴄᴀᴘᴛɪᴏɴ</b>
⦿ /del_caption - <b>ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴄᴀᴘᴛɪᴏɴ</b>"""

    PROGRESS_BAR = """\n
<b>‣ Sɪᴢᴇ</b> : {1} | {2}
<b>‣ Dᴏɴᴇ</b> : {0}%
<b>‣ Sᴘᴇᴇᴅ</b> : {3}/s
<b>‣ Eᴛᴀ</b> : {4} """
    
    
    DONATE_TXT = """<b>🥲 ᴛʜᴀɴᴋs ғᴏʀ sʜᴏᴡɪɴɢ ɪɴᴛᴇʀᴇsᴛ ɪɴ ᴅᴏɴᴀᴛɪᴏɴ! ❤️</b>
    
<b>ɪғ ʏᴏᴜ ʟɪᴋᴇ ᴍʏ ʙᴏᴛs & ᴘʀᴏᴊᴇᴄᴛs, ʏᴏᴜ ᴄᴀɴ ᴅᴏɴᴀᴛᴇ ᴍᴇ ᴀɴʏ ᴀᴍᴏᴜɴᴛ ғʀᴏᴍ 20 ʀs ᴜᴘᴛᴏ ʏᴏᴜʀ ᴄʜᴏɪᴄᴇ.</b>
    
<b>🛍 ᴜᴘɪ ɪᴅ:</b> <code>zoyaya@fam</code> """
    
    HELP_TXT = """<b>Hey</b> {}
    
<b>ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ғᴏʀ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs.</b>"""





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Developer @JishuDeveloper

