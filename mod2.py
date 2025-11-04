from pyexpat.errors import messages
from typing import Any

import time
import tkinter
from tkinter import *
import random
import math
import pymodbus
from pandas.io.sas.sas_constants import column_label_length_length
from pymodbus.client import ModbusSerialClient as ModbusClient
from requests import delete
from PIL import Image, ImageTk



client = ModbusClient(framer='rtu', port='/dev/ttyUSB0', parity='N', baudrate=115200, bytesize=8, stopbits=1,
                      timeout=1)

result = client.connect()

# client.write_register(address=4650, value=6000, slave=5)
# client.write_register(address=4654, value=2500, slave=5)
# client.write_register(address=4658, value=2500, slave=5)
# client.write_register(address=4662, value=1600, slave=5)

def mod_bus():

    if result == True:
        print(f'Ура, получилось подключиться! {result}')
        write_reg = client.write_register(address=0, value=3, slave=4)
        print('zapisi')
        time.sleep(0.5)
        read_reg = client.read_holding_registers(address=1, count=1, slave=4)
        print('prochitali')
        resultat = read_reg.registers
        print(resultat)
    client.close()


def hMeter(c, nowValue, x, y, widgLen, widgHigh, maxValue, outerColor, nameValue):
    if (nowValue > maxValue): nowValue = maxValue - 1
    devValue = float(widgLen) / float(maxValue)
    mesureValue = devValue * nowValue
    # c.create_rectangle(1, 1, widgLen, widgHigh, fill='black', outline=outerColor)
    # c.create_rectangle(2, 2, int(mesureValue), widgHigh - 1, fill=outerColor, outline=outerColor)
    # c.create_line(1, widgHigh, 1, widgHigh + 5, width=1, fill=outerColor)
    # c.create_line(widgLen, widgHigh, widgLen, widgHigh + 5, width=1, fill=outerColor)
    # c.create_line(1 + widgLen / 4, widgHigh, 1 + widgLen / 4, widgHigh + 5, width=1, fill=outerColor)
    # c.create_line(1 + widgLen / 2, widgHigh, 1 + widgLen / 2, widgHigh + 5, width=1, fill=outerColor)
    # c.create_line(1 + widgLen - widgLen / 4, widgHigh, 1 + widgLen - widgLen / 4, widgHigh + 5, width=1,
    #               fill=outerColor)
    # c.create_text(0, widgHigh + 10, font="Verdana 10", anchor="w", justify=CENTER, fill=outerColor, text='0')
    # c.create_text(widgLen - 10, widgHigh + 10, font="Verdana 10", anchor="w", justify=CENTER, fill=outerColor,
    #               text=str(maxValue))
    # c.create_text(widgLen / 2 - 10, widgHigh + 10, font="Verdana 10", anchor="w", justify=CENTER, fill=outerColor,
    #               text=str(int(maxValue / 2)))
    # c.create_text(widgLen / 4 - 10, widgHigh + 10, font="Verdana 10", anchor="w", justify=CENTER, fill=outerColor,
    #               text=str(int(maxValue / 4)))
    # c.create_text(widgLen - widgLen / 4 - 10, widgHigh + 10, font="Verdana 10", anchor="w", justify=CENTER,
    #               fill=outerColor, text=str(int(maxValue - maxValue / 4)))
    c.create_text(widgLen - 40, widgHigh + 20, font="Verdana 40", anchor="center", justify=CENTER, fill=outerColor,
                  text=str(int(nowValue)))
    c.create_text(1, widgHigh + 25, font="Verdana 15", anchor="w", justify=CENTER, fill='white', text=nameValue)



def hMeterC(nowValue, x, y, widgLen, widgHigh, maxValue, outerColor, nameValue):
    c = Canvas(root, width=widgLen + 70, height=widgHigh + 50, bg="grey", bd=0, highlightthickness=0, relief='ridge')
    c.place(x=x, y=y)
    return (c, 'hmeter', x, y, widgLen, widgHigh, maxValue, outerColor, nameValue)


