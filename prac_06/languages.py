from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

programming_languages = [python, ruby, visual_basic]
dynamic_language = [language for language in programming_languages if language.is_dynamic()]
print("The dynamically typed languages are:")
for language in dynamic_language:
    print(f"{language.name}", end="\n")
