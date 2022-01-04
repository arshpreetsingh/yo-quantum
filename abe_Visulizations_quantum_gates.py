### Here we will learn 4 Ways to represent a uantum-Circuit.
# 1. By Describing the Circuit and using draw method. (Matplotlib)
# Describe using Matirces, [0,1] or [1,0] (Using Matrices)
# By Plotting the Bloch Sphere. (By showing on loch Sphere)
# By Running a circuit on Measurement and Looking for measurements. (Using Histogram!)

import matplotlib
from matplotlib import pyplot
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, execute
from qiskit.tools.visualization import plot_bloch_vector, plot_bloch_multivector, plot_histogram

circuit = QuantumCircuit(1,1)
#circuit.h(0)
circuit.x(0)
#circuit.x(0)
simulator = Aer.get_backend("statevector_simulator")
result = execute(circuit, backend=simulator).result()
state_vector = result.get_statevector()
print(state_vector) # Will return Following, X Applied on State |0> becomes |1>
'''
Statevector([0.+0.j, 1.+0.j],
            dims=(2,))
'''
#circuit.draw(output='mpl')
plot_bloch_multivector(state_vector)
#plot_bloch_multivector(circuit)


circuit.measure(0,0)
simulator = Aer.get_backend("qasm_simulator")
result = execute(circuit, backend=simulator, shots=1024).result()
counts = result.get_counts()
plot_histogram(counts)
pyplot.show()

# Get unitary

simulator = Aer.get_backend("unitary_simulator")
result = execute(circuit, backend=simulator).result()
unitary_vector = result.get_unitary()
print("unitary")
print(unitary_vector) # Will return Following, X Applied on State |0> becomes |1>
"""
Operator([[0.+0.j, 1.+0.j],
          [1.+0.j, 0.+0.j]],
         input_dims=(2,), output_dims=(2,))
"""