import ast
with open("file.crpy") as f:
    syntaxtree = ast.parse("\n".join(f.readlines()))
