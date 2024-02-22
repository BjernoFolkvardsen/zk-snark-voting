pragma circom 2.0.0;

template isBinary () {
   //Declaration of signals.
   signal input in;
   signal output out;

   //Statements.
   out <== in * (in-1) === 0;
}

template Multiplier2 () {

   // Declaration of signals.
   signal input in1;
   signal input in2;
   signal output c;

   // Constraints.
   c <== in1 * in2;
}

template OrCircuit(){
    signal input a;
    signal input b;
    signal input c;
    signal output out;

    component mult = Multiplier2;
    component isBin = isBinary;

    mult.in1 <== a;
    mult.in2 <== b;
    isBin.in <== c;

    multIs20 <== mult.out === 20;
    out <== isBin.out || multIs20;
}
component main = OrCircuit();