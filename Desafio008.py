#Escreva um programa que leia um valor em metros e converta em centímetros e milímetro

n = int(input('Digite um valor em metros: '))
cm = n*100
mm = n*1000
print('O valor de {} m equivale a {} cm e {} mm'.format(n, cm, mm))