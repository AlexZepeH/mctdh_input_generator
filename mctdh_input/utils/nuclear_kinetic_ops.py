# hamiltonian_construction.py

from mctdh_input.builders.hamiltonian_builder import HamiltonianSubsection

def build_purely_nuclear_kinetic_subsection(
    dof_labels: list[str], 
    electronic_label: str, 
    coefficient: str = "1.0"
) -> HamiltonianSubsection:
    subsection = HamiltonianSubsection("Purely Nuclear Kinetic Terms")

    for i, label in enumerate(dof_labels):
        if label == electronic_label:
            continue
        subsection.add_term(coefficient, [(label, "KE")])

    return subsection
