import amanobot
from threading import Thread, Timer
import time
from antiflood_config import token, settings

data = []  # stores data


def delMsg(chat_id, msg_id):
    return bot.deleteMessage((chat_id, msg_id))


def antiflood(user_id, chat_id, username):
    counter = 0
    # stores all the message ids to be deleted
    msg_ids = []
    for idx, item in enumerate(data):
        combined = chat_id + ":" + user_id
        if combined in item:
            msg_id = data[idx].split(":")[2]
            # appends the message id to the msg_ids list
            msg_ids.append(msg_id)
            # increases counter by 1
            counter += 1
    if counter >= settings['antiflood_max_msgs']:
        data.clear()
        bot.kickChatMember(chat_id, user_id)
        print("[!] " + username + " banned from " + str(chat_id))
        bot.sendMessage(chat_id, f'Ho cacciato {username} dal gruppo!')
        for msg in msg_ids:
            # starts a thread for each message id to be deleted
            Thread(target=delMsg, args=(chat_id, int(msg),), ).start()
    elif counter < settings['antiflood_max_msgs']:
        data.clear()


def on_message(msg):
    content_type, chat_type, chat_id = amanobot.glance(msg)
    # main function to be used
    if content_type == 'text':
        if "new_chat_members" not in msg and "left_chat_member" not in msg and (
                msg['chat']['type'] == "supergroup" or msg['chat']['type'] == "group"):
            string_to_append = str(msg['chat']['id']) + ":" + str(msg['from']['id']) + ":" + str(msg['message_id'])
            data.append(string_to_append)
            Timer(settings['antiflood_seconds'], antiflood,
                  [str(msg['from']['id']), str(msg['chat']['id']), str(msg['from']['first_name'])]).start()

        elif 'new_chat_members' in msg and (msg['chat']['type'] == 'group' or msg['chat']['type'] == 'supergroup'):
            if msg['new_chat_members'][0]['is_bot'] and msg['new_chat_members'][0]['id'] != bot.getMe()['id']:
                # We check if it's a bot AND if it's not THIS instance of the bot
                bot.kickChatMember(msg['chat']['id'], msg['new_chat_members'][0]['id'])


def main(msg):
    # starts thread for main function
    t = Thread(target=on_message, args=(msg,), )
    t.start()


if __name__ == '__main__':
    # defines amanobot client
    bot = amanobot.Bot(token)
    # loops the threaded main function
    bot.message_loop(main)

    while 1:
        # used for receiving updates repeatedly
        time.sleep(10)
