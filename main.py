from os import system
while True:
    try:
        from telethon.sync import TelegramClient
        from telethon import errors
        from time import sleep
    except: 
        system("pip install telethon")
    else:
        break
  	

class Spam():
    def __init__(self, api_id, api_hash, timer):
        self.api_id = api_id
        self.api_hash = api_hash
        self.client = TelegramClient('bot_1', self.api_id, self.api_hash)
        self.client.start()
        self.message = self.client.get_messages('me', limit=1)[0].message
        self.mess = input(f'Сообщение: {self.message}\n[y / n] >>> ')
        if (self.mess == 'y') or (self.mess == 'yes'):
            print('Wait 35 minutes...\n')
            sleep(2100)
            self.chat_list = list()
            for dialog in self.client.iter_dialogs():
                if dialog.is_group:
                    self.chat_list.append(dialog)
            while True:
                for dialog in self.chat_list:
                    try:
                        self.client.send_message(dialog, self.message)
                        print(dialog.title, " сообщение отправлено")
                    except errors.FloodWaitError as e:
                        print("Flood wait for ", e)
                    except:
                        pass
                    sleep(5)
                print(f'Wait {timer} minutes...')
                sleep(timer*60)
        else:
            exit()


if __name__ == '__main__':
    api_id = 0 
    api_hash = ''
    time = 0 # указывать в минутах
    Spam(api_id, api_hash, time)
