import random
#Úkol č1
# pole s čísly od 0 do 100
numbers = list(range(101))

# zamíchání čísel
random.shuffle(numbers)

# Výběr prvních 9 čísel
random_numbers = numbers[:9]

print(random_numbers)


#Úkol č2

# první prostřední poslední hodnota
Prvni_hodnota = random_numbers[0]  # První hodnota
Prostredni_hodnota = random_numbers[4]  # Prostřední hodnota (index 4 pro 9 čísel)
Posledni_hodnota = random_numbers[8]    # Poslední hodnota

print("První hodnota:", Prvni_hodnota)
print("Prostřední hodnota:", Prostredni_hodnota)
print("Poslední hodnota:", Posledni_hodnota)

#Úkol č3

#Změna hodnoty na indexu 5 na 34
random_numbers[5] = 34
#Výpis nového pole
print("Nové pole:", random_numbers)

#Úkol č4

#Vypiště indexove 7 hodnotu z pole
seventh_value = random_numbers[7]
#Vypisuje 7 hodnotu z pole
print("Hodnota na 7 indexovém místě:", seventh_value)

#Úkol č5

length_of_array = len(random_numbers)
print("Délka pole:", length_of_array)

#Úkol č6

#minimální a maximální hodnoty 
min_value = min(random_numbers)
max_value = max(random_numbers)
print("Minimální hodnota", min_value)
print("Maximální hodnota", max_value)

#Úkol č7

#2 pole
pole2 = [1, 2, 3, 4, 5]
#2 pole s jakýmkoliv  čísly a náhodnou délkou
delka = random.randint(5, 15)  # náhodná délka mezi 5 a 15
pole2 = [random.randint(-100, 100) for _ in range(delka)]
print("Druhé pole:", pole2)

#Úkol č8

soucet = sum(pole2) #secteme vsechny hodnoty v poli
print("Součet čísel je:", soucet)

#Úkol č9

# Sečteme první a pátou hodnotu 
if len(pole2) >= 5:
    soucet = pole2[0] + pole2[4]
    print("Pole:", pole2)
    print("Součet první a páté hodnoty je:", soucet)
else:          
    print("Pole má méně než 5 prvků, nelze sečíst první a pátou hodnotu.") # je li méně než 5 polí, vypíše se tenhle kód