def vMeterC(nowValue, x, y, widgLen, widgHigh, maxValue, outerColor, nameValue):
    c = Canvas(root, width=widgLen + 50, height=widgHigh + 40, bg="black", bd=0, highlightthickness=0, relief='ridge')
    c.place(x=x, y=y)
    return (c, 'vmeter', x, y, widgLen, widgHigh, maxValue, outerColor, nameValue)


def vMeter(c, nowValue, x, y, widgLen, widgHigh, maxValue, outerColor, nameValue):
    if (nowValue > maxValue): nowValue = maxValue - 1
    devValue = float(widgHigh) / float(maxValue)
    mesureValue = devValue * nowValue
    c.create_rectangle(1, 1, widgLen, widgHigh, fill='black', outline=outerColor)
    c.create_rectangle(widgLen - 1, widgHigh, 2, widgHigh - int(mesureValue), fill=outerColor, outline=outerColor)
    c.create_line(widgLen, widgHigh, widgLen + 10, widgHigh, width=1, fill=outerColor)
    c.create_line(widgLen, widgHigh / 4, widgLen + 10, widgHigh / 4, width=1, fill=outerColor)
    c.create_line(widgLen, widgHigh / 2, widgLen + 10, widgHigh / 2, width=1, fill=outerColor)
    c.create_line(widgLen, widgHigh - widgHigh / 4, widgLen + 10, widgHigh - widgHigh / 4, width=1, fill=outerColor)
    c.create_line(widgLen, 1, widgLen + 10, 1, width=1, fill=outerColor)
    c.create_line(widgLen + 10, widgHigh, widgLen + 10, widgHigh, width=1, fill=outerColor)
    c.create_text(widgLen + 12, widgHigh, font="Verdana 10", anchor="w", justify=CENTER, fill=outerColor, text='0')
    c.create_text(widgLen + 12, 10, font="Verdana 10", anchor="w", justify=CENTER, fill=outerColor, text=str(maxValue))
    c.create_text(widgLen + 12, widgHigh / 2, font="Verdana 10", anchor="w", justify=CENTER, fill=outerColor,
                  text=str(maxValue / 2))
    c.create_text(widgLen + 12, widgHigh - widgHigh / 4, font="Verdana 10", anchor="w", justify=CENTER, fill=outerColor,
                  text=str(maxValue / 4))
    c.create_text(widgLen + 12, widgHigh / 4, font="Verdana 10", anchor="w", justify=CENTER, fill=outerColor,
                  text=str(maxValue - maxValue / 4))
    c.create_text(2, widgHigh + 15, font="Verdana 12", anchor="w", justify=CENTER, fill=outerColor, text=str(nowValue))

def aMeterC(nowValue, x, y, widgLen, widgHigh, maxValue, outerColor, nameValue):
        c = Canvas(root, width=widgLen, height=widgHigh, bg="black", bd=0, highlightthickness=0, relief='ridge')
        c.place(x=x, y=y)
        return (c, 'ameter', x, y, widgLen, widgHigh, maxValue, outerColor, nameValue)


