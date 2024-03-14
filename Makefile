# local-setup:
# 	echo "\033[0;32mCreating python environment...\033[0m"
# 	python3.9 -m venv . && source ./bin/activate
# 	python3.9 --version
# 	echo "\033[0;32mInstalling modules and dependencies...\033[0m"
# 	pip3.9 install --upgrade pip
# 	pip3.9 --version
# 	pip3.9 install --upgrade pip setuptools
# 	pip3.9 install wasmer wasmer_compiler_cranelift
# 	pip3.9 install -r requirements.txt

local-setup:
	echo "\033[0;32mCreating python environment...\033[0m"
# python3 -m venv . && source ./bin/activate
	python3.10 --version
	echo "\033[0;32mInstalling modules and dependencies...\033[0m"
	pip3.10 install --upgrade pip
	pip3.10 --version
	pip3.10 install --upgrade pip setuptools
	pip3.10 install -r requirements.txt

	echo "\033[0;32mCreating the package...\033[0m"
# pip install -e .
	echo "\033[0;32mInstalling npm packages...\033[0m"
	npm install
	echo "\033[0;32mAll done. Happy coding!\033[0m"

run:
	python3.10 app.py

test:
	pytest

clearNrun:
	make clearFullCircuit
	make run

clearAll:
	make clearFullCircuit
	make clearVoteCircuit
	make clearCommitmentCircuit
	make clearOrCircuit
	make clearAndCircuit
	make clearTestCircuit
	make clearMerkleTreeInclusionCircuit
	make clearElGamalCircuit

clearFullCircuit:
	rm -rf circuits/CommitmentCircuit/circuit_js/
	rm -rf circuits/CommitmentCircuit/*.zkey
	rm -f circuits/CommitmentCircuit/circuit.r1cs
	rm -f circuits/CommitmentCircuit/circuit.sym
	rm -f circuits/CommitmentCircuit/witness.wtns
	rm -f circuits/CommitmentCircuit/vkey.json
	rm -f circuits/CommitmentCircuit/public.json
	rm -f circuits/CommitmentCircuit/proof.json

clearVoteCircuit:
	rm -rf circuits/FullCircuit/NullVote_js/
	rm -rf circuits/FullCircuit/*.zkey
	rm -f circuits/FullCircuit/NullVote.r1cs
	rm -f circuits/FullCircuit/NullVote.sym
	rm -rf circuits/FullCircuit/Vote_js/
	rm -f circuits/FullCircuit/Vote.r1cs
	rm -f circuits/FullCircuit/Vote.sym
	rm -f circuits/FullCircuit/witness.wtns
	rm -f circuits/FullCircuit/vkey.json
	rm -f circuits/FullCircuit/public.json
	rm -f circuits/FullCircuit/proof.json

clearCommitmentCircuit:
	rm -rf circuits/CommitmentCircuit/circuit_js/
	rm -rf circuits/CommitmentCircuit/*.zkey
	rm -f circuits/CommitmentCircuit/circuit.r1cs
	rm -f circuits/CommitmentCircuit/circuit.sym
	rm -f circuits/CommitmentCircuit/witness.wtns
	rm -f circuits/CommitmentCircuit/vkey.json
	rm -f circuits/CommitmentCircuit/public.json
	rm -f circuits/CommitmentCircuit/proof.json

clearOrCircuit:
	rm -rf circuits/OrCircuit/circuit_js/
	rm -rf circuits/OrCircuit/*.zkey
	rm -f circuits/OrCircuit/circuit.r1cs
	rm -f circuits/OrCircuit/circuit.sym
	rm -f circuits/OrCircuit/witness.wtns
	rm -f circuits/OrCircuit/vkey.json
	rm -f circuits/OrCircuit/public.json
	rm -f circuits/OrCircuit/proof.json

clearAndCircuit:
	rm -rf circuits/AndCircuit/circuit_js/
	rm -rf circuits/AndCircuit/*.zkey
	rm -f circuits/AndCircuit/circuit.r1cs
	rm -f circuits/AndCircuit/circuit.sym
	rm -f circuits/AndCircuit/witness.wtns
	rm -f circuits/AndCircuit/vkey.json
	rm -f circuits/AndCircuit/public.json
	rm -f circuits/AndCircuit/proof.json

clearMerkleTreeInclusionCircuit:
	rm -rf circuits/MerkleTreeInclusionCircuit/circuit_js/
	rm -rf circuits/MerkleTreeInclusionCircuit/*.zkey
	rm -f circuits/MerkleTreeInclusionCircuit/circuit.r1cs
	rm -f circuits/MerkleTreeInclusionCircuit/circuit.sym
	rm -f circuits/MerkleTreeInclusionCircuit/witness.wtns
	rm -f circuits/MerkleTreeInclusionCircuit/vkey.json
	rm -f circuits/MerkleTreeInclusionCircuit/public.json
	rm -f circuits/MerkleTreeInclusionCircuit/proof.json


clearElGamalCircuit:
	rm -rf circuits/ElGamalCircuit/elGamalcircuit_js/
	rm -rf circuits/ElGamalCircuit/*.zkey
	rm -f circuits/ElGamalCircuit/elGamalcircuit.r1cs
	rm -f circuits/ElGamalCircuit/elGamalcircuit.sym
	rm -f circuits/ElGamalCircuit/witness.wtns
	rm -f circuits/ElGamalCircuit/vkey.json
	rm -f circuits/ElGamalCircuit/public.json
	rm -f circuits/ElGamalCircuit/proof.json
