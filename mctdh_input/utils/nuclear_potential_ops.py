# hamiltonian_construction.py

from mctdh_input.builders.hamiltonian_builder import HamiltonianSubsection

def build_purely_nuclear_potential_subsection(
    dof_labels: list[str], 
    electronic_label: str,
    anharmonic_labels: list[str], 
    coefficient: str = "1.0"
) -> HamiltonianSubsection:
    subsection = HamiltonianSubsection("Purely Nuclear Potential Terms")

    for label in dof_labels:
        if label == electronic_label or (label in anharmonic_labels):
            continue
        subsection.add_term(coefficient, [(label, "q^2")])
    
    return subsection
