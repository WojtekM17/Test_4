pomieszczenia = []
powierzchnia_pomieszczen = []
koszt_materialow_pomieszczenia = []
koszt_robocizny_pomieszczenia = []
suma = 0
i = 0

while True:
    print("Co chcesz zrobić?: ")
    print("1 - Dodaj pomieszczenie")
    print("2 - Wyświetl pomieszczenia")
    print("3 - Oblicz całkowity koszt")
    print("4 - Usuń pomieszczenie")
    print("5 - Wyjście")
    wybor = int(input("Co wybierasz?: "))
    if wybor == 1:
        nazwa_pomieszczenia = str(input("Jak się nazywa to pomieszczenie?: "))
        pomieszczenia.append(nazwa_pomieszczenia)
        powierzchnia = int(input("Ile metrów kwadratowych zajmuje twoje pomieszczenie: "))
        powierzchnia_pomieszczen.append(powierzchnia)
        koszt_materialow = int(input("Ile kosztują materiały?: "))
        koszt_materialow_pomieszczenia.append(koszt_materialow)
        koszt_robocizny = int(input("Ile kosztuje opłacenie robotników?: "))
        koszt_robocizny_pomieszczenia.append(koszt_robocizny)
    if wybor == 2:
        for i in range(len(pomieszczenia)):
            print(f"Pomieszczenie {i + 1} - {pomieszczenia[i]}")
            print(f"Powierzchnia tego pomieszczenia to {powierzchnia_pomieszczen[i]} metrów kwadratowych")
            print(f"Koszt materiałów tego pomieszczenia to {koszt_materialow_pomieszczenia[i]} zł")
            print(f"Koszt robocizny tego pomieszczenia to {koszt_robocizny_pomieszczenia[i]} zł")
        i = 0
    if wybor == 3:
        for i in range(len(pomieszczenia)):
            koszt_robocizny_pomieszczenia[i] += suma
            koszt_materialow_pomieszczenia[i] += suma
        print(f"Całkowity koszt tego projektu to {suma} zł")
    if wybor == 4:
        print("Które pomieszczenie chcesz usunąć?")

    if wybor == 5:
        break