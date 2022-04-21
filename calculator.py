#!/usr/bin/env python3

from tkinter import *
window = Tk()

cal_input = ""
clickHistory = ""
first_num = 0
second_num = 0
calculator_method = None
methodInBracket = None
newParenthese = False

def calculation(cal_method, number1, number2):
    if cal_method == '+':
        number1 = number1 + number2
    elif cal_method == '-':      
        number1 = number1 - number2
    elif cal_method == '*':    
        number1 = number1 * number2
    elif cal_method == '/':       
        number1 = number1 / number2
    return (number1)


def input_key(value):
    global cal_input, clickHistory
    cal_input += value
    clickHistory += value
    print(cal_input)
    cal_input_text.set(clickHistory)

def operator(method):
    global cal_input, first_num, calculator_method, second_num, methodInBracket, clickHistory
    if newParenthese == False:
        print('cal input is', cal_input)
        print("clickHistory is ", clickHistory[-1])
        if (cal_input == "") and ((clickHistory[-1] == '+') or (clickHistory[-1] == '') or (clickHistory[-1] == '*') or (clickHistory[-1] == '/')):
            calculator_method = method
            clickHistory = clickHistory[:-1]
            clickHistory += calculator_method
            cal_input_text.set(clickHistory)
            return
        elif cal_input == "":
            calculator_method = method
            clickHistory += calculator_method
            cal_input_text.set(clickHistory)
            return

        if calculator_method == None:
            calculator_method = method
            first_num = float(cal_input)
            cal_input = ""
        else:
            first_num = calculation(calculator_method, first_num, float(cal_input))
            calculator_method = method
            cal_input = ""
        clickHistory += calculator_method
        cal_input_text.set(clickHistory)
    else:
        if methodInBracket == None:
            methodInBracket = method
            second_num = float(cal_input)
            cal_input = ""
        else:
            second_num = calculation(methodInBracket, second_num, float(cal_input))
            methodInBracket = method
            cal_input = ""
        clickHistory += methodInBracket
        cal_input_text.set(clickHistory)


def openParenthese(parenthese):
    global newParenthese, clickHistory
    clickHistory += parenthese
    cal_input_text.set(clickHistory)
    newParenthese = True

def closeParenthese(parenthese):
    global cal_input, first_num, calculator_method, second_num, methodInBracket, newParenthese,  clickHistory
    clickHistory += parenthese
    cal_input_text.set(clickHistory)
    newParenthese = False
    second_num = calculation(methodInBracket, second_num, float(cal_input))
    first_num = calculation(calculator_method, first_num, second_num)

    second_num = 0
    cal_input = ""
    methodInBracket = None



def equal():
    global cal_input, first_num, calculator_method, second_num, methodInBracket, clickHistory
    if cal_input != "":
        if calculator_method == '+':    
            result = first_num + float(cal_input)
        elif calculator_method == '-':    
            result = first_num - float(cal_input)
        elif calculator_method == '*':    
            result = first_num * float(cal_input)
        elif calculator_method == '/':    
            result = first_num / float(cal_input)
    else:
        result = first_num
    calculator_method = None
    if (result).is_integer():
        result = int(result)
    print(result)
    cal_input = ""
    clickHistory = ""
    cal_input_text.set(clickHistory)
    result_text.set(result)


def clear():
    global cal_input, clickHistory, first_num, calculator_method
    cal_input = ""
    clickHistory = ""
    cal_input_text.set(clickHistory)
    result_text.set("")
    first_num = 0
    calculator_method = None

cal_input_text = StringVar()
Label(window, textvariable=cal_input_text).grid(row=1, columnspan=4)
result_text = StringVar()
Label(window, textvariable=result_text).grid(row=2, columnspan=4)

Button(window, text="Close", command=window.quit).grid(row=0, column=3)
Button(window, text=" 0 ", command=lambda: input_key("0")).grid(row=6, column=0)
Button(window, text=" 1 ", command=lambda: input_key("1")).grid(row=5, column=0)
Button(window, text=" 2 ", command=lambda: input_key("2")).grid(row=5, column=1)
Button(window, text=" 3 ", command=lambda: input_key("3")).grid(row=5, column=2)
Button(window, text=" 4 ", command=lambda: input_key("4")).grid(row=4, column=0)
Button(window, text=" 5 ", command=lambda: input_key("5")).grid(row=4, column=1)
Button(window, text=" 6 ", command=lambda: input_key("6")).grid(row=4, column=2)
Button(window, text=" 7 ", command=lambda: input_key("7")).grid(row=3, column=0)
Button(window, text=" 8 ", command=lambda: input_key("8")).grid(row=3, column=1)
Button(window, text=" 9 ", command=lambda: input_key("9")).grid(row=3, column=2)
Button(window, text=" . ", command=lambda: input_key(".")).grid(row=7, column=0)
Button(window, text=" ( ", command=lambda: openParenthese("(")).grid(row=7, column=1)
Button(window, text=" ) ", command=lambda: closeParenthese(")")).grid(row=7, column=2)
Button(window, text=" + ", command=lambda: operator("+")).grid(row=3, column=3)
Button(window, text=" - ", command=lambda: operator("-")).grid(row=4, column=3)
Button(window, text=" * ", command=lambda: operator("*")).grid(row=5, column=3)
Button(window, text=" / ", command=lambda: operator("/")).grid(row=6, column=3)
Button(window, text=" = ", command=lambda: equal()).grid(row=6, column=2)
Button(window, text=" C ", command=lambda: clear()).grid(row=6, column=1)
window.mainloop()
