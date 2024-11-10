import os
import json

def odczyt(typ: str):
    p = os.getcwd()  # Bieżący katalog roboczy
    match typ:
        case 'fun':
            dane = []
            i = 1
            while True:
                try:
                    with open(f"cls/zadania/fun{i}.json", "r") as file:
                        dane.append(json.load(file))
                    i += 1  # Zwiększamy licznik plików
                except FileNotFoundError:
                    break
                except json.JSONDecodeError:
                    print(f"Błąd dekodowania pliku: . Przerywam wczytywanie.")
                    break
            return dane
        case 'work':
            dane = []
            i = 1
            while True:
                try:
                    with open(f"cls/zadanie/work{i}.json", "r") as file:
                        dane.append(json.load(file))
                    i += 1  # Zwiększamy licznik plików
                except FileNotFoundError:
                    break
                except json.JSONDecodeError:
                    print(f"Błąd dekodowania pliku. Przerywam wczytywanie.")
                    break
            return dane
        case 'duties':
            dane = []
            i = 1
            while True:
                try:
                    with open(f"cls/zadanie/duties{i}.json", "r") as file:
                        dane.append(json.load(file))
                    i += 1  # Zwiększamy licznik plików
                except FileNotFoundError:
                    break
                except json.JSONDecodeError:
                    print(f"Błąd dekodowania pliku. Przerywam wczytywanie.")
                    break
            return dane
        case 'ppr':
            dane = []
            i = 1
            while True:
                try:
                    with open(f"cls/zadanie/ppr{i}.json", "r") as file:
                        dane.append(json.load(file))
                    i += 1  # Zwiększamy licznik plików
                except FileNotFoundError:
                    break
                except json.JSONDecodeError:
                    print(f"Błąd dekodowania pliku. Przerywam wczytywanie.")
                    break
            return dane