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
	make clearHashCircuit
	make run

clearAll:
	make clearFullCircuit
	make clearHashCircuit
	make clearOrCircuit
	make clearAndCircuit

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

clearHashCircuit:
	rm -rf circuits/HashCircuit/circuit_js/
	rm -rf circuits/HashCircuit/*.zkey
	rm -f circuits/HashCircuit/circuit.r1cs
	rm -f circuits/HashCircuit/circuit.sym
	rm -f circuits/HashCircuit/witness.wtns
	rm -f circuits/HashCircuit/vkey.json
	rm -f circuits/HashCircuit/public.json
	rm -f circuits/HashCircuit/proof.json

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

# virtualenv --python=python3.5 .venv
# source .venv/bin/activate
