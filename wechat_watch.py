import itchat
import sqlite3

def login():
    itchat.auto_login(hotReload=True)
    return itchat

@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def print_content(msg):
    if msg['FromUserName'] != "@@8d7a36a183ea7237935d3901440f43537d87e4d35539f8b801f328cefe7df0fd":
        return
    print(msg['Text'])
    record_message(msg)


def record_message(msg):
    insert_data = [msg['MsgId'], msg['ActualUserName'], msg['ActualNickName'], msg['CreateTime']]
    try:
        cursor.execute('INSERT INTO chat VALUES (?, ?, ?, ?)', insert_data)
        db.commit()
    except:
        pass


db = sqlite3.connect('chat_record.db')
cursor = db.cursor()
cursor.execute(
    'create TABLE IF NOT EXISTS chat (id varchar(20) PRIMARY KEY, user_id varchar(66), nick_name varchar(10), time_stamp INTEGER)')
a = login()
a.run()