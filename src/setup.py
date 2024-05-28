from Crypto.PublicKey import ECC
from Crypto.Signature import eddsa
from zkpy.ptau import PTau
from zkpy.circuit import Circuit, GROTH
from src.bulletinboard import BullitinBoard
from src.utility import Utility
import os
import shamirs

class SetupManager:

    bb: BullitinBoard = None

    def __init__(self, bb: BullitinBoard):
        self.bb = bb
        self.setup()

    def setup(self):
        (pk,sk,p,g) = self.setup_elgamal()
        shares = self.get_shamirs_shares(10,20,sk,p)
        self.setup_digital_signature()
        self.setup_zk_SNARK()
        self.setup_commitment_params(p)

    def setup_elgamal(self):

        ElGamalKey = Utility.generateElGamal()

        public_elgamal_params = {
            'public_key':str(ElGamalKey.y),
            'prime': str(ElGamalKey.p),
            'group': str(ElGamalKey.g)
        }
        self.bb.set_public_params("elgamal",public_elgamal_params)
        self.bb.set_private_param("elgamal_priv_key", str(ElGamalKey.x))
        return (ElGamalKey.y, ElGamalKey.x, ElGamalKey.p, ElGamalKey.g)

    def get_shamirs_shares(self,threshold,share_num,sk,p):
        shares = shamirs.shares(sk.__int__(), quantity=share_num, modulus=p.__int__(), threshold=threshold)
        return shares

    def setup_digital_signature(self):
        signing_key = ECC.generate(curve='ed25519')
        verification_key = eddsa.import_public_key(signing_key.public_key().export_key(format='raw'))

        self.bb.set_public_params("digital_signature_verification_key",verification_key.export_key(format='OpenSSH'))
        self.bb.set_private_param("signing_key", signing_key.export_key(format='PEM'))
        return (signing_key,verification_key)

    def setup_commitment_params(self,p):
        self.bb.set_public_params("T_from", str(2))
        self.bb.set_public_params("T_to", str(p-1))
        self.bb.set_public_params("CR_from", str(2))
        self.bb.set_public_params("CR_to", str(p-1))

    def setup_zk_SNARK(self):
        eligible_voters = self.bb.get_eligible_voters()
        Utility.set_max_voters_and_mtree_depth(len(eligible_voters))
        if Utility.MTREE_DEPTH > 30:
            raise Exception("Too many voters for the zk-SNARK proof. The maximum number of voters is 2^30.")
        working_dir = os.path.dirname(os.path.realpath(__file__)) + "/../circuits/FullCircuit/"
        ptau = PTau(ptau_file=working_dir+"../ptau_13.ptau")
        # Create the circuit from the template with the correct depth of the merkle tree
        with open(working_dir+"circuit.txt") as f:
            with open(working_dir+"circuit.circom", "w") as f1:
                for line in f:
                    f1.write(line)
                f1.write("component main {public [pk_t, g, e_v, cr_id, pathIndices, siblings, root]} = ZkSnarkProof("+str(Utility.MTREE_DEPTH)+");")

        circuit = Circuit("circuit.circom", working_dir=working_dir,output_dir=working_dir)
        circuit.compile()
        circuit.setup(GROTH, ptau)
        circuit.contribute_phase2(entropy="p1", output_file=working_dir+"final.zkey")
        circuit.export_vkey(output_file=working_dir+"../../tmp/vkey.json")
        self.bb.set_zkey_file_name(circuit.zkey_file)
