local-setup:
	python3.10 --version
	echo "\033[0;32mInstalling modules and dependencies...\033[0m"
	pip3.10 install --upgrade pip
	pip3.10 --version
	pip3.10 install --upgrade pip setuptools
	pip3.10 install -r requirements.txt
	echo "\033[0;32mInstalling npm packages...\033[0m"
	npm install
	echo "\033[0;32mAll done. Happy coding!\033[0m"

setup-db:
	docker run -d -p 27017:27017 --name m1 mongo

start-db:
	docker start m1

stop-db:
	docker stop m1

compileWitness:
	node circuits/FullCircuit/circuit_js/generate_witness.js circuits/FullCircuit/circuit_js/circuit.wasm circuits/FullCircuit/input.json circuits/FullCircuit/witness.wtns;

clearAndRun:
	make clearFullCircuit
	python3.10 app.py

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
	rm -rf circuits/VoteCircuit/*.zkey
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
