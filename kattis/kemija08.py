# strategy
#s = 'zepelepenapa papapripikapa'
#s = 'bapas jepe doposapadnapa opovapa kepemipijapa'
s = input()

vowels = ["a", "e", "i", "o", "u"]
sentence = ""
i = 0;
while i < len(s):
    letter = s[i]
    sentence += letter
    if letter in vowels: i += 3
    else: i += 1
print(sentence)
