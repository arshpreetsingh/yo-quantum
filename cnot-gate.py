from qiskit import qiskit, QuantumCircuit

# Create a quantum circuit with 1 qubit and 1 classical bit.
qc = QuantumCircuit(3, 3)

# Apply a NOT gate on qubit 0.
qc.t(range(3))

# Measure qubit 0.
qc.measure(range(3), range(3))

job = qiskit.execute(qc, qiskit.BasicAer.get_backend('qasm_simulator'))
print(job.result().get_counts())
