#!/usr/bin/env python

# from dataclasses import asdict
# from tkinter import tk
import tkinter as tk
import re

window = tk.Tk()

class Rpn:

    def __init__(self):
        self.priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        self.operands = "+-*/^"
        self.operands = [self.operands[i:i+1] for i in range(0, len(self.operands), 1)]
        self.my_expression_list = []
        self.my_operands_list = []
        self.my_postfix_list = []
        self.click_history = ""
        self.result = 0
        self.answer = None

    # def add_space(self, cal_input):
    #     cal_input = ''.join(('{}'.format(el) if el in '+-*/()' else el for el in cal_input))
    #     self.my_expression_list = cal_input.split(' ')
    #     return self.my_expression_list

    def input_key(self, value):
        print(f'self result is {self.result}')
        if (self.result != 0) and (self.is_operand(value)):
            self.click_history += str(self.result)
            self.result = 0
            print(f'==== click history is {self.click_history}')
        if (len(self.click_history) == 0) and (value in ['*', '/', '+', '^', '(', ')', '.']):
            return
        if (value =='(') and (self.is_operand(self.click_history[-1]) == False):
            return
        if ((value in ['.', ')']) and (self.is_operand(self.click_history[-1]))) or ((value in ['.', ')']) and (self.click_history[-1] == '(')):
            return
        if (len(self.click_history) != 0) and (self.is_operand(self.click_history[-1])) and (self.is_operand(value)):
            self.click_history = self.click_history[:-1]
        print('finish if')
        self.click_history += value
        print(f'+++++ click history is {self.click_history}')
        cal_input_text.set(self.click_history)

    def get_priority(self, operand):
        return self.priority[operand]

    def has_more_priority(self, operand1, operand2):
        return self.get_priority(operand1) >= self.get_priority(operand2) ## > or >= ?

    """
    First big function to convert infix to postfix.
    This function works by taking ...
    """
    def postfix_conversion(self, expression):
        print(f'the input is {expression}')
        if len(expression) != 0:
            expression_start = 0
            if expression[0] in ['+', '-']:
                expression_start = 1
            self.my_expression_list = re.split(r'([\+\-\*\^\(\)/])', expression[expression_start:])
            self.my_expression_list = [element for element in self.my_expression_list if element != '']
            if expression[0] in ['+', '-']:
                self.my_expression_list[0] = expression[0] + self.my_expression_list[0]
            print(f'my expression is {self.my_expression_list}')
            # for expression in self.my_expression_list:
            #     print(f'=> {expression}')
            for element in self.my_expression_list:
                if not (self.is_operand(element) or self.is_parenthesis(element)):
                    ## we have a number
                    self.my_postfix_list.append(element)
                    continue
                if len(self.my_operands_list) == 0:
                    self.my_operands_list.append(element)
                    continue
                if self.is_operand(element) and self.is_operand(self.my_operands_list[-1]):
                    self.pop_until_equal_or_higher_priority(element)
                elif element == '(':
                    self.my_operands_list.append(element)
                elif element == ')':
                    self.pop_until_close_parenthesis()
                else: 
                    self.my_operands_list.append(element) 
            self.my_postfix_list.append(self.my_operands_list.pop())
            print(f'my postfix list is {self.my_postfix_list}')
            print(f'my operands list is {self.my_operands_list}')
            if len(self.my_operands_list) != 0:
                self.my_postfix_list.append(self.my_operands_list[-1])
            print(f'here is my final postfix : {self.my_postfix_list}')

    def is_operand(self, character):
        return character in self.operands

    def is_parenthesis(self, character):
        return character in ['(', ')']

    def pop_until_close_parenthesis(self):
        while self.my_operands_list[-1] != '(':
            self.my_postfix_list.append(self.my_operands_list.pop())
        ## to remove the '('
        self.my_operands_list.pop()

    def pop_until_equal_or_higher_priority(self, character):
        while (len(self.my_operands_list) > 0 and self.my_operands_list[-1] != '(' \
            and self.has_more_priority(self.my_operands_list[-1], character)):
            self.my_postfix_list.append(self.my_operands_list.pop())
        self.my_operands_list.append(character)

    #second big function to get fiinal answer 
    def postfix_evaluation(self, postfix):
        # print(f' in final evaluation function {postfix}')
        # for element in postfix:
        #     if self.is_operand(element):
        #         index = postfix.index(element)
        #         print(f'index is {index}')
        while len(postfix) > 1:
            postfix = self.run_whole_list(postfix)
        postfix[0] = float(postfix[0])
        self.result = self.answer
        if (postfix[0]).is_integer():
            self.result = int(postfix[0])
        print(self.result)
        self.click_history = ""
        cal_input_text.set(self.click_history)
        result_text.set(self.result)
        self.my_expression_list = []
        self.my_operands_list = []
        self.my_postfix_list = []
        self.click_history = ""
        print(f'result text is {result_text}')

