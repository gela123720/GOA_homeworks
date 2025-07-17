# დაწერე ფუნქცია, რომელიც იღებს სტრიქონს და აბრუნებს მასში ხმოვნების (a, e, i, o, u) რაოდენობას. გამოიყენე ციკლი და if-else

def setnence(word):
    count = 0
    vowel = "aeiou"
    for i in word:
        if i in vowel:
            count += 1      
    print(count)

setnence("my name is gela")