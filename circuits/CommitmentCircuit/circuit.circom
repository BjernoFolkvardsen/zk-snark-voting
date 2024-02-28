pragma circom 2.0.0;

include "../HashFunctionCircuits/sha2/sha224/sha224_hash_bits.circom";
include "../sha1-circom/circuits/sha1.circom";
include "../../node_modules/circomlib/circuits/bitify.circom";

template Main() {
    signal input c_id;
    signal input cr_id;
    signal input t_id;
    signal input bit_array[32];
    signal output out;
    signal cr_id_t_id;
    signal cr_id_t_id_bits[32];
    signal c_id_out_bits[224];
    signal c_id_out;


    component sha1 = Sha1(32);
    sha1.in <== bit_array;

    for (var i = 0; i < 160; i++) {
        log(sha1.out[i]);
    }

    // component sha224 = Sha224_hash_bits_digest(32);
    // component num2bits = Num2Bits(32);
    // component bits2num = Bits2Num(224);

    // cr_id_t_id <== cr_id + t_id;
    // log(cr_id_t_id);   

    // num2bits.in <== cr_id_t_id;
    // cr_id_t_id_bits <== num2bits.out;
    
    // for (var i = 0; i < 32; i++) {
    //     log(cr_id_t_id_bits[i]);
    // }

    // sha224.inp_bits <== bit_array;
    
    // log("c_id", c_id);

    // component byteToBits[28];
    // for (var i = 0; i < 28; i++) {
    //     byteToBits[i] = Num2Bits(8);
    //     byteToBits[i].in <== sha224.hash_bytes[i];
    //     log("byteToBits[i].in", byteToBits[i].in);
    // }
     
    // for (var i = 0; i < 28; i++) {
    //     for (var j = 0; j < 8; j++) {
    //         c_id_out_bits[i*8+j] <== byteToBits[i].out[7-j];
    //         log("c_id_out_bits[i*8+j]", c_id_out_bits[i*8+j]);
    //     }
    // }
    // bits2num.in <== c_id_out_bits;
    // c_id_out <== bits2num.out;
    // log("c_id_out", c_id_out);
    // c_id === c_id_out;
    // out <-- c_id_out;
}

component main = Main();