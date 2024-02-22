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
	echo "\033[0;32mAll done. Happy coding!\033[0m"

run:
	python3.10 app.py

test:
	pytest

clearNullVote:
	rm -rf circuits/FullCircuit/NullVote_js/
	rm -rf circuits/FullCircuit/*.zkey
	rm circuits/FullCircuit/NullVote.r1cs
	rm circuits/FullCircuit/NullVote.sym
	rm circuits/FullCircuit/witness.wtns

# virtualenv --python=python3.5 .venv
# source .venv/bin/activate
