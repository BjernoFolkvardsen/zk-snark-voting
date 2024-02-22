pragma circom 2.0.0;

template ZkSnarkProof(num){
    // dummy code
    signal input x;
    signal input y;
    signal output out

    z <== y + num
    out <== x * z
}
component main {public [x]} = ZkSnarkProof(5);