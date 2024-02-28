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
	make clearCommitmentCircuit
	make run

clearAll:
	make clearFullCircuit
	make clearCommitmentCircuit
	make clearOrCircuit
	make clearAndCircuit
	make clearTestCircuit
	make clearSetMembershipCircuit
	make clearSchnorrCircuit

clearFullCircuit:
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

clearTestCircuit:
	rm -rf circuits/TestCircuit/circuit_js/
	rm -rf circuits/TestCircuit/*.zkey
	rm -f circuits/TestCircuit/circuit.r1cs
	rm -f circuits/TestCircuit/circuit.sym
	rm -f circuits/TestCircuit/witness.wtns
	rm -f circuits/TestCircuit/vkey.json
	rm -f circuits/TestCircuit/public.json
	rm -f circuits/TestCircuit/proof.json

clearSetMembershipCircuit:
	rm -rf circuits/SetMembershipCircuit/circuit_js/
	rm -rf circuits/SetMembershipCircuit/*.zkey
	rm -f circuits/SetMembershipCircuit/circuit.r1cs
	rm -f circuits/SetMembershipCircuit/circuit.sym
	rm -f circuits/SetMembershipCircuit/witness.wtns
	rm -f circuits/SetMembershipCircuit/vkey.json
	rm -f circuits/SetMembershipCircuit/public.json
	rm -f circuits/SetMembershipCircuit/proof.json

clearSchnorrCircuit:
	rm -rf circuits/SchnorrCircuit/circuit_js/
	rm -rf circuits/SchnorrCircuit/*.zkey
	rm -f circuits/SchnorrCircuit/circuit.r1cs
	rm -f circuits/SchnorrCircuit/circuit.sym
	rm -f circuits/SchnorrCircuit/witness.wtns
	rm -f circuits/SchnorrCircuit/vkey.json
	rm -f circuits/SchnorrCircuit/public.json
	rm -f circuits/SchnorrCircuit/proof.json

# virtualenv --python=python3.5 .venv
# source .venv/bin/activate
