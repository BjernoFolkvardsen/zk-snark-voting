pragma circom 2.1.6;

include "full_circuit.circom";
component main {public [pk_t, g, e_v, cr_id, pathIndices, siblings, root]} = ZkSnarkProof(3);