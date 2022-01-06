from qiskit import qiskit, QuantumCircuit

# Create a quantum circuit with 1 qubit and 1 classical bit.
qc = QuantumCircuit(1, 1)

# Apply a NOT gate on qubit 0.
qc.h(0) # Apply H-Gate! to get Super-Positions!

# Measure qubit 0.
qc.measure(0, 0)

job = qiskit.execute(qc, qiskit.BasicAer.get_backend('qasm_simulator'))
print(job.result().get_counts())
