pomieszczenia = []
powierzchnia_pomieszczen = []
koszt_materialow_pomieszczenia = []
koszt_robocizny_pomieszczenia = []

while True:
    print("\n===== KALKULATOR REMONTU =====")
    print("1 - Dodaj pomieszczenie")
    print("2 - Wyświetl pomieszczenia")
    print("3 - Oblicz całkowity koszt")
    print("4 - Usuń pomieszczenie")

    wybor = int(input("Wybierz opcję: "))

    if wybor == 1:
        nazwa_pomieszczenia = input("Jak się nazywa to pomieszczenie?: ")
        pomieszczenia.append(nazwa_pomieszczenia)
        powierzchnia = int(input("Ile metrów kwadratowych zajmuje pomieszczenie?: "))
        powierzchnia_pomieszczen.append(powierzchnia)
        koszt_materialow = int(input("Ile kosztują materiały?: "))
        koszt_materialow_pomieszczenia.append(koszt_materialow)
        koszt_robocizny = int(input("Ile kosztuje robocizna?: "))
        koszt_robocizny_pomieszczenia.append(koszt_robocizny)
        print("Pomieszczenie zostało dodane!")

    elif wybor == 2:
        if len(pomieszczenia) == 0:
            print("Brak dodanych pomieszczeń.")
        else:
            print("\n===== POMIESZCZENIA =====")

            for i in range(len(pomieszczenia)):
                razem = (
                        koszt_robocizny_pomieszczenia[i]
                        + koszt_materialow_pomieszczenia[i]
                )
                print(f"\n{i + 1}. {pomieszczenia[i]}")
                print(f"   Powierzchnia: {powierzchnia_pomieszczen[i]} m2")
                print(f"   Robocizna: {koszt_robocizny_pomieszczenia[i]} zł")
                print(f"   Materiały: {koszt_materialow_pomieszczenia[i]} zł")
                print(f"   Razem: {razem} zł")

            print("\n=========================")

    elif wybor == 3:
        suma = 0

        for i in range(len(pomieszczenia)):
            suma += koszt_robocizny_pomieszczenia[i]
            suma += koszt_materialow_pomieszczenia[i]

        print(f"\nCAŁKOWITY KOSZT: {suma} zł")

    elif wybor == 4:
        if len(pomieszczenia) == 0:
            print("Nie ma żadnych pomieszczeń do usunięcia.")
        else:
            print("\n===== POMIESZCZENIA =====")

            for i in range(len(pomieszczenia)):
                print(f"{i + 1}. {pomieszczenia[i]}")

            numer = int(input("Które pomieszczenie chcesz usunąć?: "))

            if 1 <= numer <= len(pomieszczenia):
                indeks = numer - 1

                usuniete = pomieszczenia[indeks]

                pomieszczenia.pop(indeks)
                powierzchnia_pomieszczen.pop(indeks)
                koszt_materialow_pomieszczenia.pop(indeks)
                koszt_robocizny_pomieszczenia.pop(indeks)

                print(f"Usunięto pomieszczenie: {usuniete}")
            else:
                print("Nieprawidłowy numer pomieszczenia.")

    elif wybor == 0:
        print("Koniec programu.")
        break
    else:
        print("Nieprawidłowa opcja.")