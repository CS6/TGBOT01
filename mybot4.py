##加入溫度監控
#可直接使用的BOT
#V1
#!/usr/bin/env python3
#-*- coding: utf-8 -*-



#app = Flask(__name__)

#logging.basicConfig(level=logging.DEBUG,

#                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#bot_name = '@aboutbig6bot'

#bot = telegram.Bot(token='344519590:AAH1Gzn260TvJRHclFPBGW8S1mmBPNJW8Gw')


#TEXT = '您好'

#bot.sendMessage(chat_id='-230670018', text='我是新人')
#bot.sendMessage(chat_id='-230670018', text=TEXT)
#bot.setWebhook("https://sddivid.tw")  
#https://api.telegram.org/bot344519590:AAH1Gzn260TvJRHclFPBGW8S1mmBPNJW8Gw/sendMessage?chat_id=@big666bot&text=test
#curl https://api.telegram.org/bot344519590:AAH1Gzn260TvJRHclFPBGW8S1mmBPNJW8Gw/setWebhook?url=sean.taipei/telegram/hook.php
#https://api.telegram.org/bot344519590:AAH1Gzn260TvJRHclFPBGW8S1mmBPNJW8Gw/getUpdates

#@app.route('/<token>', methods=['POST'])
##Day2##
from datetime import datetime
import time,datetime
##Day2##
import serial
import sys
from telegram.ext import Updater  
from telegram.ext import CommandHandler

#name = input('請輸入你的名稱：')
#print('歡迎 ', name)
#設定時間戳記&格式化日期
DD=time.strftime("%Y-%m-%d--%H:%M:%S")
DT=time.strftime("%Y-%m-%d--%H:%M:%S") 

print(DT)
print(DD)

ser = serial.Serial('/dev/ttyACM1', 9600)#arduino板01
#ser = serial.Serial('/dev/ttyAMA0', 9600)#arduino板01
data = ser.readline()
print (data)  
print ("Good bye!")

#token 輸入 bot father 給你的 bot 專屬 token key
updater = Updater(token='344519590:AAH1Gzn260TvJRHclFPBGW8S1mmBPNJW8Gw');  
dispatcher = updater.dispatcher

#start 方法
def start(bot, update):  
    bot.sendMessage(chat_id=update.message.chat_id, text="安安你好我是大六")
    bot.sendMessage(chat_id=update.message.chat_id, text="很高興認識你")

def info(bot, update):  
    bot.sendMessage(chat_id=update.message.chat_id, text="作者:sddivid")
    bot.sendMessage(chat_id=update.message.chat_id, text="GitHub:才不告訴你")
def teacher(bot, update):  
    bot.sendMessage(chat_id=update.message.chat_id, text="老師好")
    bot.sendMessage(chat_id=update.message.chat_id, text="請問如何稱呼")
    name = input('請輸入你的答案：')
    print('日安 ', name ,'老師 ')

def professor(bot, update):  
    bot.sendMessage(chat_id=update.message.chat_id, text="教授好")
    bot.sendMessage(chat_id=update.message.chat_id, text="請問如何稱呼")
    name = input('請輸入你的答案：')
    print('日安 ', name ,'教授 ')
    bot.sendMessage(chat_id=update.message.chat_id, text=name)

def stu(bot, update):  
    bot.sendMessage(chat_id=update.message.chat_id, text="...")
    bot.sendMessage(chat_id=update.message.chat_id, text="...喔")

def talk(bot, update):  
    bot.sendMessage(chat_id=update.message.chat_id, text="最近如何")
    bot.sendMessage(chat_id=update.message.chat_id, text="天氣真好")

def aboutme(bot, update):  
    bot.sendMessage(chat_id=update.message.chat_id, text="個人簡歷")
    bot.sendMessage(chat_id=update.message.chat_id, text="由於個資法保護")
    bot.sendMessage(chat_id=update.message.chat_id, text="但我還是偷偷告訴你")

def server(bot, update):  
    bot.sendMessage(chat_id=update.message.chat_id, text="溫度A")
    bot.sendMessage(chat_id=update.message.chat_id, text="濕度A")
    name = input('請輸入你的答案：')
    print('歡迎 ', name )
    bot.sendMessage(chat_id=update.message.chat_id, text=name)


def order(bot, update):  
    bot.sendMessage(chat_id=update.message.chat_id, text="OAO")
    bot.sendMessage(chat_id=update.message.chat_id, text="TAT")
    CCCFFF = ser
    print('87喔', CCCFFF)
    bot.sendMessage(chat_id=update.message.chat_id, text=CCCFFF)




#第一個參數是接受的指令 `\start` 的字串。
start_handler = CommandHandler('start',start)
#第2個參數是接受的指令 `\info` 的字串。
info_handler = CommandHandler('info',info)
#第3參數是接受的指令 `\info` 的字串。
teacher_handler = CommandHandler('teacher',teacher)
#第4參數是接受的指令 `\info` 的字串。
professor_handler = CommandHandler('professor',professor)
#第5參數是接受的指令 `\info` 的字串。
stu_handler = CommandHandler('stu',stu)
#第6參數是接受的指令 `\info` 的字串。
talk_handler = CommandHandler('talk',talk)
#第7參數是接受的指令 `\info` 的字串。
aboutme_handler = CommandHandler('aboutme',aboutme)
#第8參數是接受的指令 `\info` 的字串。
server_handler = CommandHandler('server',server)
#第9參數是接受的指令 `\info` 的字串。
order_handler = CommandHandler('order',order)

#告訴 api 增加一個新的指令處理方法 (註冊)
dispatcher.add_handler(start_handler)
#告訴 api 增加2個新的指令處理方法 (註冊)
dispatcher.add_handler(info_handler)
#告訴 api 增加3個新的指令處理方法 (老師}
dispatcher.add_handler(teacher_handler)
#告訴 api 增加4個新的指令處理方法 (教授
dispatcher.add_handler(professor_handler)
#告訴 api 增加5個新的指令處理方法 (同學
dispatcher.add_handler(stu_handler)
#告訴 api 增加6個新的指令處理方法 (聊天
dispatcher.add_handler(talk_handler)
#告訴 api 增加7個新的指令處理方法 (關於我
dispatcher.add_handler(aboutme_handler)
#告訴 api 增加8個新的指令處理方法 (server
dispatcher.add_handler(server_handler)
#告訴 api 增加9個新的指令處理方法 (order
dispatcher.add_handler(order_handler)
#進入無限迴圈，也就是開始監聽。
updater.start_polling()  



#########################
##
##一個參數是接受的指令 `\start` 的字串。
#start -1
##第2個參數是接受的指令 `\info` 的字串。
#info -2
##第3參數是接受的指令 `\info` 的字串。
#teacher -3
##第4參數是接受的指令 `\info` 的字串。
#professor -4
##第5參數是接受的指令 `\info` 的字串。
#stu -5
##第6參數是接受的指令 `\info` 的字串。
#talk -6
##第7參數是接受的指令 `\info` 的字串。
#aboutme -7
#########
'''
start - 1A
info - 2A
teacher - 3A
professor - 4A
stu - 5A
talk - 6A
aboutme - 7A
server - 8A
order - 9A

pi@raspberrypi:/etc/workspace/tgbot/mybot1 $ sudo python3 mybot2.py

'''
##########################