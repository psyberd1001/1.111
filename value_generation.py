import tkinter as tk
import random
from tkinter import *

def generate_random_number():
    return random.randint(200,1000)


def hMeter(c, nowValue, x, y, widgLen, widgHigh, maxValue, outerColor, nameValue):
    if (nowValue > maxValue): nowValue = maxValue - 1
    devValue = float(widgLen) / float(maxValue)
    mesureValue = devValue * nowValue
    c.create_rectangle(1, 1, widgLen, widgHigh, fill='black', outline=outerColor)
    c.create_rectangle(2, 2, int(mesureValue), widgHigh - 1, fill=outerColor, outline=outerColor)
    c.create_line(1, widgHigh, 1, widgHigh + 5, width=1, fill=outerColor)
    c.create_line(widgLen, widgHigh, widgLen, widgHigh + 5, width=1, fill=outerColor)
    c.create_line(1 + widgLen / 4, widgHigh, 1 + widgLen / 4, widgHigh + 5, width=1, fill=outerColor)
    c.create_line(1 + widgLen / 2, widgHigh, 1 + widgLen / 2, widgHigh + 5, width=1, fill=outerColor)
    c.create_line(1 + widgLen - widgLen / 4, widgHigh, 1 + widgLen - widgLen / 4, widgHigh + 5, width=1,
                  fill=outerColor)
    c.create_text(0, widgHigh + 10, font="Verdana 10", anchor="w", justify=CENTER, fill='red', text='0')
    c.create_text(widgLen - 10, widgHigh + 10, font="Verdana 10", anchor="w", justify=CENTER, fill='red',
                  text=str(maxValue))
    c.create_text(widgLen / 2 - 10, widgHigh + 10, font="Verdana 10", anchor="w", justify=CENTER, fill='red',
                  text=str(int(maxValue / 2)))
    c.create_text(widgLen / 4 - 10, widgHigh + 10, font="Verdana 10", anchor="w", justify=CENTER, fill='red',
                  text=str(int(maxValue / 4)))
    c.create_text(widgLen - widgLen / 4 - 10, widgHigh + 10, font="Verdana 10", anchor="w", justify=CENTER,
                  fill='red', text=str(int(maxValue - maxValue / 4)))
    c.create_text(widgLen + 20, widgHigh - 8, font="Verdana 12", anchor="w", justify=CENTER, fill=outerColor,
                  text=str(int(nowValue)))
    c.create_text(1, widgHigh + 25, font="Verdana 10", anchor="w", justify=CENTER, fill='white', text=nameValue)



def hMeter1(c, nowValue, x, y, widgLen, widgHigh, maxValue, outerColor, nameValue):
    if (nowValue > maxValue): nowValue = maxValue - 1
    devValue = float(widgLen) / float(maxValue)
    mesureValue = devValue * nowValue
    c.create_rectangle(1, 1, widgLen, widgHigh, fill='black', outline=outerColor)
    c.create_rectangle(2, 2, int(mesureValue), widgHigh - 1, fill=outerColor, outline=outerColor)
    c.create_line(1, widgHigh, 1, widgHigh + 5, width=1, fill=outerColor)
    c.create_line(widgLen, widgHigh, widgLen, widgHigh + 5, width=1, fill=outerColor)
    c.create_line(1 + widgLen / 4, widgHigh, 1 + widgLen / 4, widgHigh + 5, width=1, fill=outerColor)
    c.create_line(1 + widgLen / 2, widgHigh, 1 + widgLen / 2, widgHigh + 5, width=1, fill=outerColor)
    c.create_line(1 + widgLen - widgLen / 4, widgHigh, 1 + widgLen - widgLen / 4, widgHigh + 5, width=1,
                  fill=outerColor)
    c.create_text(0, widgHigh + 10, font="Verdana 10", anchor="w", justify=CENTER, fill='red', text='0')
    c.create_text(widgLen - 10, widgHigh + 10, font="Verdana 10", anchor="w", justify=CENTER, fill='red',
                  text=str(maxValue))
    c.create_text(widgLen / 2 - 10, widgHigh + 10, font="Verdana 10", anchor="w", justify=CENTER, fill='red',
                  text=str(int(maxValue / 2)))
    c.create_text(widgLen / 4 - 10, widgHigh + 10, font="Verdana 10", anchor="w", justify=CENTER, fill='red',
                  text=str(int(maxValue / 4)))
    c.create_text(widgLen - widgLen / 4 - 10, widgHigh + 10, font="Verdana 10", anchor="w", justify=CENTER,
                  fill='red', text=str(int(maxValue - maxValue / 4)))
    c.create_text(widgLen + 20, widgHigh - 8, font="Verdana 12", anchor="w", justify=CENTER, fill=outerColor,
                  text=str(int(nowValue)))
    c.create_text(1, widgHigh + 25, font="Verdana 10", anchor="w", justify=CENTER, fill='white', text=nameValue)



