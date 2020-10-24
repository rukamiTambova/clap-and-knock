# Чтение вслух
import os
import re
from pygame import mixer
import datetime
import time
from gtts import gTTS
from main import b_feed_func

# Для того чтобы не возникало коллизий при удалении mp3 файлов
# заведем переменную mp3_nameold в которой будем хранить имя предыдущего mp3 файла
mp3_nameold = 'labels.mp3'
mp3_name = "1.mp3"

# Инициализируем звуковое устройство
mixer.init()

# Открываем файл с текстом и по очереди читаем с него строки в ss
f = open("labels.txt", "r")
ss = f.readline()
while ss:
    # Делим прочитанные строки на отдельные предложения
    #split_regex = re.compile(r'[.|!|?|…]')
    split_regex = re.compile(r'[/|!|?]')
    sentences = filter(lambda t: t, [t.strip() for t in split_regex.split(ss)])

    # Перебираем массив с предложениями
    for x in sentences:
        if (x != ""):
            print(x)
            # Эта строка отправляет предложение которое нужно озвучить гуглу
            tts = gTTS(text=x, lang='ru')
            # Получаем от гугла озвученное предложение в виде mp3 файла
            tts.save(mp3_name)
            # Проигрываем полученный mp3 файл
            mixer.music.load(mp3_name)
            mixer.music.play()
            while mixer.music.get_busy():
                time.sleep(0.1)
            # Если предыдущий mp3 файл существует удаляем его
            # чтобы не захламлять папку с приложением кучей mp3 файлов
            if (os.path.exists(mp3_nameold) and (mp3_nameold != "1.mp3")):
                os.remove(mp3_nameold)
            mp3_nameold = mp3_name
            # Формируем имя mp3 файла куда будет сохраняться озвученный текст текущего предложения
            # В качестве имени файла используем текущие дату и время
            now_time = datetime.datetime.now()
            #mp3_name = now_time.strftime("%d%m%Y%I%M%S") + ".mp3"
            mp3_name = 'labels' + ".mp3"

    # Читаем следующую порцию текста из файла
    ss = f.readline()

# Закрываем файл
f.close

# Устанвливаем текущим файлом 1.mp3 и закрываем звуковое устройство
# Это нужно чтобы мы могли удалить предыдущий mp3 файл без колизий
mixer.music.load('1.mp3')
mixer.stop
mixer.quit

# Удаляем последний предыдущий mp3 файл
if (os.path.exists(mp3_nameold)):
    os.remove(mp3_nameold)