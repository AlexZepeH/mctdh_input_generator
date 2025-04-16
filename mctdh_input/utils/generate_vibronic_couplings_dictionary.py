electronic_couplings = {}

def make_dof_range(start, end):
    return [f"x{i}" for i in range(start, end + 1)]

for state in range(1, 7):
    if state == 1:
        dofs = make_dof_range(1, 32)
    elif state == 2:
        dofs = make_dof_range(17, 48)
    elif state == 3:
        dofs = make_dof_range(1, 16)
    elif state == 4:
        dofs = make_dof_range(17, 32)
    elif state == 5:
        dofs = make_dof_range(33, 48)
    elif state == 6:
        dofs = make_dof_range(1, 48)

    coefficients = [f"k0{state}_{dof[1:]}" for dof in dofs]  # dof[1:] extracts the number part from "x##"
    electronic_couplings[state] = {
        "dofs": dofs,
        "coefficients": coefficients
    }

# optional: print to verify
import pprint
pprint.pprint(electronic_couplings)