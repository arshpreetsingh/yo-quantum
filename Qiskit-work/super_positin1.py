from math import sqrt
from qiskit import *
qc = QuantumCircuit(1)
state_vector = [0.+1.j/sqrt(2), 1/sqrt(2)+0.j]
qc.initialize(state_vector, 0)
#qc.h(0)
qc.measure_all()

sim = Aer.get_backend('aer_simulator')
qc.save_statevector()
qobj = assemble(qc)
state = sim.run(qobj).result().get_statevector()
print(str(state))