def hMeter2(c, nowValue, x, y, widgLen, widgHigh, maxValue, outerColor, nameValue):
    if (nowValue > maxValue): nowValue = maxValue - 1
    devValue = float(widgLen) / float(maxValue)
    mesureValue = devValue * nowValue
    c.create_rectangle(1, 1, widgLen, widgHigh, fill='black', outline=outerColor)
    c.create_rectangle(2, 2, int(mesureValue), widgHigh - 1, fill=outerColor, outline=outerColor)
    c.create_line(1, widgHigh, 1, widgHigh + 5, width=1, fill=outerColor)
    c.create_line(widgLen, widgHigh, widgLen, widgHigh + 5, width=1, fill=outerColor)
    c.create_line(1 + widgLen / 4, widgHigh, 1 + widgLen / 4, widgHigh + 5, width=1, fill=outerColor)
    c.create_line(1 + widgLen / 2, widgHigh, 1 + widgLen / 2, widgHigh + 5, width=1, fill=outerColor)
    c.create_line(1 + widgLen - widgLen / 4, widgHigh, 1 + widgLen - widgLen / 4, widgHigh + 5, width=1,
                  fill=outerColor)
    c.create_text(0, widgHigh + 10, font="Verdana 10", anchor="w", justify=CENTER, fill='red', text='0')
    c.create_text(widgLen - 10, widgHigh + 10, font="Verdana 10", anchor="w", justify=CENTER, fill='red',
                  text=str(maxValue))
    c.create_text(widgLen / 2 - 10, widgHigh + 10, font="Verdana 10", anchor="w", justify=CENTER, fill='red',
                  text=str(int(maxValue / 2)))
    c.create_text(widgLen / 4 - 10, widgHigh + 10, font="Verdana 10", anchor="w", justify=CENTER, fill='red',
                  text=str(int(maxValue / 4)))
    c.create_text(widgLen - widgLen / 4 - 10, widgHigh + 10, font="Verdana 10", anchor="w", justify=CENTER,
                  fill='red', text=str(int(maxValue - maxValue / 4)))
    c.create_text(widgLen + 20, widgHigh - 8, font="Verdana 12", anchor="w", justify=CENTER, fill=outerColor,
                  text=str(int(nowValue)))
    c.create_text(1, widgHigh + 25, font="Verdana 10", anchor="w", justify=CENTER, fill='white', text=nameValue)


def hMeterC(nowValue, x, y, widgLen, widgHigh, maxValue, outerColor, nameValue):
    c = Canvas(root, width=widgLen + 80, height=widgHigh + 70, bg="black", bd=0, highlightthickness=0, relief='ridge')
    c.place(x=x, y=y)
    return (c, 'hmeter', x, y, widgLen, widgHigh, maxValue, outerColor, nameValue)

def hMeterC1(nowValue, x, y, widgLen, widgHigh, maxValue, outerColor, nameValue):
    c = Canvas(root, width=widgLen + 80, height=widgHigh + 70, bg="black", bd=0, highlightthickness=0, relief='ridge')
    c.place(x=x, y=y)
    return (c, 'hmeter', x, y, widgLen, widgHigh, maxValue, outerColor, nameValue)

def hMeterC2(nowValue, x, y, widgLen, widgHigh, maxValue, outerColor, nameValue):
    c = Canvas(root, width=widgLen + 80, height=widgHigh + 70, bg="black", bd=0, highlightthickness=0, relief='ridge')
    c.place(x=x, y=y)
    return (c, 'hmeter', x, y, widgLen, widgHigh, maxValue, outerColor, nameValue)

def jobMeter():
    global mesureValue
    analogFig[0].delete("all")
    analogFig1[0].delete("all")
    analogFig2[0].delete("all")
    count = random.randint(100, 10000)

    hMeter(analogFig[0], count, analogFig[2], analogFig[3], analogFig[4], analogFig[5], analogFig[6],
           analogFig[7], analogFig[8])
    hMeter(analogFig1[0], count, analogFig1[2], analogFig1[3], analogFig1[4], analogFig1[5], analogFig1[6],
           analogFig1[7], analogFig1[8])
    hMeter(analogFig2[0], count, analogFig2[2], analogFig2[3], analogFig2[4], analogFig2[5], analogFig2[6],
           analogFig2[7], analogFig2[8])

    lenVal = len(mesureValue) + 1
    mesureValue.append(lenVal)
    mesureValue[lenVal - 1] = count
    # lenVal1 = len(mesureValue) + 1
    # mesureValue.append(lenVal1)
    # mesureValue[lenVal1 - 1] = ref1_count[0]

    if(len(mesureValue) == 80):
        mesureValue = None
        mesureValue = []


    root.after(100, jobMeter)


root = Tk()
root.geometry('1700x900')
canv = Canvas(root, width=1900, height=950, bg="black")
canv.place(x=0, y=25)

analogFig = hMeterC(250, 20, 50, 300, 20, 5000, 'red', 'Между регуляторами')
analogFig1 = hMeterC(250, 20, 250, 300, 20, 5000, 'green', 'Между регуляторами')
analogFig2= hMeterC(250, 20, 550, 300, 20, 5000, 'blue', 'Между регуляторами')

global mesureValue
mesureValue = []
root.after(1, jobMeter)
root.mainloop()



