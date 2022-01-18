from math import sqrt
from qiskit import *
qc = QuantumCircuit(2,2)
#state_vector = [0.+1.j/sqrt(2), 1/sqrt(2)+0.j]
#qc.initialize(state_vector, 0)

# HZH can also be implemented using X-NOT gate or vice-Versa~
qc.h(0)
qc.z(0)
qc.h(0)
#qc.cx(0,1)
qc.measure([0,1],2)

sim = Aer.get_backend('aer_simulator')
qc.save_statevector()
qobj = assemble(qc)
state = sim.run(qobj).result().get_counts()
print(str(state))
