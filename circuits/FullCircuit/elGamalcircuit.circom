pragma circom 2.0.0;

template Encrypt(){
    // signal input m;
    signal input r;
    signal input g;
    signal input y;
    signal output c1;
    signal output c2;
    // signal c2_1;
    // signal c2_2;


    c1 <-- g**r;

    // c2_1 <-- g**m;

    // c2_2 <-- y**r;

    c2 <-- y**r;
}
