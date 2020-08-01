

import random
import vk_api
import datetime
import time
from threading import Timer

token = ''
my_id = '302461117'                          
#LogFile = 'Q:\ServerAAAAAAAAAAAAAAAAAAAAAAAAAA\Log\\'   # Папка с логими
LogFile = ''

favorite_sticker_id = '1048' #ТИМО ЖРЁТ КЕКСИКИ


def tprint(str1, end = ''):
    print('[' + str(datetime.datetime.time(datetime.datetime.now())) + '] ' + str(str1), end)


def write_msg(user_id, message):

    sent = True

    try:
        vk.method('messages.setActivity', {'user_id': user_id,'type': 'typing'})
        time.sleep(float(random.randint(25, 50))/10)
        vk.method('messages.send', {'user_id': user_id,'random_id': random.randint(0, 99999), 'message': message})
        vk.method('messages.send', {'user_id': user_id,'random_id': random.randint(0, 99999), 'sticker_id': favorite_sticker_id})        
    except Exception as e:
        tprint(e)
        sent = False

    return sent



class PAZDRAVLAROR:

    def SDR():
        tprint('Начало поздравлений!')

        token = GetToken()

        Date_Today = str(datetime.date.today())
        Date_Today_Str = str(int(Date_Today[8:10])) + '.' + str(int(Date_Today[5:7]))

        file = LogFile+'BDLog'+str(Date_Today)+'.txt'
        f = open(file, 'a+')
    
        userss = vk.method('friends.get', {'user_id': my_id, 'fields': 'bdate'})['items']
        for user in userss:
            if 'bdate' in user:
                if user['bdate'][0:5] == Date_Today_Str: # or user['id'] == 133890390
                    f.close()
                    f = open(file, 'r+')
                    DONTSEND = 0
                    lines = f.readlines()
                    for line in lines:
                        tempstr = '[' + str(user.user_id) + ']'
                        if tempstr in line:
                            DONTSEND = 1
                            break

                    if DONTSEND == 1:
                        continue


                    if write_msg(user['id'], 'Сдр!'):

                        f = open(file, 'a+')
                        f.write(str(datetime.datetime.time(datetime.datetime.now())) + '\t' + '[' + str(user['id']) + '] ' + str('Поздравлен Сдр!') + '\n')
                        f.close()

                        tprint('  Отправлено' + str(user['id']))

                    else:
                        tprint('  НЕ Отправлено' + str(user['id']))


        
        tprint('Поздравления завершены!')
        

tprint("Server started")

file_path = LogFile + 'token.txt'
f = open(file_path)
token = f.read()
f.close()

vk = vk_api.VkApi(token=token)

PAZDRAVLAROR.SDR()
t1 = Timer(3600.0, PAZDRAVLAROR.SDR)
t1.start()
