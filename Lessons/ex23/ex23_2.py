import sys
script, encoding, error = sys.argv


#def main(language_file, encoding, errors):
#    line = language_file.readline()

#    if line:
#        print_line(line, encoding, errors)
#        return main(language_file, encoding, errors)


#def print_line(line, encoding, errors):
#    next_lang = line.strip()
#    raw_bytes = next_lang.encode(encoding, errors=errors)
#    cooked_string = raw_bytes.decode(encoding, errors=errors)

#    print(raw_bytes, "<====>", cooked_string)


#languages = open("languages.txt", encoding="utf-8")

#main(languages, encoding, errors)

read1 = "Test123"

def nick_line(read1, encoding):
    raw_bytes1 = read1.encode(encoding)
    cooked_string2 = raw_bytes1.decode(encoding)
    print(raw_bytes1, "<=====>", cooked_string2)

nick_line(read1, encoding)
