from qiskit import qiskit, QuantumCircuit

# Create a quantum circuit with 1 qubit and 1 classical bit.
qc = QuantumCircuit(2, 2)

# Apply a NOT gate on qubit 0.
qc.x(0)
qc.x(1)
qc.h(0)
# Measure qubit 0.
qc.measure([0,1],[0,1])

job = qiskit.execute(qc, qiskit.BasicAer.get_backend('qasm_simulator'))
print(job.result().get_counts())
