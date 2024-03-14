pragma circom 2.0.0;

include "../../node_modules/circomlib/circuits/poseidon.circom";
include "../../node_modules/circomlib/circuits/mux1.circom";

template MerkleTreeInclusionProof(nLevels) {
    signal input leaf;
    signal input pathIndices[nLevels];
    signal input siblings[nLevels];
    signal input root;
    signal output out;

    component poseidons[nLevels];
    component mux[nLevels];

    component poseidon = Poseidon(2);
    poseidon.inputs[0] <== leaf;
    poseidon.inputs[1] <== 0;
    // log("poseidon hashed leaf: ", poseidon.out);

    signal hashes[nLevels + 1];
    hashes[0] <== poseidon.out;

    for (var i = 0; i < nLevels; i++) {
        pathIndices[i] * (1 - pathIndices[i]) === 0;

        poseidons[i] = Poseidon(2);
        mux[i] = MultiMux1(2);

        mux[i].c[0][0] <== hashes[i];
        mux[i].c[0][1] <== siblings[i];

        mux[i].c[1][0] <== siblings[i];
        mux[i].c[1][1] <== hashes[i];

        mux[i].s <== pathIndices[i];

        poseidons[i].inputs[0] <== mux[i].out[0];
        poseidons[i].inputs[1] <== mux[i].out[1];

        hashes[i + 1] <== poseidons[i].out;
    }
    // log("root", root);
    // log("hashes[nLevels]", hashes[nLevels]);
    root === hashes[nLevels];

    out <== 1;

    signal dummy;
    dummy <== leaf * root;

}