def aMeter(c, nowValue, x, y, widgLen, widgHigh, maxValue, outerColor, nameValue):
    if (nowValue > maxValue): nowValue = maxValue - 1
    devValue = float(180) / float(maxValue)
    mesureValue = devValue * nowValue
    x1 = widgLen / 2
    y1 = widgHigh / 2 + 10
    x2 = 10
    y2 = widgHigh / 2 + 10
    angle = math.pi * int(mesureValue) / 180;
    newx = ((x2 - x1) * math.cos(angle) - (y2 - y1) * math.sin(angle)) + x1
    newy = ((x2 - x1) * math.sin(angle) + (y2 - y1) * math.cos(angle)) + y1
    c.create_oval(1, 1, widgLen - 1, widgHigh - 1, width=2, fill='black', outline=outerColor)
    c.create_text(7, y1, font="Verdana 10", anchor="w", justify=CENTER, fill=outerColor, text='0')
    c.create_text(widgLen - 30, y1, font="Verdana 10", anchor="w", justify=CENTER, fill=outerColor, text=str(maxValue))
    c.create_text(widgLen / 2 - 10, 10, font="Verdana 10", anchor="w", justify=CENTER, fill=outerColor,
                  text=str(maxValue / 2))
    c.create_text(widgLen / 8, widgHigh / 4, font="Verdana 10", anchor="w", justify=CENTER, fill=outerColor,
                  text=str(maxValue / 4))
    c.create_text(widgLen / 2 + widgLen / 4, widgHigh / 4, font="Verdana 10", anchor="w", justify=CENTER,
                  fill=outerColor, text=str(maxValue - maxValue / 4))
    c.create_text(widgLen / 2 - 20, widgHigh - 40, font="Verdana 14", anchor="w", justify=CENTER, fill=outerColor,
                  text=str(nowValue))
    c.create_rectangle(0, widgHigh / 2 + 18, widgLen, widgHigh, fill='black', outline='black')
    c.create_text(widgLen / 2 - 60, widgHigh - 70, font="Verdana 50", anchor="w", justify=CENTER, fill=outerColor,
                  text=str(nowValue))
    c.create_text(0, widgHigh + 20, font="Verdana 20", anchor="w", justify=CENTER, fill=outerColor, text=str(nameValue))
    c.create_oval(x1 - 10, y1 - 10, x1 + 10, y1 + 10, fill=outerColor, outline=outerColor)
    c.create_line(x1, y1, newx, newy, width=5, fill=outerColor)


def hTrendC(x, y, widgLen, widgHigh, maxValue, outerColor, nameValue, trendKoef):
    c = Canvas(root, width=widgLen + 50, height=widgHigh + 40, bg="black", bd=0, highlightthickness=0, relief='ridge')
    c.place(x=x, y=y)
    return (c, 'htrend', x, y, widgLen, widgHigh, maxValue, outerColor, nameValue, trendKoef)

def hTrend(arrayData, arrayValue):
    c, markErr, x, y, widgLen, widgHigh, maxValue, outerColor, nameValue, trendKoef = arrayData
    c.create_rectangle(1, 1, widgLen, widgHigh, fill='black', outline=outerColor)
    c.create_line(50, widgHigh / 2, widgLen - 5, widgHigh / 2, width=0.1, fill='white', dash=(4, 2))
    c.create_line(50, widgHigh / 4, widgLen - 5, widgHigh / 4, width=0.1, fill='white', dash=(4, 2))
    c.create_line(50, widgHigh - widgHigh / 4, widgLen - 5, widgHigh - widgHigh / 4, width=0.2, fill='white',
                  dash=(4, 2))
    c.create_text(10, widgHigh - 10, font="Verdana 10", anchor="w", justify=CENTER, fill='white', text=0)
    c.create_text(10, 12, font="Verdana 10", anchor="w", justify=CENTER, fill='white', text=str(maxValue))
    c.create_text(10, widgHigh / 2, font="Verdana 10", anchor="w", justify=CENTER, fill='white',
                  text=str(int(maxValue / 2)))
    c.create_text(10, widgHigh / 4, font="Verdana 10", anchor="w", justify=CENTER, fill='white',
                  text=str(int(maxValue - maxValue / 4)))
    c.create_text(10, widgHigh - widgHigh / 4, font="Verdana 10", anchor="w", justify=CENTER, fill='white',
                  text=str(int(maxValue / 4)))
    c.create_text(1, widgHigh + 25, font="Verdana 10", anchor="w", justify=CENTER, fill='white', text=nameValue)
    c.create_text(widgLen / 10, widgHigh + 10, font="Verdana 10", anchor="w", justify=CENTER, fill='white',
                  text='1')
    c.create_text((widgLen / 10) * 2, widgHigh + 10, font="Verdana 10", anchor="w", justify=CENTER, fill='white',
                  text='2')
    c.create_text((widgLen / 10) * 3, widgHigh + 10, font="Verdana 10", anchor="w", justify=CENTER, fill='white',
                  text='3')
    c.create_text((widgLen / 10) * 4, widgHigh + 10, font="Verdana 10", anchor="w", justify=CENTER, fill='white',
                  text='4')
    c.create_text((widgLen / 10) * 5, widgHigh + 10, font="Verdana 10", anchor="w", justify=CENTER, fill='white',
                  text='5')
    c.create_text((widgLen / 10) * 6, widgHigh + 10, font="Verdana 10", anchor="w", justify=CENTER, fill='white',
                  text='6')
    c.create_text((widgLen / 10) * 7, widgHigh + 10, font="Verdana 10", anchor="w", justify=CENTER, fill='white',
                  text='7')
    c.create_text((widgLen / 10) * 8, widgHigh + 10, font="Verdana 10", anchor="w", justify=CENTER, fill='white',
                  text='8')
    c.create_text((widgLen / 10) * 9, widgHigh + 10, font="Verdana 10", anchor="w", justify=CENTER, fill='white',
                  text='9')
    c.create_text(widgLen - 10, widgHigh + 10, font="Verdana 10", anchor="w", justify=CENTER, fill='white',
                  text='100')

    oldy = widgHigh - float(widgHigh) / float(maxValue) * arrayValue[0] * int(trendKoef)
    oldx = 5
    xval = 0

    for counter in range(0, len(arrayValue)):
        val = arrayValue[counter]
        yval = widgHigh - float(widgHigh) / float(maxValue) * val * int(trendKoef)
        xval += 10
        c.create_line(oldx, oldy, xval, yval, width=1.5, fill='green')

        oldy = yval
        oldx = xval
    mesureValue = arrayValue[len(arrayValue) - 1] * int(trendKoef)
    c.create_line(xval, widgHigh - 10, xval, 0, width=0.5, fill='white')
    c.create_text(xval + 10, yval, font="Verdana 10", anchor="w", justify=CENTER, fill='white',
                  text=str(mesureValue))
    c.create_text(xval + 10, yval + 20, font="Verdana 10", anchor="w", justify=CENTER, fill='white',
                  text=time.strftime('%H:%M:%S'))
