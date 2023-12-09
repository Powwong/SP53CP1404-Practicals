WORDS = {}
lengths = []

text = input("Text: ")
TEXTS = text.split(" ")
for text in TEXTS:
    if text in WORDS.keys():
        WORDS[text] += 1
    else:
        WORDS[text] = 1

list_words = WORDS.keys()
sorted_words = sorted(list_words)

for word in WORDS.keys():
    length = len(word)
    lengths.append(length)
    width = max(lengths)

for text in sorted_words:
    print(f"{text:<{width}}: {WORDS[text]}")