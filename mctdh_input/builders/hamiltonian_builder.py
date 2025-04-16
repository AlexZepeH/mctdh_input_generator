#hamiltonian_builder.py

"""
I want to create a file with several classes. 
The objective is to have a class named HamiltonianBuilder 
that would encapsulate everything needed for generating a 
"operator" file. The file starts with some standard line and 
finish with some standard line, in between it is followed by 
two main section: one where degrees of freedom are defined in 
a particular order, and a section where the actual terms of the 
operator in function of the degrees of freedom are defined.
"""

class OperatorTerm:
    def __init__(self, coefficient :str, operator :str):
        self.coefficient = coefficient
        self.operator = operator

    def __str__(self):
        return f"{self.coefficient} {self.operator}"

class HamiltonianBuilder:
    def __init__(self, degrees_of_freedom_labels: list[str]):
        self.dof_labels = degrees_of_freedom_labels
        self.operator_terms = []

    def add_term(self,coefficient: str, operator: str):
        term = OperatorTerm(coefficient,operator)
        self.operator_terms.append(term)

    def _format_modes_lines(self,chunk_size=5):
        """Split DOF labels into lines with a amx of `chunk_size` per line."""
        lines = []
        for i in range(0,len(self.dof_labels),chunk_size):
            chunk = self.dof_labels[i:i+chunk_size]
            line = "modes | " + " | ".join(chunk)
            lines.append(line)
        return lines

    def generate_file(self, filename: str):
        with open(filename, 'w') as f:
            f.write("$HAMILTONIAN-section\n\n")
            
            #FORMAT DOF section
            for line in self._format_modes_lines():
                f.write(line + "\n")
            f.write("\n")

            for term in self.operator_terms:
                f.write(str(term) + "\n")
        
            f.write("\nend-hamiltonian-section\n")


         