class Compiler:
    def compile_stmt(self, node):
        if type(node) == Module:  # Juurtipp
            for n in node.body:
                self.compile_stmt(n)  # Rekursioon
        elif type(node) == If:
            self.if_stmt(node)  # Kompileeri if-lause
        # ...
