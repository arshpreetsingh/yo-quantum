'''
Grover's Diffusion Operator:> [Oracle]+[Reflection]

Oracle: Oracle is going to Flip the sign of the operator if operator is "Winner"

# We want a gate that Flips the State of the 11 operator. that is Z-Gate in this case.

Amplitude-Amplification: Amplitude Amplification need to learn more!

'''
# Get Required import(s)
from qiskit import *
#import matplotlib.pyplot as plt
import numpy as np

# define Oracle Circuit!
oracle = QuantumCircuit(2,name='oracle')
oracle.cz(0,1) # Applied control-Z gate on Each Qubit!
oracle.to_gate()
print(oracle)
backend = Aer.get_backend("statevector_simulator")

# Now define Grover-Circuit and Add Oracle to it.
grover_cirq = QuantumCircuit(2,2)
grover_cirq.h([0,1])
grover_cirq.append(oracle,[0,1])
print("this is Grover-Cirq!!")
print(grover_cirq)

# Execute Grover-Circuit on Simulator.
job = execute(grover_cirq,backend)
result = job.result()

print(result)

state_vector = result.get_statevector()
print(state_vector)

'''
## What we have done till now!?
1. Prepared the Super-Position state.
2. Got back the Same state but with |11> state Flipped. 

Now we have got state vector, in order to get probability we have 
square the State-vector to get the probability of measure. 

# multiple each Element of State-Vector by multiplying the Hermition-conjucate.!
'''

## Amplitude-Amplification : Maximize the probabilities of Winning state and Minimizing the
## Probabilities of Non-Winning State!
