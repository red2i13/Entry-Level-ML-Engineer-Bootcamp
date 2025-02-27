import string
import sys
def text_analyzer(text = None):
    '''This function counts the number of upper characters, lower characters,
punctuation and spaces in a given text'''
    if(not text):
        text = input("What is the text to analyze? ")
    if not isinstance(text, str):
        print("Error Arugument must be a string")
        return
    punctuation = 0
    spaces = 0
    upper = 0
    lowercase = 0
    tot = len(text)
    for char in text:
        if(char in string.punctuation):
            punctuation += 1
        elif(char.isupper()):
            upper += 1
        elif(char.islower()):
            lowercase += 1
        elif(char.isspace()):
            spaces += 1
    print("The text contains {0} printable character(s)\
:\n- {1} upper letter(s)\n- {2} lower letter(s)\n\
- {3} punctuation mark(s)\n- {4} space(s)"\
    .format(tot, upper, lowercase, punctuation, spaces))

if __name__=="__main__":
    if len(sys.argv) != 2:
        print("Error the number of args are not correct")
        sys.exit()
    text_analyzer(sys.argv[1])
