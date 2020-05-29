import os
import re
import json
import logging


def calculator(a, b, operator):
    """
    Do the simple expression like sum, subtraction, divide and multiply
    with the given operands a, b and operator.
    :param a: Operand a.
    :param b: Operand b.
    :param operator: Operator.
    :return: Result.
    """
    if operator == '+':
        val = a + b
    elif operator == '-':
        val = a - b
    elif operator == '*':
        val = a * b
    elif operator == '/':
        val = a / b
    return val

def eval_postfix(postfix, data):
    """
    Evaluate Postfix expression to store formula and calculate.
    :param postfix: A postfix expression builded from build_postfix function.
    :return: Result.
    """
    queue = []
    for element in postfix:
        if isinstance(element, float) or isinstance(element, int):
            queue.append(element)
        else:
            if element.startswith('('):
                # Extract the leftmost and rightmost parentheses
                parentheses_extractor = "(^\(|\)$)"
                element = re.sub(parentheses_extractor, '', element)
                # Build postfix for the parentheses expression and calculate it
                number = build_postfix(element, data)
                val = eval_postfix(number, data)

                queue.append(val)
            else:
                a = queue.pop(0)
                b = queue.pop(0)

                val = calculator(a, b, element)

                queue.insert(0, val)

    return queue.pop()

def build_postfix(formula, data):
    """
    Build a postfix expression from formula and data.
    :param formula: User input formula.
    :param data: System data variables use to transform the operand.
    :return: A postfix expression.
    """
    operator_extractor = "[\+\-\*\/]"
    operand_extractor = "(\d+\.\d+|\w+|\(+.*?\)+)"

    operands = re.findall(operand_extractor, formula)

    # Remove the expression inside the parentheses from formula
    operators = re.sub("(\(.*?\))", '', formula)
    # Get the current expression operators
    operators = re.findall(operator_extractor, operators)

    # Check if the user input the right formula format
    assert len(operators) < len(operands), 'Wrong formula!'

    # Build list operand contain all the numbers (integer, float)
    operand_list = []
    for operand in operands:
        if data.get(operand):
            operand_list.append(data[operand])
        elif operand.startswith('('):
            operand_list.append(operand)
        else:
            operand_list.append(float(operand))

    postfix = operand_list + operators
    return postfix

def run(formula, data):
    postfix = build_postfix(formula, data)
    res = eval_postfix(postfix, data)
    return res

if __name__ == '__main__':
    formula = input('Enter the formula: ')
    file_name = input('Enter the file name: ')

    try:
        # Read the json data file from the current directory
        # and convert it to dictionary
        with open(os.getcwd() + '/' + file_name, 'r') as f:
            data = json.load(f)
        f.close()

        res = run(formula, data)
        print(res)
    except IOError as e:
        logging.error(e)
