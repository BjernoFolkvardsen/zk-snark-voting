pragma circom 2.1.6;
include "../node_modules/circomlib/circuits/comparators.circom";

template CalculateTotal(N) {
    signal input in[N];
    signal output out;

    signal outs[N];
    outs[0] <== in[0];

    for (var i=1; i < N; i++) {
        outs[i] <== outs[i - 1] + in[i];
    }

    out <== outs[N - 1];
}

template AtIndex(N) {
    signal input array[N];
    signal input index;

    signal output out;

    component result = CalculateTotal(N);
    for (var i = 0; i < N; i++) {
        // Check if i == index
        var isEqual = IsEqual()([i, index]); 
        // Pass the element in as non-zero value if isEqual == true
        result.in[i] <== isEqual * array[i]; 
    }

    out <== result.out; // Return the 
}


template schnorr(n) {
   // Lets us build a circuit that checks if the input x such that h=g^x
   signal input h;
   signal input g;
   signal input r;
   signal input e;
   signal input x;
   signal h_final;
   signal g_array[n];
   signal h_array[n];
   
   g_array[0] <== g;
   h_array[0] <== h;
   for (var i = 1; i<n; i++) {
      g_array[i] <== g_array[i-1] * g;
      h_array[i] <== h_array[i-1] * h;
   }

   component a = AtIndex(n);
   a.array <== g_array;
   a.index <== r-1;
   //a.out === a=g^r

   component g_z = AtIndex(n);
   g_z.array <== g_array;
   g_z.index <== (x * e + r)-1;
   //g_z.out === g^z

   component h_e = AtIndex(n);
   h_e.array <== h_array;
   h_e.index <== e-1;
   //h_e.out === h^e
   
   //h^e * a
   h_final <== h_e.out * a.out;
   
   //h^e * a = g^z
   h_final === g_z.out;
}

component main {public [g, h, r, e]} = schnorr(100);

