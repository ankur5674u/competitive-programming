__author__ = "Ankur Prakash Singh"
# Date format "%m-%d-%Y"
__date__ = '01-13-2020'


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
    for paren in input_p:
        if paren in input_paren_l:
            stack.append(paren)
        else:
            if not stack:
                return False
            else:
                top = stack[-1]
                if paren == ')' and top == '(' or \
                        paren == ']' and top == '[' or \
                        paren == '}' and top == '{':
                    stack.pop()
    return True if not stack else False


if __name__=='__main__':
    is_valid_parentheses("{{}}()[()]")