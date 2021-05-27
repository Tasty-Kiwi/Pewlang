import sys
import syntax

# Main code
if sys.argv[1] == "decode":
    pew = open(sys.argv[2], "rt", encoding="utf8").read()
    text = pew
    for x in range(len(syntax.BRAINF)):
        text = text.replace(syntax.CUSTOM_LANG[x], syntax.BRAINF[x])
    f = open(sys.argv[3], "w", encoding="utf8")
    f.write(text)
    f.close()
    print("Decoding Done.")

if sys.argv[1] == "encode":
    pew = open(sys.argv[2], "rt", encoding="utf8").read()
    text = pew
    for x in range(len(syntax.BRAINF)):
        text = text.replace(syntax.BRAINF[x], syntax.CUSTOM_LANG[x])
    f = open(sys.argv[3], "w", encoding="utf8")
    f.write(text)
    f.close()
    print("Encoding Done.")
