import tokenize
import io
tokens = tokenize.generate_tokens(io.StringIO("x = 10").readline)
for tok in tokens:
    print(tok)
import ast
tree = ast.parse("x = 10")
print(ast.dump(tree, indent=2))
