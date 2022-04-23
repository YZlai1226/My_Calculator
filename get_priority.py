from dataclasses import asdict
import re

class Rpn:

    def __init__(self):
        self.priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        self.operands = "+-*/^"
        self.operands = [self.operands[i:i+1] for i in range(0, len(self.operands), 1)]
        self.my_expression_list = []
        self.my_operands_list = []
        self.my_postfix_list = []
        self.answer = None

    # def add_space(self, cal_input):
    #     cal_input = ''.join(('{}'.format(el) if el in '+-*/()' else el for el in cal_input))
    #     self.my_expression_list = cal_input.split(' ')
    #     return self.my_expression_list

    def get_priority(self, operand):
        return self.priority[operand]

    def has_more_priority(self, operand1, operand2):
        return self.get_priority(operand1) >= self.get_priority(operand2) ## > or >= ?

    """
    First big function to convert infix to postfix.
    This function works by taking ...
    """
    def postfix_conversion(self, expression):
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
        print(f'{self.my_postfix_list}')

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
        print(f' in final evaluation function {postfix}')
        # for element in postfix:
        #     if self.is_operand(element):
        #         index = postfix.index(element)
        #         print(f'index is {index}')
        while len(postfix) > 1:
            postfix = self.run_whole_list(postfix)
            print(f' in final 2222 evaluation function {postfix}')
        return postfix

## returns True if the next 3 characters are an expression
    def is_expression(self, partial_list):
        char1 = partial_list[0]
        char2 = partial_list[1]
        char3 = partial_list[2]
        if (self.is_operand(char3)) and (self.is_operand(partial_list[0]) == False) and (self.is_operand(partial_list[1]) == False):
            return True
        return False

    def calculate(self, number1, number2, operand):
        if operand == '+':
            self.answer = int(number1) + int(number2)
        elif operand == '-':      
            self.answer = int(number1) - int(number2)
        elif operand == '*':    
            self.answer = int(number1) * int(number2)
        elif operand == '/':       
            self.answer = int(number1) / int(number2)
        elif operand == '^':       
            self.answer = int(number1) ** int(number2)

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



string = '-1+12*3*((2^3+3)*4)-5'
# string = '-1+12+3.3*((2^3+3-2+3^(4.5--2))*4)-(5)'

my_calculator = Rpn()
# print(my_calculator.get_priority('+'))
# print(my_calculator.get_priority('^'))

# operands = ['(', '+', '*']
# postfix = ['5', '2', '1']
# print(f'1. operands: {operands}')
# print(f'1. postfix: {postfix}')
# my_calculator.pop_until_close_parenthesis(operands, postfix)
# my_calculator.pop_until_equal_or_higher_priority('-')
my_calculator.postfix_conversion(string)
print('======', my_calculator.my_postfix_list)
my_list = ['1', '3', '+', '2', '+']
my_calculator.postfix_evaluation(my_calculator.my_postfix_list)
# print(my_calculator.run_whole_list(my_list))
# print(f'2. operands: {my_calculator.my_operands_list}')
# print(f'2. postfix: {my_calculator.my_postfix_list}')

# postfix_expression = my_calculator.postfix_conversion("USERASDASDASDASD")
# answer = my_calculator.postfix_evaluation(postfix_expression)

'1+2*3*((2^2+3)*4)-5'
'123*23+4**+5-'
