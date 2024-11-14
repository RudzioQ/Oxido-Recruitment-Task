import openai

openai.api_key = 'BLANK'

with open('article.txt', 'r', encoding='utf-8') as file:
    article_content = file.read()

prompt = (
    "Przetwórz poniższy tekst na format HTML. Użyj odpowiednich tagów HTML do "
    "strukturyzacji treści, nie dodawaj żadnych nadrzędnych znacznikówki np. <head>, <html>, czy <!DOCTYPE>. Uwaga nie zaznaczaj kodu za pomocą apostrof czy ```html"
    "Zastanów się, a następnie wstaw w wybrane przez ciebie miejsca grafiki, które idealnie nadają się do użycia w danym miejscu tekstu za pomocą tagu <figure>, a w nim <img> z atrybutem"
    "src=\"image_placeholder.jpg\" oraz z tekstem altermatywnym z dokładnym i szczegółowym poleceniem wygenerowania wymyślonych przez ciebie grafik np: Wygeneruj grafikę przedstawiającą [TWÓJ POMYSŁ NA GRAFIKE]"
    "Dodaj także podpisy pod obrazkami, korzystając z tagu <figcaption>, który umieścisz w tym samym znaczniku <figure> co znacznik <img>."
    "W pliku html NIE dodawaj znacznika <body>, <footer>, <article> czy (```html); ani żadnego wizualnego zaznaczenia rozszerzenia pliku czy też znaczników sekcji."
    f"Artykuł:\n{article_content}"
)


response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "Jesteś asystentem, którego codzienną pracą jest przekładanie artykułów.txt na pliki .html zgodnie z podanymi Ci wytycznymi."},
        {"role": "user", "content": prompt}
    ]
)


html_content = response.choices[0].message['content']


with open('artykul.html', 'w', encoding='utf-8') as html_file:
    html_file.write(html_content)

print("Kod HTML został zapisany w pliku artykul.html")
