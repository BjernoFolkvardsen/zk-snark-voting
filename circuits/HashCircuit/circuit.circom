pragma circom 2.0.0;

include "../../node_modules/circomlib/circuits/sha256/sha256_2.circom";

template Main() {
    signal input c_id;
    signal input cr_id;
    signal input t_id;
    signal output out;

    component sha256_2 = Sha256_2();

    sha256_2.a <== cr_id;
    log("sha256_2.a /cr_id", sha256_2.a);
    sha256_2.b <== t_id;
    log("sha256_2.b/t_id", sha256_2.b);
    log("sha256_2.out", sha256_2.out);
    log("c_id", c_id);
    c_id === sha256_2.out;
    out <== sha256_2.out;
}

component main = Main();