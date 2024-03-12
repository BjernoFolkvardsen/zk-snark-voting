from pyseidon.constants import Constants
# This implementation of Poseidon is based on the js implementation poseidon-lite: https://github.com/vimwitch/poseidon-lite/tree/main

class Poseidon:
    F = 21888242871839275222246405745257275088548364400416034343698204186575808495617
    N_ROUNDS_F = 8
    N_ROUNDS_P = [56, 57, 56, 60, 60, 63, 64, 63, 60, 66, 60, 65, 70, 60, 64, 68]

    @staticmethod
    def pow5(v):
        o = v * v
        return (v * o * o) % Poseidon.F


    @staticmethod
    def mix(state, M):
        out = []
        for x in range(len(state)):
            o = 0
            for y in range(len(state)):
                o = o + int(M[x][y],0) * state[y]
            out.append(o % Poseidon.F)
        return out

    @staticmethod
    def hash(inputs): 
        inputs = [int(i) for i in inputs]
        if len(inputs) <= 0:
            raise ValueError('poseidon-lite: Not enough inputs')
        if len(inputs) > len(Poseidon.N_ROUNDS_P):
            raise ValueError('poseidon-lite: Too many inputs')

        t = len(inputs) + 1
        nRoundsF = Poseidon.N_ROUNDS_F
        nRoundsP = Poseidon.N_ROUNDS_P[t - 2]

        constants = Constants(t)
        M = constants.POSEIDON_M()
        C = constants.POSEIDON_C()

        if len(M) != t:
            raise ValueError(
                f'poseidon-lite: Incorrect M length, expected {t} got {len(M)}'
            )

        state = [0] + inputs
        # print(state)
        # print(len(C))
        for x in range(nRoundsF + nRoundsP):
            for y in range(len(state)):
                # print(x * t + y)
                state[y] = state[y] + int(C[x * t + y],0)
                if x < (nRoundsF // 2) or x >= (nRoundsF // 2 + nRoundsP):
                    state[y] = Poseidon.pow5(state[y])
                elif y == 0:
                    state[y] = Poseidon.pow5(state[y])
            state = Poseidon.mix(state, M)
        return state[0]

