import os
import tempfile

from mctdh_input.builders.hamiltonian_builder import HamiltonianBuilder

def test_hamiltonian_builder_creates_correct_file():
    #Setup
    dofs = ["el", "R"] + [f"label{i}" for i in range(1, 48+1)]

    builder = HamiltonianBuilder(degrees_of_freedom_labels=dofs)
    builder.add_term("-E_offset","|1")

    #Use a temporary file for testing output
    with tempfile.NamedTemporaryFile(mode="r+", delete=False) as temp:
        temp_path = temp.name
        builder.generate_file(temp_path)

    #Read and verify output
    with open(temp_path, "r") as f:
        content = f.read()
    
    #Clean up
    os.remove(temp_path)

    # Assert structure 
    assert "HAMILTONIAN" in content
    assert content.count("modes |") >=10
    assert "-E_offset","|1" in content
    assert "end-hamiltonian-section" in content

