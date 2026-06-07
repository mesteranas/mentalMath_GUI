import random

def number2Equation(level: int, operations: list) -> tuple:
    operation = random.choice(operations)
    num1, num2 = 0, 0
    speech_op = ""
    if level == 1:
        if operation == '+':
            num1 = random.randint(1, 9)
            num2 = random.randint(1, 9)
            result = num1 + num2
            speech_op = "plus"
        elif operation == '-':
            num1 = random.randint(1, 9)
            num2 = random.randint(1, 9)
            if num1 < num2:
                num1, num2 = num2, num1
            result = num1 - num2
            speech_op = "minus"
        elif operation == '*':
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            result = num1 * num2
            speech_op = "times"
            
        elif operation == '/':
            num2 = random.randint(1, 10)
            result = random.randint(1, 10)
            num1 = num2 * result
            speech_op = "divided by"


    elif level == 2:
        if operation == '+':
            num1 = (random.randint(1, 8) * 10) + random.randint(0, 4)
            num2 = random.randint(1, 5)
            result = num1 + num2
            speech_op = "plus"
            
        elif operation == '-':
            ones_digit = random.randint(4, 9)
            num1 = (random.randint(1, 9) * 10) + ones_digit
            num2 = random.randint(1, ones_digit)
            result = num1 - num2
            speech_op = "minus"
            
        elif operation == '*':
            num1 = random.choice([11, 12, 13, 21, 22, 23, 31, 32])
            num2 = random.choice([2, 3])
            result = num1 * num2
            speech_op = "times"
            
        elif operation == '/':
            num2 = random.randint(2, 5)
            result = random.randint(11, 19)
            num1 = num2 * result
            speech_op = "divided by"


    elif level == 3:
        if operation == '+':
            ones_digit_1 = random.randint(5, 9)
            num1 = (random.randint(1, 8) * 10) + ones_digit_1
            num2 = random.randint(10 - ones_digit_1, 9)
            result = num1 + num2
            speech_op = "plus"
            
        elif operation == '-':
            ones_digit_1 = random.randint(0, 5)
            num1 = (random.randint(2, 9) * 10) + ones_digit_1
            num2 = random.randint(ones_digit_1 + 1, 9)
            result = num1 - num2
            speech_op = "minus"
            
        elif operation == '*':
            num1 = random.randint(14, 29)
            num2 = random.randint(4, 7)
            result = num1 * num2
            speech_op = "times"
            
        elif operation == '/':
            num2 = random.randint(4, 8)
            result = random.randint(12, 25)
            num1 = num2 * result
            speech_op = "divided by"


    elif level == 4:
        if operation == '+':
            num1 = random.randint(10, 99)
            num2 = random.randint(10, 99)
            result = num1 + num2
            speech_op = "plus"
            
        elif operation == '-':
            num1 = random.randint(10, 99)
            num2 = random.randint(10, 99)
            if num1 < num2:
                num1, num2 = num2, num1
            result = num1 - num2
            speech_op = "minus"
            
        elif operation == '*':
            num1 = random.randint(11, 75)
            num2 = random.randint(4, 9)
            result = num1 * num2
            speech_op = "times"
            
        elif operation == '/':
            num2 = random.randint(6, 12)
            result = random.randint(12, 40)
            num1 = num2 * result
            speech_op = "divided by"


    elif level == 5:
        if operation == '+':
            num1 = random.randint(100, 999)
            num2 = random.randint(10, 999)
            result = num1 + num2
            speech_op = "plus"
            
        elif operation == '-':
            num1 = random.randint(100, 999)
            num2 = random.randint(10, 999)
            if num1 < num2:
                num1, num2 = num2, num1
            result = num1 - num2
            speech_op = "minus"
            
        elif operation == '*':
            if random.choice([True, False]):
                base = random.randint(11, 25)
                return f"{base} times {base}", base * base
            else:
                num1 = random.randint(12, 15)
                num2 = random.randint(12, 25)
                result = num1 * num2
                speech_op = "times"
            
        elif operation == '/':
            num2 = random.randint(12, 25)
            result = random.randint(15, 50)
            num1 = num2 * result
            speech_op = "divided by"


    equation_str = f"{num1} {speech_op} {num2}"
    return equation_str, result