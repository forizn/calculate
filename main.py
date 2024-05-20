def main():
    num = input("Enter a number: ")
    result = num.split()
    x = len(result)
    if x == 3:
        num1, num2 = result[0], result[2]
        if num1.isnumeric() and num2.isnumeric():
            num1, num2 = int(num1), int(num2)
            if 1 <= num1 <= 10 and 1 <= num2 <= 10:
                sign = result[1]
                match sign:
                    case '+':
                        print(num1 + num2)
                    case '/':
                        print(num1 // num2)
                    case '*':
                        print(num1 * num2)
                    case '-':
                        print(num1 - num2)
    elif x == 1:
        print('throws Exception //т.к. строка не является математической операцией')
    elif x == 4:
        print('throws Exception ')
    elif x >= 5:
        print('throws Exception //т.к. формат математической операции не удовлетворяет заданию - '
              'два операнда и один оператор (+, -, /, *)')


main()
