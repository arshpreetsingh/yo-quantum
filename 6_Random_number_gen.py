from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit, IBMQ, execute
from qiskit.tools.monitor import job_monitor
from read_config import get_api_key

# Connecet with IBM computer.
# Connect with Backend!
IBMQ.enable_account(get_api_key())
provider = IBMQ.get_provider(hub='ibm-q')
backend = provider.get_backend('ibmq_qasm_simulator')

q = QuantumRegister(16, 'q')
c = ClassicalRegister(16,'c')
circuit = QuantumCircuit(q,c)
circuit.h(q) # Will apply Hadmard to all 16 Qubits!
circuit.measure(q,c)
print(circuit)
job = execute(circuit, backend, shots=1)
job_monitor(job)
result = job.result().get_counts()
print("RESULT--->",result)
# RESULT---> {'0010010011101011': 1}
# RESULT---> {'1100010101010011': 1}