counters = 0
counters2 = 0
counters3 = 0
counters4 = 0
counters5 = 0
counters6 = 0
counters7 = 0
counters8 = 0
counters_pz = 0
counters_pz_m = 0

def on_press(event):
    event.widget.start_time = time.time()
    event.widget.config(bg="yellow")  # Цвет при удержании


# Обработчик отпускания
def on_release(event):
    duration = time.time() - event.widget.start_time
    event.widget.config(bg="lightgray")  # Возвращаем исходный цвет
    if duration >= 0.5:
        command_value = 1
    else:
        command_value = 0
    # Можно вывести или использовать длительность
    print(f"Длительность нажатия: {duration:.2f} секунд")

def command_button_1():
    global counters
    counters += 1
    count_tk = entry_tk.get()
    client.write_register(address=12, value=1, slave=4)
    button_1.config(bg='green')
    time.sleep(int(count_tk))
    client.write_register(address=12, value=0, slave=4)
    button_1.config(bg='red')

def command_button_2():
    global counters2
    counters2 += 1
    count_ttk = entry_tk.get()
    client.write_register(address=12, value=2, slave=4)
    button_2.config(bg='green')
    time.sleep(int(count_ttk))
    client.write_register(address=12, value=0, slave=4)
    button_2.config(bg='red')

def command_button_3():
    global counters3
    counters3 += 1
    client.write_register(address=12, value=4, slave=4)
    button_2.config(bg='green')
    time.sleep(int(count_ttk))
    client.write_register(address=12, value=0, slave=4)
    button_2.config(bg='red')

def command_button_4():
    global counters4
    counters4 += 1
    client.write_register(address=12, value=8, slave=4)
    button_2.config(bg='green')
    time.sleep(int(count_ttk))
    client.write_register(address=12, value=0, slave=4)
    button_2.config(bg='red')

def command_button_5():
    global counters5
    counters5 += 1
    if counters5 % 2 == 0:
        client.write_register(address=9, value=0, slave=4)
        client.write_register(address=10, value=10, slave=4)
        time.sleep(1)
        button_5.config(bg='red')
        client.write_register(address=10, value=0, slave=4)
    else:
        client.write_register(address=9, value=1, slave=4)
        client.write_register(address=10, value=10, slave=4)
        time.sleep(1)
        button_5.config(bg='green')
        client.write_register(address=10, value=0, slave=4)

