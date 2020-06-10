            # 23: Strings, Bytes, and Character Encodings

import sys
script, filename, input_encoding, error = sys.argv
    #3rd step: ([languages.txt encoded into utf-8], given codec, error)
def main(language_file, encoding, errors):
    #4th step: Read each line of the file. If there is a line, continue, otherwise stop
    line = language_file.readline()
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    #5th step: strip all white space from the line
    next_lang = line.strip()
    #6th step: Encode the stripped line into raw bytes
    raw_bytes = next_lang.encode(encoding, errors=errors)
    #7th step: Decode the raw bytes into utf-8 language
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    #8th step: Print the encoded raw bytes <===> print the decoded strings
    print(raw_bytes, "<===>", cooked_string)

    #1st step: encode text in "languages.txt" into raw bytes
languages = open(filename, encoding="utf-8")
    #2nd step: begin the main function ([open languages.txt & encode to utf-8], given codec, error)
main(languages, input_encoding, error)
