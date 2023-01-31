from PIL import Image

MORSE_CODE_TO_CHARS_MAPPING = {
    ".-"    : 'A',   "-..."  : 'B',   "-.-."  : 'C',   "-.."   : 'D',
    "."     : 'E',   "..-."  : 'F',   "--."   : 'G',   "...."  : 'H',
    ".."    : 'I',   ".---"  : 'J',   "-.-"   : 'K',   ".-.."  : 'L',
    "--"    : 'M',   "-."    : 'N',   "---"   : 'O',   ".--."  : 'P',
    "--.-"  : 'Q',   ".-."   : 'R',   "..."   : 'S',   "-"     : 'T',
    "..-"   : 'U',   "...-"  : 'V',   ".--"   : 'W',   "-..-"  : 'X',
    "-.--"  : 'Y',   "--.."  : 'Z',   ".----" : '1',   "..---" : '2',
    "...--" : '3',   "....-" : '4',   "....." : '5',   "-...." : '6',
    "--..." : '7',   "---.." : '8',   "----." : '9',   "-----" : '0',
}

def get_morse_from_image():
    img_file = Image.open("external_resources/picture.png")
    img_width, img_height = img_file.size
    img_pixel = img_file.load()
    
    preposition = 0
    morse_code = ''

    for y_point in range(img_height):
        for x_point in range(img_width):
            if img_pixel[x_point, y_point] == 1:
                morse_code += chr(x_point + 100 * y_point - preposition)
                preposition = x_point + 100 * y_point
               
    return morse_code
    

def morse_to_ascii(morse_code):
    english_plain_text = ''

    current_char_morse_code = ''
    i = 0
    while i < len(morse_code) - 1:
        if morse_code[i] == ' ':
            if len(current_char_morse_code) == 0 and morse_code[i + 1] == ' ':
                english_plain_text += ' '
                i += 1
            else:
                english_plain_text += MORSE_CODE_TO_CHARS_MAPPING[
                    current_char_morse_code]
                current_char_morse_code = ''
        else:
            current_char_morse_code += morse_code[i]
        i += 1

    if len(current_char_morse_code) > 0:
        english_plain_text += MORSE_CODE_TO_CHARS_MAPPING[
            current_char_morse_code]

    return english_plain_text


if __name__ == "__main__":
    morse_code = get_morse_from_image()
    text = morse_to_ascii(morse_code)
    print(morse_code)
    print(text)
