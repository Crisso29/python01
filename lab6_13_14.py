punt=int(input("Qué puntuación le das entre 0 a 100?:=>"))
if punt>=90:
    print("A")
elif punt>=80 and punt<90:
    print("B")
elif punt>=70 and punt<80:
    print("C")
elif punt>=60 and punt<70:
    print("D")
elif punt<60:
    print("F")

#14
año = int(input("Por favor, ingresa un año: ")

if año % 4 == 0:
    if año % 100 == 0:
        if año % 400 == 0:
            es_bisiesto = True
        else:
            es_bisiesto = False
    else:
        es_bisiesto = True
else:
    es_bisiesto = False

print(es_bisiesto)