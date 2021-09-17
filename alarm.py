import easygui_qt as easy
import time
import datetime


def set_timer(text, local_time):
    local_time = local_time * 60
    time.sleep(local_time)
    easy.show_message(text, title='Напоминалка')


def menu():
    reply = easy.get_yes_or_no('Установить напоминание?', title='Напоминалка')
    while(reply):
        text = easy.get_string('О чем вам напомнить?', title='Напоминалка')
        local_time = easy.get_int("На сколько минут установить таймер?", title='Напоминалка')
        local_time = float(local_time)
        with open('alarm_data.txt', 'a') as data_file:
            data_file.write("{} - {}, через {} мин\n".format(datetime.date.today(),text, local_time))
        set_timer(text, local_time)
        reply = easy.get_yes_or_no('Установить ещё одно напоминание?', title='Напоминалка')


menu()
