import tokenize, io
tokens = tokenize.generate_tokens(io.StringIO("x = 10").readline)
for tok in tokens:
    print(tok)


import dis
dis.dis("x = Fayaz")



import ast
print(ast.dump(ast.parse("x = 10"), indent=2))
