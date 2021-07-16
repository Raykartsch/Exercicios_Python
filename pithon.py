'''Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately, starting with the leftmost digit and skipping any 0s. So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.

Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000
'''

def decoding_roman_numbers(decode_text):
    roman_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M':1000}
    total = cont = 0
    while cont < len(decode_text):  
        value = roman_numbers.get(decode_text[cont])
        if cont < len(decode_text) - 1:
            next_value = roman_numbers.get(decode_text[cont + 1])
        else:
            next_value = 0
        if value < next_value:
            next_value = next_value - value
            total += next_value
            decode_text = decode_text[:cont] + decode_text[cont+2:]
        else:
            total += value      
            cont += 1           
    return total

decoding_roman_numbers('CMLXXXIV')

'''Algoritmo para codificar numero inteiro em romano'''
def encode_roman_number(number):
    pass


'''
A Narcissistic Number is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).

For example, take 153 (3 digits), which is narcisstic:

    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
and 1652 (4 digits), which isn't:

    1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
The Challenge:

Your code must return true or false depending upon whether the given number is a Narcissistic number in base 10.

Error checking for text strings or other invalid inputs is not required, only valid positive non-zero integers will be passed into the function.

'''

def narcissistic_number(num):
    #FAZER COM LIST COMPREHENSION
    total = 0
    num = str(num)
    for i in range(len(num)):
        total += int(num[i])**len(num)

    return True if str(total) == num else False 

print(narcissistic_number(153))


'''
Write a simple parser that will parse and run Deadfish.

Deadfish has 4 commands, each 1 character long:

i increments the value (initially 0)
d decrements the value
s squares the value
o outputs the value into the return array
Invalid characters should be ignored.

parse("iiisdoso")  ==>  [8, 64]

'''

def parse(commands):
    value = 0
    array = []
    for i in range(len(commands)):
        if commands[i] == 'i':
            value += 1
        elif commands[i] == 'd':
            value -= 1
        elif commands[i] == 's':
            value = pow(value, 2)
        elif commands[i]  == 'o':
            array.append(value)
            print(array)
        else:
            continue

parse("oooooo")
#["Good" if i>=4 else "Neutral" if i==3 else "Bad" for i in x]



