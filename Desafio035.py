l1 = int(input('Lado1 = '))
l2 = int(input('Lado2 = '))
l3 = int(input('Lado3 = '))

#Jeito Jean
if (abs(l2-l3)<l1<(l2+l3)):
    if (abs(l1-l3)<l2<(l1+l3)):
        if(abs(l1-l2)<l3<(l2+l1)):
            print('Estes lados formam um triângulo!')
else:
    print('Estes lados não formam um triângulo')

#Jeito Gustavo Guanabara
if l1 < l2+l3 and l2 < l1+l3 and l3 < l1+l2:
    print("Estes lados formam um triângulo")
else:
    print("Estes lados não formam um triângulo")



