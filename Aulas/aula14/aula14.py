num1 = input('Digite um numero: ')
num2 = input('Digite outro numero: ')

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)
else:
    print('Error')



"""
try:
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)

except:
    print("Favor, digite um valor valido")
"""


