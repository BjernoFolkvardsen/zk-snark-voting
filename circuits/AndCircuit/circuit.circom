pragma circom 2.0.0;

template binaryCheck () {
   //Declaration of signals.
   signal input in;
   signal output out;

   //Statements.
   in * (in-1) === 0;
   out <== in;
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
    // dummy code
    signal input a;
    signal input b;
    signal input c;
    signal output out

    component mult = Multiplier2;
    component binCheck = binaryCheck;

    mult.in1 = a
    mult.in2 = b
    binCheck.in = c

    out <== binCheck.out && mult.out
}
component main = OrCircuit();