from mctdh_input.builders.hamiltonian_builder import HamiltonianBuilder, HamiltonianSubsection
from mctdh_input.utils.electronic_ops import ElectronicOperatorFactory
from mctdh_input.utils.nuclear_kinetic_ops import build_purely_nuclear_kinetic_subsection
from mctdh_input.utils.nuclear_potential_ops import build_purely_nuclear_potential_subsection
from mctdh_input.utils.generate_vibronic_couplings_dictionary import electronic_couplings as vibronic_couplings

# Initialize builder
dofs = ["el", "R"] + [f"x{i}" for i in range(1, 49)]

def add_vibronic_coupling_terms(electronic_couplings: dict, hamitlonian: HamiltonianBuilder):
    """
    Add vibronic coupling terms for each electronic state.
    :param electronic_couplings: Dictionary containing electronic state coupling info
    """
    for electronic_state, coupling_data in electronic_couplings.items():
        dofs = coupling_data["dofs"]
        coefficients = coupling_data["coefficients"]
        subsection = HamiltonianSubsection(HamiltonianSubsection(f"Coupling Terms for Electronic State {electronic_state}"))

        # Loop through the DOFs and coefficients for this electronic state
        for dof, coefficient in zip(dofs, coefficients):
            # Add the term with the coupling coefficient
            # The first tuple refers to the electronic state (using factory.Smn)
            # The second tuple refers to the nuclear degree of freedom
            subsection.add_term(coefficient, [
                ("el", factory.Smn(electronic_state, electronic_state)),  # Smn for electronic part
                (dof, "q")  # Nuclear DOF term
            ])
        hamitlonian.add_subsection(subsection)




builder = HamiltonianBuilder(degrees_of_freedom_labels=dofs)

# Create operator factory for 3 electronic states
factory = ElectronicOperatorFactory(num_states=6)

# Create a nuclear-kinetic section (just for fun)
kinetic_sub = build_purely_nuclear_kinetic_subsection(builder.dof_labels, electronic_label="el")
builder.add_subsection(kinetic_sub)

# Create a nuclear-kinetic section (just for fun)
potential_sub = build_purely_nuclear_potential_subsection(builder.dof_labels, electronic_label="el", anharmonic_labels=['R'])
builder.add_subsection(potential_sub)


# Create a purely electronic section
electronic_section = HamiltonianSubsection("Purely Electronic Terms")
electronic_section.add_term("1.0", [("el", factory.Smn(1, 2))])
electronic_section.add_term("0.5", [("el", factory.Zmn(3, 3))])
electronic_section.add_term("0.1", [("el", factory.identity())])

# Add to builder
builder.add_subsection(electronic_section)

# Create a nuclear-electronic coupling section (just for fun)
add_vibronic_coupling_terms(vibronic_couplings,builder)

# Write to file
builder.generate_file("examples/hamiltonian_test.txt")
print("Hamiltonian file written to examples/hamiltonian_test.txt")
