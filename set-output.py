def set_output(self, output_node, signal_node):
    self.compile_expr(output_node)
    self.compile_expr(signal_node)
    self.assembly.dwr()