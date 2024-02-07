from Crypto.PublicKey import ElGamal, ECC
from Crypto.Random import get_random_bytes
from Crypto.Signature import eddsa
from Crypto.Hash import SHA256
from zkpy.ptau import PTau
from zkpy.circuit import Circuit, GROTH
import os
#import subprocess
import shamirs

class SetupManager:
    def __init__(self):
        pass 
    
    def setup(self):
        (pk,sk,p,g) = self.setup_elgamal(256)
        shares = self.get_shamirs_shares(10,20,sk,p)
        self.setup_digital_signature()
        m = b'Hello world!'
        (com,rand) = self.SHA_commit(m)
        print(m)
        print(com)
        print(rand)
        print(self.SHA_commit_verify(com,m,rand))
        #self.setup_zk_SNARK()

    def setup_elgamal(self,keysize):
        ElGamalKey = ElGamal.generate(keysize, get_random_bytes)
        # print("y/publickey:", ElGamalKey.y)
        # print("x/privateKey:", ElGamalKey.x)
        # print("p:", ElGamalKey.p)
        # print("g:", ElGamalKey.g)

        #print(ElGamalKey.x.to_bytes())
        # shares = shamirs.shares(ElGamalKey.x.__int__(), quantity=share_num, modulus=ElGamalKey.p.__int__(), threshold=threshold)
        #print("shares:", shares)
        
        # privateKey = shamirs.interpolate(shares[5:15], threshold=10)
        # print("pk:", privateKey)
        # print("pk:", ElGamalKey.x)
        
        return (ElGamalKey.y, ElGamalKey.x, ElGamalKey.p, ElGamalKey.g)

    def get_shamirs_shares(self,threshold,share_num,sk,p):
        shares = shamirs.shares(sk.__int__(), quantity=share_num, modulus=p.__int__(), threshold=threshold)
        return shares

    def setup_digital_signature(self):
        signing_key = ECC.generate(curve='ed25519')
        verification_key = eddsa.import_public_key(signing_key.public_key().export_key(format='raw'))

        # message = b'Hello, World!'
        # message1 = b'Hello, World!'
        # signer = eddsa.new(signing_key, 'rfc8032')
        # verifier = eddsa.new(verification_key,'rfc8032')
        # h = signer.sign(message)
        # print(verifier.verify(message1,h))
        # print("sign: ", signer)
        # print("verify: ", verifier)
        # print(DSS.DssSigScheme.can_sign(sign))

        return (signing_key,verification_key)

    def SHA_commit(self,m):
        random = get_random_bytes(256)
        commitment = SHA256.new(random+m)
        return (commitment.hexdigest(),random)

    def SHA_commit_verify(self,com,m,key):
        return com == SHA256.new(key+m).hexdigest()
        

    def setup_zk_SNARK(self):
        working_dir = os.path.dirname(os.path.realpath(__file__)) + "/../circom4/"
        ptau = PTau(working_dir=working_dir)
        ptau.start(constraints='15')
        ptau.contribute()
        ptau.beacon()
        ptau.prep_phase2()

        # Args:
        #     circ_file (str): Path to a circom circuit file.
        #     output_dir (str, optional): Path to where generated files should be outputted. Defaults to the current directory.
        #     working_dir (str, optional): Path that all given file paths are relative to. Defaults to the current directory
        #     r1cs (str, optional): Optional path to a pre-generated r1cs file.
        #     sym_file (str, optional): Optional path to a pre-generated symbols file.
        #     js_dir (str, optional): Optional path to a pre-generated directory with JS files.
        #     wasm (str, optional): Optional path to a pre-generated wasm file.
        #     witness (str, optional): Optional path to a witness file.
        #     zkey (str, optional): Optional path to a pre-generated zkey file.
        #     vkey (str, optional): Optional path to a pre-generated verification key file.
        circuit = Circuit("circuit.circom", working_dir=working_dir,output_dir=working_dir)
        circuit.compile()
        circuit.get_info()
        circuit.print_constraints()
        circuit.gen_witness(working_dir+"input.json")
        # proc = subprocess.run(
        #         ["snarkjs", "plonk", "setup", working_dir+"circuit.r1cs", ptau.ptau_file, working_dir+"key.zkey"],
        #         shell=True,
        #         capture_output=True,
        #         cwd=working_dir,
        #         check=True,
        # )
        # print(proc.stdout.decode('utf-8'))
        circuit.setup(GROTH, ptau)
        circuit.contribute_phase2(entropy="p1")
        circuit.prove(GROTH)
        circuit.export_vkey(output_file=working_dir+"vkey.json")
        circuit.verify(GROTH, vkey_file=working_dir+"vkey.json", public_file=working_dir+"public.json", proof_file=working_dir+"proof.json")


if __name__ == "__main__":
    setup_manager = SetupManager()
    setup_manager.setup()