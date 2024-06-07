import requests
import os
import json


if not os.path.exists('Downloads'):
    os.makedirs('Downloads')

else:
    print("Se guardaran en el repositorio Downloads")
numpost=input("Ingrese la cantidad de posts(Entre 1 y 100): ")
if numpost.isdecimal():
    numpost=int(numpost)
    if numpost >= 1 and numpost <= 100:
        print(f"Creando {numpost} posts...")
        for i in range(1, int(numpost)+1):
                response = requests.get('https://jsonplaceholder.typicode.com/posts')
                data = response.json()
    else:
        print("El numero ingresado debe ser entre 1 y 100")
else:
    print("Deberias ingresar un numero")

diccprimo={}
diccnoprimo={}
def IsPrime():
    x=0
    for i in range(int(numpost)):
        num=data[i]['id']
        if num > 1:
            for i in range(1,num):
                if (num % i) == 0:
                    diccnoprimo[num]="No es primo"
                    with open(f'Downloads/dl{x+1}NotPrimes.json','w') as f:
                        json.dump(diccnoprimo, f)
                    print("Se crearon los posts no primos")
                elif (num%2)!=0 and (num%i)!=0:
                    diccprimo[num]="Es primo"
                    with open(f'Downloads/dl{x+1}Primes.json', 'w') as f:
                        json.dump(diccprimo, f)
                    print("Se crearon los posts primos")
IsPrime()