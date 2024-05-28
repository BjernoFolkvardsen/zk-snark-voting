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

setup-db:
	docker run -d -p 27017:27017 --name m1 mongo
#	python3.10 setup_db.py

start-db:
	docker start m1

test:
	pytest

compileWitness:
	node circuits/FullCircuit/circuit_js/generate_witness.js circuits/FullCircuit/circuit_js/circuit.wasm circuits/FullCircuit/input.json circuits/FullCircuit/witness.wtns;

clearNrun:
	make clearFullCircuit
	make clearTmp
	make run

clearAll:
	make clearFullCircuit
	make clearVoteCircuit
	make clearCommitmentCircuit
	make clearOrCircuit
	make clearAndCircuit
	make clearMerkleTreeInclusionCircuit
	make clearElGamalCircuit

clearTmp:
	rm -f tmp/proof.json
	rm -f tmp/public.json
	rm -f tmp/vkey.json

clearFullCircuit:
	rm -rf circuits/FullCircuit/circuit_js/
	rm -rf circuits/FullCircuit/*.zkey
	rm -f circuits/FullCircuit/circuit.r1cs
	rm -f circuits/FullCircuit/circuit.sym
	rm -f circuits/FullCircuit/witness.wtns
	rm -f circuits/FullCircuit/vkey.json
	rm -f circuits/FullCircuit/public.json
	rm -f circuits/FullCircuit/proof.json
	rm -f circuits/FullCircuit/circuit.circom

clearVoteCircuit:
	rm -rf circuits/VoteCircuit/NullVote_js/
	rm -rf circuits/VoteCircuit/*.zkey
	rm -f circuits/VoteCircuit/NullVote.r1cs
	rm -f circuits/VoteCircuit/NullVote.sym
	rm -rf circuits/VoteCircuit/Vote_js/
	rm -f circuits/VoteCircuit/Vote.r1cs
	rm -f circuits/VoteCircuit/Vote.sym
	rm -f circuits/VoteCircuit/witness.wtns
	rm -f circuits/VoteCircuit/vkey.json
	rm -f circuits/VoteCircuit/public.json
	rm -f circuits/VoteCircuit/proof.json

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
	rm -rf circuits/OldCircuits/OrCircuit/circuit_js/
	rm -rf circuits/OldCircuits/OrCircuit/*.zkey
	rm -f circuits/OldCircuits/OrCircuit/circuit.r1cs
	rm -f circuits/OldCircuits/OrCircuit/circuit.sym
	rm -f circuits/OldCircuits/OrCircuit/witness.wtns
	rm -f circuits/OldCircuits/OrCircuit/vkey.json
	rm -f circuits/OldCircuits/OrCircuit/public.json
	rm -f circuits/OldCircuits/OrCircuit/proof.json

clearAndCircuit:
	rm -rf circuits/OldCircuits/AndCircuit/circuit_js/
	rm -rf circuits/OldCircuits/AndCircuit/*.zkey
	rm -f circuits/OldCircuits/AndCircuit/circuit.r1cs
	rm -f circuits/OldCircuits/AndCircuit/circuit.sym
	rm -f circuits/OldCircuits/AndCircuit/witness.wtns
	rm -f circuits/OldCircuits/AndCircuit/vkey.json
	rm -f circuits/OldCircuits/AndCircuit/public.json
	rm -f circuits/OldCircuits/AndCircuit/proof.json

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
