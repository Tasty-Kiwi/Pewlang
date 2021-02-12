import sys

# Definintions
Syntax = {
    '>': "pew",
    '<': "Pew",
    '+': "pEw",
    '-': "peW",
    ',': "PEw",
    '.': "pEW",
    '[': "PeW",
    ']': "PEW",
}

# Reverse-Definintions
ReverseSyntax = {
    'pew': ">",
    'Pew': "<",
    'pEw': "+",
    'peW': "-",
    'PEw': ",",
    'pEW': ".",
    'PeW': "[",
    'PEW': "]",
}
# Main code
if sys.argv[1] == "decode":
    pew = open(sys.argv[2], "rt", encoding="utf8").read()
    output = pew.replace(Syntax[']'], ']').replace(Syntax['['], '[').replace(Syntax['.'], '.').replace(Syntax[','], ',').replace(Syntax['-'], '-').replace(Syntax['+'], '+').replace(Syntax['<'], '<').replace(Syntax['>'], '>').replace(" ", "")
    f = open(sys.argv[3], "w")
    f.write(output)
    f.close()
    print("Decoding Done.")

if sys.argv[1] == "encode":
    pew = open(sys.argv[2], "rt", encoding="utf8").read()
    output = pew.replace(ReverseSyntax['PEW'], 'PEW ').replace(ReverseSyntax['PeW'], 'PeW ').replace(ReverseSyntax['pEW'], 'pEW ').replace(ReverseSyntax['PEw'], 'PEw ').replace(ReverseSyntax['peW'], 'peW ').replace(ReverseSyntax['pEw'], 'pEw ').replace(ReverseSyntax['Pew'], 'Pew ').replace(ReverseSyntax['pew'], 'pew ')
    f = open(sys.argv[3], "w")
    f.write(output)
    f.close()
    print("Encoding Done.")
