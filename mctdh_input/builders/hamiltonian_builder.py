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
    def __init__(self, coefficient :str, operators : list[tuple[str,str]]):
        """
        operators is a list of tuples like: [(dof_label, operator_string)]
        """
        self.coefficient = coefficient
        self.operators = operators

    def __str__(self):
        # Format the term: <coefficient> |<index1> <op1> |<index2> <op2>  ...
        terms = [f"{self.coefficient}"]
        for dof_label,op in self.operators:
            terms.append(f"|{dof_label} {op}")
        return " ".join(terms)

class HamiltonianSubsection:
    def __init__(self, name: str):
        self.name = name
        self.terms: list[OperatorTerm] = []

    def add_term(self, coefficient: str, ops: list[tuple[str, str]]):
        term = OperatorTerm(coefficient, ops)
        self.terms.append(term)

    def __str__(self):
        lines = [f"# {self.name}"]
        for term in self.terms:
            lines.append(str(term))
        return "\n".join(lines)

class HamiltonianBuilder:
    def __init__(self, degrees_of_freedom_labels: list[str]):
        self.dof_labels = degrees_of_freedom_labels
        self.subsections: list[HamiltonianSubsection] = []

    def add_subsection(self, subsection: HamiltonianSubsection):
        self.subsections.append(subsection)

    def add_term(self,coefficient: str, operators: list[tuple[str,str]]):
        """
        Add a new operator term.
        
        Parameters:
            coefficient (str): Coefficient for the operator term (e.g. "Q1 * Q2").
            operators (list of tuples): List of (DOF label, operator expression).
        """
        term = OperatorTerm(coefficient,operators)
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

             # FORMAT operator terms
            for subsection in self.subsections:
                f.write(str(subsection) + "\n\n")
        
            f.write("\nend-hamiltonian-section\n")


         