import wikipedia

# set the language to English
wikipedia.set_lang("en")

search_phrase = input("Enter a prompt: ")

while search_phrase != "":
    try:
        # search for the page and get the first result
        page_title = wikipedia.search(search_phrase)[0]

        # get the summary of the page
        page_summary = wikipedia.summary(search_phrase)

        # get the Wikipedia page object without auto_suggest
        page = wikipedia.page(page_title, auto_suggest=False)

        # print the title, summary, and URL
        print("Title:", page.title)
        print("Summary:", page_summary)
        print("URL:", page.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print("Disambiguation Error:", e.options)
    except wikipedia.exceptions.PageError:
        print("Page not found.")

    search_phrase = input("Enter a prompt: ")