pragma circom 2.0.0;
include "elGamalcircuit.circom";

template NullVote(){
    signal input pk_t;
    signal input g;
    signal input e_v[2];
    signal input r;
    // signal output ev1;
    // signal output ev2;

    component encrypt = Encrypt();

    encrypt.r <== r;
    encrypt.g <== g;
    encrypt.y <== pk_t;
    encrypt.m <== 0;
    // log("pk_t", pk_t);
    // log("g", g);
    // log("r", r);
    // log("encrypt.m", encrypt.m);
    // log("encrypt.r", encrypt.r);
    // log("encrypt.g", encrypt.g);
    // log("encrypt.y", encrypt.y);
    // log("e_v[0]", e_v[0]);
    // log("e_v[1]", e_v[1]);
    // log("encrypt.c1", encrypt.c1);
    // log("encrypt.c2", encrypt.c2);
    e_v[0] === encrypt.c1;
    // ev1 <== e_v[0] - encrypt.c1;
    e_v[1] === encrypt.c2;
    // ev2 <== e_v[1] - encrypt.c2;

    signal dummy;
    dummy <== e_v[0] * e_v[1];

}
component main {public [pk_t, g, e_v]} = NullVote();