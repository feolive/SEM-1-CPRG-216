#morse code translator
#morse code dictionary
morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'}

#function to convert text to morse code
text = input("Enter the text to convert to morse code: ")
message = ""
while text != "stop":
    for i in text:
        if i.isspace():
            message = message + "   "
        else:
            output = morse_code[i.upper()]
            message = message + output
    print(message)
    text = input("Enter the text to convert to morse code: ")
    message = ""