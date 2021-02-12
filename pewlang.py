import sys
import Syntax

# Main code
if sys.argv[1] == "decode":
    pew = open(sys.argv[2], "rt", encoding="utf8").read()
    text = pew
    for x in range(len(Syntax.BRAINF)):
        text = text.replace(Syntax.CUSTOM_LANG[x], Syntax.BRAINF[x])
    f = open(sys.argv[3], "w")
    f.write(text)
    f.close()
    print("Decoding Done.")

if sys.argv[1] == "encode":
    pew = open(sys.argv[2], "rt", encoding="utf8").read()
    text = pew
    for x in range(len(Syntax.BRAINF)):
        text = text.replace(Syntax.BRAINF[x], Syntax.CUSTOM_LANG[x])
    f = open(sys.argv[3], "w")
    f.write(text)
    f.close()
    print("Encoding Done.")
