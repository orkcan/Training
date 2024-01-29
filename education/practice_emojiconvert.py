message = input("Enter your desired emoji to convert: ")
words = message.split(' ')
print(words)


emojis= {
    ":)":"😊",
    ":(":"🙁",
    "3:)":"😇"
}
output=""
emojis.update({':D':'😁'})

for spliited_word  in words:
    output += emojis.get(spliited_word,spliited_word+" ")
print(output)
