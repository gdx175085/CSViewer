# Dokumentacja: CSViewer

## 1. Wprowadzenie
Celem tego projektu jest stworzenie aplikacji do przeglądania, sortowania oraz filtrowania danych z plików CSV, z interfejsem graficznym zaprojektowanym w Pythonie z wykorzystaniem bibliotek `customtkinter` i `pandas`. Projekt jest zgodny z wytycznymi SAFe® 6.0 i przyjmuje podejście iteracyjne, umożliwiające regularne dostarczanie wartości dla interesariuszy.

---

## 2. Wizja Produktu

Aplikacja umożliwia użytkownikom:

- Wyświetlanie danych z plików CSV w przyjaznym interfejsie graficznym.
- Sortowanie danych według wybranych kolumn.
- Filtrowanie danych na podstawie wartości w wybranych kolumnach.
- Pracę w trybie ciemnego motywu (dark mode), poprawiając komfort pracy.
- Przeglądanie ograniczonych wyników (pierwsze 100 rekordów) w celu optymalizacji wydajności.

---

## 3. Cel Biznesowy

Projekt ma na celu wsparcie operacji analizy danych przez dostarczenie łatwego w obsłudze narzędzia umożliwiającego szybkie i efektywne przeglądanie, sortowanie oraz filtrowanie danych CSV.

---

## 4. Kluczowe Funkcjonalności

### 4.1 Wczytywanie Plików CSV

- Automatyczne ładowanie danych z pliku CSV zdefiniowanego w kodzie.
- Obsługa błędów podczas ładowania danych (np. niepoprawny format pliku).

### 4.2 Wyświetlanie Danych

- Interfejs oparty na kontrolce `Treeview` z paskami przewijania (pionowym i poziomym).
- Limit wyników do 100 rekordów, aby zapewnić płynne działanie aplikacji.

### 4.3 Sortowanie

- Użytkownik może sortować dane według wybranej kolumny w porządku rosnącym lub malejącym.
- Interfejs graficzny umożliwia łatwy wybór kolumny i kierunku sortowania.

### 4.4 Filtrowanie

- Możliwość filtrowania danych na podstawie wybranej kolumny i wartości wprowadzonej przez użytkownika.
- Obsługa wyszukiwania wartości w trybie case-insensitive.

### 4.5 Interfejs Użytkownika

- Tryb ciemny (dark mode) dla lepszej czytelności i komfortu pracy.
- Responsywność interfejsu w pełnym oknie aplikacji.
- Estetyczny i nowoczesny design dzięki bibliotece `customtkinter`.

---

## 5. Realizacja Wartości w SAFe

### 5.1 ART (Agile Release Train)

Ten projekt jest częścią inicjatywy Agile Release Train, skupiającej się na aplikacjach analitycznych. Kluczowym celem jest poprawa produktywności analityków danych poprzez uproszczenie ich codziennych zadań.

### 5.2 Epiki

- **Epik 1**: Stworzenie interfejsu graficznego dla aplikacji.
- **Epik 2**: Dodanie funkcji sortowania danych.
- **Epik 3**: Implementacja funkcji filtrowania danych.
- **Epik 4**: Implementacja trybu ciemnego.
- **Epik 5**: Optymalizacja wydajności dla dużych plików CSV.

### 5.3 Funkcje

Każdy epik został podzielony na mniejsze funkcje realizowane podczas iteracji:

- Wyświetlanie danych w tabeli.
- Obsługa pasków przewijania.
- Dodanie przycisków sortowania i filtrowania.

### 5.4 Iteracje

Projekt jest realizowany w podejściu iteracyjnym:

- **Iteracja 1**: Wyświetlenie danych w tabeli z podstawową funkcjonalnością.
- **Iteracja 2**: Dodanie sortowania danych.
- **Iteracja 3**: Wprowadzenie trybu ciemnego i filtrowania danych.
- **Iteracja 4**: Optymalizacja wizualna i wydajnościowa.

---

## 6. Techniczne Szczegóły

### 6.1 Technologia

- **Język programowania**: Python 3
- **Biblioteki**: pandas, customtkinter, tkinter

### 6.2 Instalacja

Aby uruchomić aplikację, należy zainstalować wymaganą bibliotekę `customtkinter` za pomocą polecenia:

```
pip install customtkinter
```

### 6.3 Struktura Kodowa

- **`load_csv(file_path)`**: Funkcja ładująca dane z pliku CSV i ograniczająca je do pierwszych 100 rekordów.
- **`display_data(data, tree)`**: Funkcja wyświetlająca dane w widoku `Treeview` z obsługą kolumn i danych wierszowych.
- **`sort_data(data, tree, sort_column, ascending)`**: Funkcja implementująca sortowanie danych.
- **`filter_data(data, tree)`**: Funkcja umożliwiająca filtrowanie danych na podstawie wartości wprowadzonej przez użytkownika.
- **`apply_darkmode_to_treeview(tree)`**: Funkcja stosująca tryb ciemny do kontrolki `Treeview`.
- **Główna funkcja `main()`**: Obsługa interfejsu graficznego, logiki aplikacji i integracja funkcjonalności sortowania i filtrowania.

### 6.4 Optymalizacja

- Ograniczenie wyników do 100 rekordów.
- Dodanie pasków przewijania (pionowego i poziomego).
- Tryb ciemny dla lepszej czytelności w warunkach słabego oświetlenia.

---

## 7. Testowanie

### 7.1 Testy Manualne

1. Wczytanie pliku CSV i sprawdzenie poprawności danych.
2. Przetestowanie sortowania danych dla każdej kolumny.
3. Walidacja filtrowania danych z różnymi wartościami wejściowymi.
4. Walidacja interfejsu użytkownika (czytelność, responsywność).

### 7.2 Testy Automatyczne

- Testy jednostkowe dla funkcji `load_csv` i `sort_data`.
- Mockowanie obiektów, takich jak `Treeview`, aby sprawdzić poprawność wyświetlania danych.

Przykładowe testy (zawarte w pliku `test.py`):

- **`test_load_csv`**: Sprawdza poprawność wczytywania danych.
- **`test_sort_data`**: Weryfikuje sortowanie danych według wskazanej kolumny.

---

## 8. Wymagania Niefunkcjonalne

- Aplikacja powinna działać w systemach Windows, macOS i Linux.
- Czas reakcji aplikacji podczas sortowania i filtrowania nie powinien przekraczać 2 sekund dla 100 rekordów.

---

## 9. Potencjalny Rozwój

- Dodanie zaawansowanego filtrowania z wieloma kryteriami.
- Eksport wyników sortowania lub filtrowania do nowego pliku CSV.
- Integracja z bazami danych (np. MySQL, PostgreSQL).
- Rozbudowa interfejsu o dodatkowe funkcje analityczne (np. wykresy).

---

## 10. Podsumowanie

Projekt dzięki dodatkowym funkcjonalnościom, takim jak filtrowanie danych, aplikacja stanowi wszechstronne narzędzie wspierające analityków danych i innych użytkowników.

