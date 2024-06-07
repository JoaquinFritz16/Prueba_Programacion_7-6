import requests
import json
word_key=input("Ingrese la palabra a filtrar: ")
n_words=input("Ingrese la cantidad de veces que se van a buscar esa palabra: ")
count=0
if n_words.isdecimal():
    n_words=int(n_words)
    print(f"Buscando {n_words} en los posts...")
    for i in range(1, int(n_words)+1):
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        data = response.json()
        for post in data:
            if word_key.lower() in post['title']:
                print(f"Post{i}:{post["title"]}")
                count=count+1
                print(f"La palabra se encontró {count} veces en el titulo")
                print(post["title"])
            if word_key.lower() in post['body']:
                print(f"Post{i}:{post["body"]}")
                count=count+1
                print(f"La palabra se encontró {count} veces en el cuerpo")
                print(post["body"])
else:
    print("Deberias haber puesto un numero")