## returns True if the next 3 characters are an expression
    def is_expression(self, partial_list):
        char3 = partial_list[2]
        if (self.is_operand(char3)) and (self.is_operand(partial_list[0]) == False) and (self.is_operand(partial_list[1]) == False):
            return True
        return False

    def calculate(self, number1, number2, operand):
        if operand == '+':
            self.answer = float(number1) + float(number2)
        elif operand == '-':      
            self.answer = float(number1) - float(number2)
        elif operand == '*':    
            self.answer = float(number1) * float(number2)
        elif operand == '/':       
            self.answer = float(number1) / float(number2)
        elif operand == '^':       
            self.answer = float(number1) ** float(number2)

    def run_whole_list(self, postfix):
        # for i, elem in enumerate(postfix):
        i = 0
        while i < len(postfix):
            # print(f'i is {i} and elem is {postfix[i]}')
            if i <= (len(postfix) - 3) and self.is_expression(postfix[i:i+3]):
                # print(f'length is {len(postfix) - 3}')
                # print(f'i is {i}')
                number1 = postfix[i]
                number2 = postfix[i + 1]
                operand = postfix[i + 2]
                self.calculate(number1, number2, operand)
                del postfix[i:i+3]
                # print(f'after deleting the list is {postfix}')
                postfix.insert(i, str(self.answer))
                print(f'after inserting the list is {postfix}')
                i -= 1
            i += 1
        return postfix

    def clear(self):
        self.click_history = ''
        cal_input_text.set(self.click_history)
        result_text.set('')
        self.my_expression_list = []
        self.my_operands_list = []
        self.my_postfix_list = []
        self.answer = None

    def delete_char(self):
        self.click_history = self.click_history[:-1]
        cal_input_text.set(self.click_history)
    
    def conversion_and_evaluation(self, input_string, postfix_list):
        print(f'input string is {input_string}')
        input_string_list = [input_string[i:i+1] for i in range(0, len(input_string), 1)]
        print(f'input string  list is {input_string_list}')
        if (len(input_string_list) < 3):
            return
        self.postfix_conversion(input_string)
        self.postfix_evaluation(postfix_list)

my_calculator = Rpn()

cal_input_text = tk.StringVar()
tk.Label(window, textvariable=cal_input_text).grid(row=1, columnspan=4)
result_text = tk.StringVar()
tk.Label(window, textvariable=result_text).grid(row=2, columnspan=4)

tk.Button(window, text="Close", command=window.quit).grid(row=0, column=3)
tk.Button(window, text=" 0 ", command=lambda: my_calculator.input_key("0")).grid(row=6, column=0)
tk.Button(window, text=" 1 ", command=lambda: my_calculator.input_key("1")).grid(row=5, column=0)
tk.Button(window, text=" 2 ", command=lambda: my_calculator.input_key("2")).grid(row=5, column=1)
tk.Button(window, text=" 3 ", command=lambda: my_calculator.input_key("3")).grid(row=5, column=2)
tk.Button(window, text=" 4 ", command=lambda: my_calculator.input_key("4")).grid(row=4, column=0)
tk.Button(window, text=" 5 ", command=lambda: my_calculator.input_key("5")).grid(row=4, column=1)
tk.Button(window, text=" 6 ", command=lambda: my_calculator.input_key("6")).grid(row=4, column=2)
tk.Button(window, text=" 7 ", command=lambda: my_calculator.input_key("7")).grid(row=3, column=0)
tk.Button(window, text=" 8 ", command=lambda: my_calculator.input_key("8")).grid(row=3, column=1)
tk.Button(window, text=" 9 ", command=lambda: my_calculator.input_key("9")).grid(row=3, column=2)
tk.Button(window, text=" . ", command=lambda: my_calculator.input_key(".")).grid(row=7, column=0)
tk.Button(window, text=" ( ", command=lambda: my_calculator.input_key("(")).grid(row=7, column=1)
tk.Button(window, text=" ) ", command=lambda: my_calculator.input_key(")")).grid(row=7, column=2)
tk.Button(window, text=" + ", command=lambda: my_calculator.input_key("+")).grid(row=3, column=3)
tk.Button(window, text=" - ", command=lambda: my_calculator.input_key("-")).grid(row=4, column=3)
tk.Button(window, text=" * ", command=lambda: my_calculator.input_key("*")).grid(row=5, column=3)
tk.Button(window, text=" / ", command=lambda: my_calculator.input_key("/")).grid(row=6, column=3)
tk.Button(window, text=" ^ ", command=lambda: my_calculator.input_key("^")).grid(row=7, column=3)
tk.Button(window, text=" del ", command=lambda: my_calculator.delete_char()).grid(row=7, column=3)
tk.Button(window, text=" = ", command=lambda: my_calculator.conversion_and_evaluation(my_calculator.click_history, my_calculator.my_postfix_list)).grid(row=6, column=2)
tk.Button(window, text=" C ", command=lambda: my_calculator.clear()).grid(row=6, column=1)
window.title("myCalculator")
window.resizable(False, False)
window.mainloop()

