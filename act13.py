num1 = int(input("ingrese primer numero"))
num2 = int(input("ingrese segundo numero"))
if num2 != 0:
    sum = num1 + num2
    rest = num1 - num2
    mult = num1 * num2
    div = num1 % num2
print("no se puede dividir entre cero")
print("la suma es",sum,",""la resta es",rest,",""la multiplicacion es",mult,",""la divicion es",div)