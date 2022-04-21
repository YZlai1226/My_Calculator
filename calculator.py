#!/usr/bin/env python3

from tkinter import *
window = Tk()

cal_input = ""
first_num = 0
second_num = 0
calculator_method = None
methodInBracket = None
openParenthese = False

def input_key(value):
    global cal_input
    cal_input += value
    print(cal_input)
    cal_input_text.set(cal_input)

def operator(method):
    global cal_input, first_num, calculator_method, second_num, methodInBracket
    if openParenthese = False:
        if cal_input == "":
            calculator_method = method
            return
        if calculator_method == None:
            calculator_method = method
            first_num = float(cal_input)
            cal_input = ""
        else:
            if calculator_method == '+':
                first_num = first_num + float(cal_input)
            elif calculator_method == '-':      
                first_num = first_num - float(cal_input)
            elif calculator_method == '*':    
                first_num = first_num * float(cal_input)
            elif calculator_method == '/':       
                first_num = first_num / float(cal_input)
            calculator_method = method
            cal_input = ""
    else:
        if methodInBracket == None:
            methodInBracket = method
            second_num = float(cal_input)
            cal_input = ""
        else:
            if methodInBracket == '+':  
                second_num = second_num + float(cal_input)
            elif methodInBracket == '-':       
                second_num = second_num - float(cal_input)
            elif methodInBracket == '*':      
                second_num = first_second_numum * float(cal_input)
            elif methodInBracket == '/':      
                second_num = second_num / float(cal_input)
            methodInBracket = method
            cal_input = ""


def openParenthese(parenthese):
    global openParenthese
    openParenthese = True

def closeParenthese(parenthese):
    global cal_input, first_num, calculator_method, second_num, methodInBracket, openParenthese
    openParenthese = False
    if methodInBracket == '+':    
        second_num = second_num + float(cal_input)
    elif methodInBracket == '-':    
        second_num = second_num - float(cal_input)
    elif methodInBracket == '*':    
        second_num = second_num * float(cal_input)
    elif methodInBracket == '/':    
        second_num = second_num / float(cal_input)

    if calculator_method == '+':
        first_num = first_num + second_num
    elif calculator_method == '-':      
        first_num = first_num - second_num
    elif calculator_method == '*':    
        first_num = first_num * second_num
    elif calculator_method == '/':       
        first_num = first_num / second_num

    second_num = 0
    cal_input = ""
    methodInBracket = None



def equal():
    global cal_input, first_num, calculator_method
    if cal_input == "":
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
    cal_input_text.set(cal_input)
    result_text.set(result)


def clear():
    global cal_input
    cal_input = ""
    cal_input_text.set(cal_input)
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
Button(window, text=" ( ", command=lambda: input_key("(")).grid(row=7, column=1)
Button(window, text=" ) ", command=lambda: input_key(")")).grid(row=7, column=2)
Button(window, text=" + ", command=lambda: operator("+")).grid(row=3, column=3)
Button(window, text=" - ", command=lambda: operator("-")).grid(row=4, column=3)
Button(window, text=" * ", command=lambda: operator("*")).grid(row=5, column=3)
Button(window, text=" / ", command=lambda: operator("/")).grid(row=6, column=3)
Button(window, text=" = ", command=lambda: equal()).grid(row=6, column=2)
Button(window, text=" C ", command=lambda: clear()).grid(row=6, column=1)
window.mainloop()
