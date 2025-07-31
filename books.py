import re

def calc_books(name):
    punctuation = r"[,.!;:\"()\-_+*']"

    # use this pattern to remove articles
    articles_pattern = r'\b(a|an|the)\b'

    with open(name, encoding="utf-8") as file:
        data = file.read().lower()
        cleaned_from_symbols = re.sub(punctuation, "", data)

        #  clean from articles here:
        cleaned_from_articles = re.sub(articles_pattern, '', cleaned_from_symbols, flags=re.IGNORECASE)

        cleaned_from_numbers = re.sub(r'\d+', '', cleaned_from_articles)

        res = set(cleaned_from_numbers.split())

        # return cleaned data
        print(res)

        return res
    
calc_books("book1.txt")

b1= calc_books("book1.txt")
b2 = calc_books("book2.txt")

print(b1)
print(b2)
print(f"Book1 has {len(b1)} unique words")
print(f"Book2 has {len(b2)} unique words")

print(f"book1 and book2 intersection: {len(b1 & b2)}")
print(f"book1 and book2 union: {len(b1 | b2)}")
print(f"book1 diff book2: {len(b1 - b2)}")
print(f"book2 diff book1: {len(b2 - b1)}")
print(f"book1 and book2 symmetric diff: {len(b1 ^ b2)}")



