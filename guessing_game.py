import math # import biblioteki matematycznej
import random #import randomizacji
a = [] #otwarta lista, na której będziemy
a.append(random.randint(1, 99)) #losuje liczbę od 1 do 99 i dodaje je do listy
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
for i in range(10): # otwiera pętle w zakresie 10
    g = int(input("Enter an integer from 1 to 99: ")) #prosi użytkownika o zgadnięcie cyfry o 1 do 99
    while a[i] != g: #otwiera pętle gdzie będzie sprawdzać czy wprowadzona wartość g jest różna od wylosowanej liczby
        if g < a[i]: #jeżeli wprowadzona liczba jest niższa
            print("guess is low") #wyświetla komunikat o zbyt niskim wprowadzeniu
            g = int(input("Enter an integer from 1 to 99: ")) #wyświetla możliwosć salszego wpisywania
        elif g > a[i]: # jeżeli wprowadzona liczba jest wyższa
            print("guess is high") #wyświetla komunikat o zbyt wysokim wprowadzeniu
            g = int(input("Enter an integer from 1 to 99: ")) #wyświetla możliwosć salszego wpisywania
        else: # jeżeli nie jest ani za duże ani za mała 
            break #to zamyka pętle
    print("you guessed it!") # i wyświetla, że zgadł liczbę

b = []
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
for i in range(10):
    g = int(input("Enter an integer from 1 to 49: "))
    while b[i] != g:
        if g < b[i]:
            print("guess is low")
            g = int(input("Enter an integer from 1 to 49: "))
        elif g > b[i]:
            print("guess is high")
            g = int(input("Enter an integer from 1 to 49: "))
        else:
            break
    print("you guessed it!")