def command_button_pz():
    input_value = entry.get()
    try:
        # Преобразуем введенное значение в число (например, int)
        count = int(input_value)
        # Вызываем функцию записи регистра t1 = a7 - время паузы
        client.write_register(address=6, value=6000, slave=4)
        client.write_register(address=10, value=7, slave=4)
        time.sleep(1)
        client.write_register(address=10, value=0, slave=4)
        # Вызываем функцию записи регистра t2 = a8 - время работы
        client.write_register(address=7, value=2700, slave=4)
        client.write_register(address=10, value=8, slave=4)
        time.sleep(1)
        client.write_register(address=10, value=0, slave=4)
        # Вызываем функцию записи регистра t = a9 - время задержки
        client.write_register(address=8, value=15000, slave=4)
        client.write_register(address=10, value=9, slave=4)
        time.sleep(1)
        client.write_register(address=10, value=0, slave=4)
        # Записываем в регистры значение заданного давления
        client.write_register(address=5, value=count, slave=4)
        client.write_register(address=10, value=6, slave=4)
        time.sleep(1)
        client.write_register(address=10, value=0, slave=4)
        # Записываем в регистры значение минимальной скорости а1
        client.write_register(address=0, value=2, slave=4)
        client.write_register(address=10, value=1, slave=4)
        time.sleep(1)
        client.write_register(address=10, value=0, slave=4)
        # Записываем в регистры значение максимальной скорости а2
        client.write_register(address=1, value=10, slave=4)
        client.write_register(address=10, value=2, slave=4)
        time.sleep(1)
        client.write_register(address=10, value=0, slave=4)
        # Записываем в регистры значение kp
        client.write_register(address=4, value=5, slave=4)
        client.write_register(address=10, value=5, slave=4)
        time.sleep(1)
        client.write_register(address=10, value=0, slave=4)
        # Записываем значение в регистр а10 режим ручной скорости
        client.write_register(address=9, value=10, slave=4)
        client.write_register(address=10, value=10, slave=4)
        time.sleep(1)
        client.write_register(address=10, value=0, slave=4)
        print("Значение успешно записано.")
    except ValueError:
        print("Ошибка: введите числовое значение.")

def command_pusk():
    global counters7
    counters7 += 1
    # client.write_register(address=10, value=1, slave=3)
    client.write_register(address=11, value=1, slave=4)
    # client.write_register(address=11, value=0, slave=3)
    time.sleep(2)
    #client.write_register(address=14, value=0, slave=3)
    button_7.config(bg='red', text='START')
    client.write_register(address=11, value=0, slave=4)

def command_stop():
    global counters8
    counters8 += 1
    client.write_register(address=11, value=2, slave=4)
    time.sleep(2)
    client.write_register(address=11, value=0, slave=4)
    button_8.config(bg='red', text='STOP')

def command_speed_plus():
    global counters_pz
    counters_pz += 1
    counter_pz_p = 1
    pz = client.read_holding_registers(address=0, count=1, slave=4)
    pz_count = pz.registers[0]
    if pz_count < 10:
        button_pz_plus.config(bg='green', text='SPEED PLUS')
    if pz_count <= 10:
        client.write_register(address=0, value=pz_count + counter_pz_p, slave=4)
        client.write_register(address=10, value=1, slave=4)
        time.sleep(1)
        client.write_register(address=10, value=0, slave=4)
    else:
        button_pz_plus.config(bg='red', text='MAXIMUM')

def command_speed_minus():
    global counters_pz_m
    counters_pz_m += 1
    counter_pz_m = 1
    pz1 = client.read_holding_registers(address=0, count=1, slave=4)
    pz1_count = pz1.registers[0]
    if pz1_count <= 10:
        button_pz_minus.config(bg='green', text='MINUS SPEED')
        if pz1_count >= 3:
            client.write_register(address=0, value=pz1_count - counter_pz_m, slave=4)
            client.write_register(address=10, value=1, slave=4)
            time.sleep(1)
            client.write_register(address=10, value=0, slave=4)
        else:
            button_pz_minus.config(bg='red', text='MINIMUM')


