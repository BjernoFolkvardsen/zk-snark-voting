pragma circom 2.0.0;

include "../AndCircuit/circuit.circom";
include "../OrCircuit/circuit.circom";
include "../CommitmentCircuit/circuit.circom";
include "../SetMembershipCircuit/merkleTree.circom";
include "../VoteCircuit/vote.circom";
include "../VoteCircuit/NullVote.circom";


template ZkSnarkProof(num){
    signal input r;
    signal input c_id;
    signal input v;
    signal input t_id;
    signal output pi

    z <== y + num
    out <== x * z
}
component main {public [x]} = ZkSnarkProof(5);