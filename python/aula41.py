# Exercício 42
seg1 = float(input("Digite o primeiro segmento: "))
seg2 = float(input("Digite o segundo segmento: "))
seg3 = float(input("Digite o terceiro segmento: "))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print("Os segmentos acima PODEM FORMAR um triângulo!")
    if seg1 == seg2 == seg3:
        print("Triângulo Equilátero!")
    if seg1 != seg2 != seg3 != seg1:  
        print("Triângulo Escaleno!")
    else:
        print("Triângulo Isósceles!") 
else:
    print("Os segmentos acima NÃO PODEM FORMAR um triângulo!")

