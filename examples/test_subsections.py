from mctdh_input.builders.hamiltonian_builder import HamiltonianBuilder, HamiltonianSubsection
from mctdh_input.utils.electronic_ops import ElectronicOperatorFactory
from mctdh_input.utils.nuclear_kinetic_ops import build_purely_nuclear_kinetic_subsection


# Initialize builder
dofs = ["el", "R"] + [f"x{i}" for i in range(1, 49)]
builder = HamiltonianBuilder(degrees_of_freedom_labels=dofs)

# Create operator factory for 3 electronic states
factory = ElectronicOperatorFactory(num_states=6)

# Create a purely electronic section
electronic_section = HamiltonianSubsection("Purely Electronic Terms")
electronic_section.add_term("1.0", [("el", factory.Smn(1, 2))])
electronic_section.add_term("0.5", [("el", factory.Zmn(3, 3))])
electronic_section.add_term("0.1", [("el", factory.identity())])

# Add to builder
builder.add_subsection(electronic_section)

# Create a nuclear-electronic coupling section (just for fun)
coupling_section = HamiltonianSubsection("Coupling Terms")
coupling_section.add_term("0.25", [("el", factory.Smn(2, 1)), ("R", "x")])  # R is a nuclear mode

builder.add_subsection(coupling_section)

# Create a nuclear-kinetic section (just for fun)
kinetic_sub = build_purely_nuclear_kinetic_subsection(builder.dof_labels, electronic_label="el")
builder.add_subsection(kinetic_sub)

# Write to file
builder.generate_file("examples/hamiltonian_test.txt")
print("Hamiltonian file written to examples/hamiltonian_test.txt")
