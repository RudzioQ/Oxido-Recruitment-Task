# Opis działania aplikacji

1. Importowanie biblioteki
2. Ustawienie klucza API
3. Odczyt pliku article.txt: Kod otwiera plik article.txt w trybie odczytu i odczytuje jego zawartość, która jest następnie zapisana w zmiennej article_content. Plik musi istnieć w tej samej lokalizacji co skrypt lub w ścieżce wskazanej przez użytkownika.
4. Tworzenie promptu (zapytania): Zmienna prompt jest skonstruowana w taki sposób, aby przekazać odpowiednie instrukcje do modelu GPT-4. Model ma za zadanie przetworzyć tekst na kod HTML z określonymi wymaganiami.
5. Wysłanie zapytania do OpenAI: Funkcja openai.ChatCompletion.create jest używana do komunikacji z modelem gpt-4.
6. Wysłanie zapytania do OpenAI: Funkcja openai.ChatCompletion.create jest używana do komunikacji z modelem gpt-4.
7. Zapisanie wygenerowanego kodu: Odpowiedź zwrócona przez model jest pobierana, a zawartość (czyli wygenerowany kod HTML) jest zapisana w pliku artykul.html.
8. Komunikat końcowy: Na koniec kod wypisuje komunikat potwierdzający zapisanie wynikowego pliku.


# Instrukcja korzystania z kodu:

1. Upewnij się, że masz zainstalowaną bibliotekę OpenAI. Jeśli nie, możesz zainstalować ją za pomocą polecenia: "pip install openai"
2. Zastąp przykładowy klucz, swoim własnym, uzyskanym z platformy OpenAI (ze względów bezpieczeństw zamieniłem klucz na "BLANK")
3. Upewnij się, że plik article.txt zawiera tekst, który chcesz przekonwertować na format HTML. Plik powinien znajdować się w tej samej lokalizacji co skrypt.
4. Wykonaj skrypt za pomocą dowolnego środowiska obsługującego kod Python (preferowany pyCharm), lub poprzez wywołanie polecenia w konsoli: "python script.py"
5. Po uruchomieniu skryptu, plik artykul.html zostanie wygenerowany w tej samej lokalizacji co skrypt. Otwórz go, aby zobaczyć wynik.
