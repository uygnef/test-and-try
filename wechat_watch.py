import itchat
import sqlite3

def login():
    itchat.auto_login(hotReload=True)
    return itchat

@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def print_content(msg):
    print(msg['Text'])
    # for i in msg:
    #     try:
    #         print(i, msg[i])
    #     except:
    #         pass
    record_message(msg)


def record_message(msg):
    insert_data = [msg['MsgId'], msg['ActualUserName'], msg['ActualNickName'], msg['CreateTime'], msg['Text'], msg['FromUserName']]
    try:
        cursor.execute('INSERT INTO chat VALUES (?, ?, ?, ?, ?, ?)', insert_data)
    except sqlite3.IntegrityError:
        pass
    db.commit()


db = sqlite3.connect('chat_record.db')
cursor = db.cursor()
cursor.execute(
    'create TABLE IF NOT EXISTS chat (id varchar(20) PRIMARY KEY, user_id varchar(66), nick_name varchar(10), time_stamp INTEGER, text varchar(256), group_id varchar(66))')
a = login()
a.run()