def jobMeter():
    global mesureValue
    analogFig[0].delete("all")
    analogFig1[0].delete("all")
    analogFig2[0].delete("all")
    analogVertical[0].delete("all")


    ref = client.read_holding_registers(address=0, count=1, slave=4)
    ref_count = ref.registers
    ref1 = client.read_holding_registers(address=1, count=1, slave=4)
    ref1_count = ref1.registers
    ref2 = client.read_holding_registers(address=2, count=1, slave=4)
    ref2_count = ref2.registers
    ref3 = client.read_holding_registers(address=3, count=1, slave=4)
    ref3_count = ref3.registers
    ref4 = client.read_holding_registers(address=5, count=1, slave=4)
    ref4_count = ref4.registers
    counter = random.randint(1000, 10000)

    if (800 <= ref4_count[0] - ref2_count[0]*10 < 200) and (800 <= ref2_count[0]*10 >= 900):
        client.write_register(address=1, value=6, slave=4)
        client.write_register(address=10, value=2, slave=4)
        client.write_register(address=10, value=0, slave=4)

    elif (ref2_count[0]*10 - ref4_count[0] < 100) and (900 <= ref2_count[0]*10 >= 1000) and (ref2_count[0]*10 > 900):
        client.write_register(address=1, value=8, slave=4)
        client.write_register(address=10, value=2, slave=4)
        client.write_register(address=10, value=0, slave=4)

    elif (ref2_count[0]*10 >= ref4_count[0]) and (1000 < ref2_count[0]*10 > 1100):
        client.write_register(address=1, value=10, slave=4)
        client.write_register(address=10, value=2, slave=4)
        client.write_register(address=10, value=0, slave=4)

    hMeter(analogFig[0], ref4_count[0], analogFig[2], analogFig[3], analogFig[4], analogFig[5], analogFig[6],
           analogFig[7], analogFig[8])
    hMeter(analogFig1[0], ref1_count[0], analogFig1[2], analogFig1[3], analogFig1[4], analogFig1[5], analogFig1[6],
           analogFig1[7], analogFig1[8])
    hMeter(analogFig2[0], ref2_count[0] * 100, analogFig2[2], analogFig2[3], analogFig2[4], analogFig2[5], analogFig2[6],
           analogFig2[7], analogFig2[8])
    aMeter(analogVertical[0], ref3_count[0] * 100, analogVertical[2], analogVertical[3], analogVertical[4],
           analogVertical[5], analogVertical[6], analogVertical[7], analogVertical[8])
    # aMeter(analogString[0], count, analogString[2], analogString[3], analogString[4],
    #        analogString[5], analogString[6], analogString[7], analogString[8])
    # with open('result_diag.txt','a') as file:
    #     file.write(f'МЕЖДУ РЕГУЛЯТОРАМИ: {ref_count[0]}, KM1: {ref1_count[0]}, KM2: {ref2_count[0]}, ВЫХОДНОЕ ДАВЛЕНИЕ: {ref3_count[0]} .\n')

    lenVal = len(mesureValue) + 1
    mesureValue.append(lenVal)
    mesureValue[lenVal - 1] = ref3_count[0] * 100
    # lenVal1 = len(mesureValue) + 1
    # mesureValue.append(lenVal1)
    # mesureValue[lenVal1 - 1] = ref1_count[0]
    #trend[0].delete("all")
    #hTrend(trend, mesureValue)

    if (len(mesureValue) == 80):
        mesureValue = None
        mesureValue = []


    root.after(100, jobMeter)


root = Tk()
root.geometry('1700x900')
# bg_image = Image.open("make1.jpg")
# bg_photo = ImageTk.PhotoImage(bg_image)
canv = Canvas(root, width=1800, height=963, bg="blue")
canv.pack()
# canv.create_image(0, 0, image=bg_photo, anchor='nw')

