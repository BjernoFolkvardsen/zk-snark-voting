pragma circom 2.1.6;
include "../../node_modules/circomlib/circuits/poseidon.circom";


template PoseidonHash() {
    signal input c_id;
    signal input cr_id;
    signal input t_id;
    
    component hash = Poseidon(2);
    hash.inputs[0] <== cr_id;
    hash.inputs[1] <== t_id;

    c_id === hash.out;
    

    signal dummy;
    dummy <== cr_id * t_id;
}

component main { public [ c_id, cr_id ] } = PoseidonHash();