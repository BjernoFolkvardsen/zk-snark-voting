<p><a target="_blank" href="https://app.eraser.io/workspace/G3dUXURUGn3xFGdR9Ux2" id="edit-in-eraser-github-link"><img alt="Edit in Eraser" src="https://firebasestorage.googleapis.com/v0/b/second-petal-295822.appspot.com/o/images%2Fgithub%2FOpen%20in%20Eraser.svg?alt=media&amp;token=968381c8-a7e7-472a-8ed6-4a6626da5501"></a></p>

```
# create the circuit
circuit = Circuit("circuit.circom", working_dir=working_dir,output_dir=working_dir)

#compile the circuit
circuit.compile()

# Prints info about the circuit. Requires that the circuit was compiled first.
circuit.get_info()

#Prints info about the constraints of the circuit.
circuit.print_constraints()

#Generates a witness file. Requires that the circuit was compiled first.
# Args:
#     input_file (str): Path to an input json file that specifies the inputs to the circuit.
#     output_file (str): Path of where the witness file should be outputted. Defaults to a randomly generated file name.

circuit.gen_witness(working_dir+"input.json")
# proc = subprocess.run(
#         ["snarkjs", "plonk", "setup", working_dir+"circuit.r1cs", ptau.ptau_file, working_dir+"key.zkey"],
#         shell=True,
#         capture_output=True,
#         cwd=working_dir,
#         check=True,
# )
# print(proc.stdout.decode('utf-8'))

# Prepares to generate proof and creates a zkey file.
circuit.setup(GROTH, ptau)

# Contributes to phase 2. Required for the Groth16 proving scheme. The circuit must have been previously setup.
circuit.contribute_phase2(entropy="p1")

#Generates a proof for the circuit.
circuit.prove(GROTH)

# Exports a verification key.
circuit.export_vkey(output_file=working_dir+"vkey.json")

# Verifies that a proof is valid.
circuit.verify(GROTH, vkey_file=working_dir+"vkey.json", public_file=working_dir+"public.json", proof_file=working_dir+"proof.json")
```
![Figure 1](/.eraser/G3dUXURUGn3xFGdR9Ux2___lqrF2i07Z8W7Qv7K4pe5Hkyjfqc2___---figure---dp4k0pMXyNjcXWji-09FM---figure---OAJm1qNsvBVzDa0xjVs0Ag.png "Figure 1")




<!--- Eraser file: https://app.eraser.io/workspace/G3dUXURUGn3xFGdR9Ux2 --->