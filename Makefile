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
# python -m venv . && source ./bin/activate
	python --version
	echo "\033[0;32mInstalling modules and dependencies...\033[0m"
	pip install --upgrade pip
	pip --version
	pip install --upgrade pip setuptools
	pip install zkpy
	pip install -r requirements.txt

	echo "\033[0;32mCreating the package...\033[0m"
#	pip install -e .
	echo "\033[0;32mAll done. Happy coding!\033[0m"

run:
	python src/setup.py


# virtualenv --python=python3.5 .venv
# source .venv/bin/activate