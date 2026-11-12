while True:
    print("Co chcesz zrobić?: ")
    print("1 - Dodaj pomieszczenie")
    print("2 - Wyświetl pomieszczenia")
    print("3 - Oblicz całkowity koszt")
    print("4 - Usuń pomieszczenie")
    print("5 - Zapisz dane")
    print("6 - Wczytaj dane")
    print("7 - Wyjście")
    wybor = int(input("Co wybierasz?: "))
    if wybor == 1:
        nazwa_pomieszczenia = str(input("Jak się nazywa to pomieszczenie?: "))
        powierzchnia = int(input("Ile metrów kwadratowych zajmuje twoje pomieszczenie: "))