button_1 = tkinter.Button(background='red', command=command_button_1, text='REG 2 Vniz')
button_1.place(x=1500, y=200)
button_1.bind('<ButtonPress-1>', on_press)
button_1.bind('<ButtonRelease-1>', on_release)
button_2 = tkinter.Button(background='red', command=command_button_2, text='REG 2 Vverh')
button_2.place(x=1500, y=250)
button_2.bind('<ButtonPress-1>', on_press)
button_2.bind('<ButtonRelease-1>', on_release)
# button_3 = tkinter.Button(background='red', command=command_button_3, text='REG 1 Vniz')
# button_3.place(x=1500, y=300)
# button_3.bind('<ButtonPress-1>', on_press)
# button_3.bind('<ButtonRelease-1>', on_release)
# button_4 = tkinter.Button(background='red', command=command_button_4, text='REG 1 Vverh')
# button_4.place(x=1500, y=350)
# button_4.bind('<ButtonPress-1>', on_press)
# button_4.bind('<ButtonRelease-1>', on_release)
button_5 = tkinter.Button(background='red', command=command_button_5, text='SPEED')
button_5.place(x=1500, y=400)
button_5.bind('<ButtonPress-1>', on_press)
button_5.bind('<ButtonRelease-1>', on_release)

# label = tkinter.Label(canv, text="Ввод")
# label.place(x=1610, y=450)
label_tk = tkinter.Label(canv, text='Ввод')
label_tk.place(x=1390, y=225)
# Создаем текстовое поле для ввода внутри Canvas
entry = tkinter.Entry(canv, width=6)
entry.place(x=1550, y=450)
entry.focus_set()  # Устанавливаем фокус на поле ввода

entry_tk = tkinter.Entry(canv, width=8)
entry_tk.place(x=1430, y=225)
entry_tk.focus_set()
# button_pod = tkinter.Button(canv, text='Ввод', command=command_button_1)
# button_pod.place(x=1430, y=240)

# Создаем кнопку для подтверждения внутри Canvas
# submit_button = tkinter.Button(canv, text="Ввод", command=command_button_pz)
# submit_button.place(x=1550, y=490)

# Связываем нажатие клавиши Enter с функцией on_submit
root.bind('<Return>', lambda event: command_button_pz())
#root.bind('<Return>', lambda event: command_button_1())

button_6 = tkinter.Button(background='grey', command=command_button_pz, text='PZ')
button_6.place(x=1500, y=450)
button_7 = tkinter.Button(background='white', command=command_pusk, text='START')
button_7.place(x=1500, y=500)
button_8 = tkinter.Button(background='white', command=command_stop, text='STOP')
button_8.place(x=1500, y=550)
button_pz_plus = tkinter.Button(background='grey', command=command_speed_plus, text='PLUS SPEED')
button_pz_plus.place(x=1500, y=100)
button_pz_minus = tkinter.Button(background='grey', command=command_speed_minus, text='MINUS SPEDD')
button_pz_minus.place(x=1500, y=150)


def click_handler(event):
    if event.num == 2:
        print('RIGHT CLICK')


analogFig = hMeterC(250, 20, 50, 400, 20, 20000, 'red', 'PZ')
analogFig1 = hMeterC(250, 20, 200, 400, 20, 20000, 'yellow', 'Vb')
analogFig2 = hMeterC(250, 20, 350, 400, 20, 60000, 'green', 'Dat1')
analogVertical = vMeterC(250, 650, 200, 300, 300, 20000, 'grey', 'ВЫХОДНОЕ ДАВЛЕНИЕ')

def func_create_oval():
    oval = canv.create_oval(0, 0, 100, 100, fill='white')
    return oval


def more_func(event):
    canv.move(analogFig, event.x + 10, event.y + 10)
    #canv.coords(event.x - 50, event.y - 50, event.x + 50, event.y + 50)

canv.bind("<B1-Motion>", more_func)




global mesureValue
mesureValue = []
#trend = hTrendC(850, 28, 800, 400, 5000, 'green', 'ВЫХОДНОЕ', '1')

root.after(1, jobMeter)
root.mainloop()
