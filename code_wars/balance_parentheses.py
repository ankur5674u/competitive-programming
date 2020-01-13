__author__ = "Ankur Prakash Singh"
# Date format "%m-%d-%Y"
__date__ = '01-13-2020'

"""
https://www.codewars.com/kata/52774a314c2333f0a7000688/train/python

Write a function called that takes a string of parentheses, and
determines if the order of the parentheses is valid. 
The function should return true if the string is valid, 
and false if it's invalid.

Along with opening (() and closing ()) parenthesis, 
input may contain any valid ASCII characters. 
Furthermore, the input string may be empty and/or not contain 
any parentheses at all. Do not treat other forms of brackets 
as parentheses (e.g. [], {}, <>).


"""


def is_valid_parentheses(input_p):
    """
    :algorithm
        1. Declare an empty stack.
        2. Push an opening parenthesis on top of the stack.
        3. In case of a closing bracket, check if the stack is empty.
        4. If not, pop in a closing parenthesis if the top of the stack contains the corresponding opening parenthesis.
        5. If the parentheses are valid,​ then the stack will be empty once the input string finishes.
    :param input_p:
    :return: True/False
    """
    # Declaring empty stack
    stack = []
    input_paren_l = ['(', '{', '[']
    closing_paren_l = [')', '}', ']']

    for paren in input_p:
        if paren in input_paren_l:
            stack.append(paren)
        elif paren in closing_paren_l:
            if not stack:
                return False
            else:
                top = stack[-1]
                if paren == ')' and top == '(' or \
                        paren == ']' and top == '[' or \
                        paren == '}' and top == '{':
                    stack.pop()
        else:
            continue
    return True if not stack else False


if __name__ == '__main__':
    is_valid_parentheses("{{}}()[()]")
