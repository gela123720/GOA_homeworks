# 6) შექმენით ფუნქცია, რომელიც იღებს სიტყვას და აბრუნებს, არის თუ არა ეს სიტყვა პალინდრომი.

def palindrom(word):
    if word == word[::-1]:
        print("This word is a palindrom")
    else:
        print("This word is not a palindrom")

palindrom("gela")
palindrom("ana")