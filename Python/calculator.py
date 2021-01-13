import argparse
import math

def addition(numbers):
    result = sum(numbers)
    return result

def subtraction(numbers):
    x = numbers[0]
    y = numbers[1]
    result = x-y
    return result

def division(numbers):
    x = numbers[0]
    y = numbers[1]
    result = x/y
    return result

def multiplication(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

def power(numbers):
    x = numbers[0]
    y = numbers[1]
    result = math.pow(x, y)
    return result

def log(numbers):
    x = numbers[0]
    y = numbers[1]
    result = math.log(x)
    return result

parser = argparse.ArgumentParser(description="Some operations will only calculate using the first and/or second operands.")
parser.add_argument('--add','--addition', action="store_true")
parser.add_argument('--sub','--subtraction', action="store_true")
parser.add_argument('--div','--division', action="store_true")
parser.add_argument('--mult','--multiplication', action="store_true")
parser.add_argument('--pow','--power', action="store_true")
parser.add_argument('--log', action="store_true")

parser.add_argument('--operands', type=int, nargs='+')

args = parser.parse_args()
numbers = args.operands

calculatorFuncs = {
    'add': addition,
    'sub': subtraction,
    'div': division,
    'mult': multiplication,
    'pow': power,
    'log': log
}

for arg in vars(args):
    if getattr(args, arg):
        try: 
            print(f'{arg}: {calculatorFuncs[str(arg)](numbers)}')
        except KeyError:
            pass
