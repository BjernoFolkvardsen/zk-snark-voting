# Zk-snark-voting Protocol
## Overview
Welcome to Zk-snark-voting Protocol! This is a Python project that leverages npm packages and the Circom language, which is implemented in Rust. This README will guide you through the setup process and provide essential information about the project.

## Prerequisites
Before you begin, ensure you have the following installed:

- Python (version 3.10)
- npm (version 10.1)
- GNU Make (4.4)
- Docker (v4.30)

## Circom Setup
Before proceeding with the project, you need to set up Circom. Follow these steps:

Check Circom to see how [Circom Installation Guide](https://docs.circom.io/getting-started/installation/%5D(https://docs.circom.io/getting-started/installation/))

### Circum setup in short
#### Installing Dependencies
You need several dependencies in your system to run Circom and its associated tools.

##### Rust
The core tool, the Circom compiler, is written in Rust. Install Rust using rustup. If you're using Linux or macOS, open a terminal and run:

```bash
curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf | sh
```
or use brew

```bash
brew install rust
```

##### Node.js and npm/yarn
Circom also relies on npm packages, so ensure Node.js and a package manager like npm or yarn are available. Install Node.js version 10 or higher.

#### Installing Circom
To install Circom from the source, clone the Circom repository:

```bash
git clone https://github.com/iden3/circom.git
```
Navigate to the Circom directory and use cargo build to compile:

```bash
cd circom
cargo build --release
```
The installation takes approximately 3 minutes. Once complete, the circom binary is generated in the directory target/release. Install this binary:

```bash
cargo install --path circom
```
This command installs the circom binary in the directory $HOME/.cargo/bin.

### Continue with Project Setup
Now that you have set up Circom, continue with the rest of the project setup as mentioned in the main README file.

## Installation
1. Clone the repository:
```bash
git clone https://github.com/BjernoFolkvardsenDev/zk-snark-voting.git
cd zk-snark-voting
```
1. Install python and npm packages:
```bash
make local-setup
```
1. Setup the database
```bash
make setup-db
```
## Usage
1. Start the database docker container
```bash
make start-db
```
1. Run the Python script:
```bash
make clearAndRun
```
## Test
For testing, clone the benchmarking branch. This branch contains existing data for already run tests and the code to reproduce the tests. 
The tests are visible in files app.py, voting.py, and tally.py, each file containing the necessary commands to run the different tests. Simply uncomment the specified lines and run the protocol as specified in the _Usage_ section above. 

For all tests, you must specify the number of voters and candidates to run the protocol with; this is done in app.py. If you wish to test the functions of re-votes and null-votes, these numbers must equally be specified in the app.py file. 

Tests concerning ballot generation, proof generation, and Merkle tree traversal are done in the voting.py file, and the test concerning proof verification is in tally.py.

## Issues
If you encounter any issues or have suggestions, please open an issue [here](https://github.com/BjernoFolkvardsenDev/zk-snark-voting/issues).

## License
[MIT](https://choosealicense.com/licenses/mit/)
