# reusable functions
def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "😊",
        ":(": "🙁",
        "3:)": "😇"
    }

    output = ""
    for spliited_word in words:
        output += emojis.get(spliited_word, spliited_word) + " "
    return output


message = input("Enter your desired emoji to convert: ")
converted_result = emoji_converter(message)
print(converted_result)
