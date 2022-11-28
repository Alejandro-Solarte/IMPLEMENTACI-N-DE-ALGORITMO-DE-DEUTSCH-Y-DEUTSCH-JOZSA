import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit import Aer
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

###### Funcion numero 1 #######
simulator = Aer.get_backend('qasm_simulator')

circuit = QuantumCircuit(2, 2)

circuit.barrier()
circuit.cx(0,1)
circuit.barrier()


circuit.measure(0,1)
circuit.measure(1,0)

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()

######### Funcion numero 1.2 ###########

simulator = Aer.get_backend('qasm_simulator')

circuit = QuantumCircuit(2, 2)

circuit.x(1)
circuit.barrier()
circuit.cx(0,1)
circuit.barrier()


circuit.measure(0,1)
circuit.measure(1,0)

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()

######### Funcion numero 1.3 ###########

simulator = Aer.get_backend('qasm_simulator')

circuit = QuantumCircuit(2, 2)

circuit.x(0)
circuit.barrier()
circuit.cx(0,1)
circuit.barrier()


circuit.measure(0,1)
circuit.measure(1,0)

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()

######### Funcion numero 1.4 ###########

simulator = Aer.get_backend('qasm_simulator')

circuit = QuantumCircuit(2, 2)

circuit.x(0)
circuit.x(1)
circuit.barrier()
circuit.cx(0,1)
circuit.barrier()


circuit.measure(0,1)
circuit.measure(1,0)

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()

######### Funcion numero 2 ###########

simulator = Aer.get_backend('qasm_simulator')

circuit = QuantumCircuit(2, 2)

circuit.i(0)
circuit.i(1)

circuit.measure(0,1)
circuit.measure(1,0)

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()

######### Funcion numero 2.2 ###########

simulator = Aer.get_backend('qasm_simulator')

circuit = QuantumCircuit(2, 2)

circuit.x(1)
circuit.barrier()
circuit.barrier()


circuit.measure(0,1)
circuit.measure(1,0)

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()

######### Funcion numero 2.3 ###########

simulator = Aer.get_backend('qasm_simulator')

circuit = QuantumCircuit(2, 2)

circuit.x(1)
circuit.x(1)
circuit.barrier()
circuit.barrier()


circuit.measure(0,1)
circuit.measure(1,0)

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()

######### Funcion numero 2.4 ###########

simulator = Aer.get_backend('qasm_simulator')

circuit = QuantumCircuit(2, 2)

circuit.x(0)
circuit.x(1)
circuit.barrier()
circuit.barrier()


circuit.measure(0,1)
circuit.measure(1,0)

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()

######### Funcion numero 3 ###########

simulator = Aer.get_backend('qasm_simulator')

circuit = QuantumCircuit(2, 2)

circuit.x(0)
circuit.x(1)
circuit.x(1)
circuit.barrier()
circuit.barrier()


circuit.measure(0,1)
circuit.measure(1,0)

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()

######### Primer circuito ###########

simulator = Aer.get_backend('qasm_simulator')

circuit = QuantumCircuit(2, 2)

circuit.h(0)
circuit.x(1)
circuit.h(1)
circuit.barrier()
circuit.cx(0,1)
circuit.barrier()
circuit.h(0)

circuit.measure(0,0)

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()

######### Segundo circuito ###########

simulator = Aer.get_backend('qasm_simulator')

circuit = QuantumCircuit(2, 2)

circuit.h(0)
circuit.x(1)
circuit.h(1)
circuit.barrier()
circuit.barrier()
circuit.h(0)

circuit.measure(0,0)

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()

######### Tercer circuito ###########

simulator = Aer.get_backend('qasm_simulator')

circuit = QuantumCircuit(2, 2)

circuit.h(0)
circuit.x(1)
circuit.h(1)
circuit.barrier()
circuit.x(1)
circuit.barrier()
circuit.h(0)

circuit.measure(0,0)

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()

######### Cuarto circuito ###########

simulator = Aer.get_backend('qasm_simulator')

circuit = QuantumCircuit(2, 2)

circuit.h(0)
circuit.x(1)
circuit.h(1)
circuit.barrier()
circuit.x(0)
circuit.cx(0,1)
circuit.x(0)
circuit.barrier()
circuit.h(0)

circuit.measure(0,0)

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()


################# Funcion Deutsch-Jozsa 1 #################

simulator = Aer.get_backend('qasm_simulator')

circuit = QuantumCircuit(2, 2)


qreg_q = QuantumRegister(4, 'q')
creg_c = ClassicalRegister(4, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)





circuit.barrier()
circuit.x(2)
circuit.barrier()


circuit.measure(0,2)
circuit.measure(1, 1)
circuit.measure(2, 0)

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()


################# Funcion Deutsch-Jozsa 1.2 #################

simulator = Aer.get_backend('qasm_simulator')

circuit = QuantumCircuit(2, 2)


qreg_q = QuantumRegister(4, 'q')
creg_c = ClassicalRegister(4, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)




circuit.x(2)
circuit.barrier()
circuit.x(2)
circuit.barrier()


circuit.measure(0,2)
circuit.measure(1, 1)
circuit.measure(2, 0)

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()

################# Funcion Deutsch-Jozsa 1.3 #################

simulator = Aer.get_backend('qasm_simulator')

circuit = QuantumCircuit(2, 2)


qreg_q = QuantumRegister(4, 'q')
creg_c = ClassicalRegister(4, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)




circuit.x(1)
circuit.barrier()
circuit.x(2)
circuit.barrier()


circuit.measure(0,2)
circuit.measure(1, 1)
circuit.measure(2, 0)

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()

################# Funcion Deutsch-Jozsa 1.4 #################

simulator = Aer.get_backend('qasm_simulator')

circuit = QuantumCircuit(2, 2)


qreg_q = QuantumRegister(4, 'q')
creg_c = ClassicalRegister(4, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)



circuit.x(1)
circuit.x(2)
circuit.barrier()
circuit.x(2)
circuit.barrier()


circuit.measure(0,2)
circuit.measure(1, 1)
circuit.measure(2, 0)

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()

################# Funcion Deutsch-Jozsa 1.b #################

simulator = Aer.get_backend('qasm_simulator')

circuit = QuantumCircuit(2, 2)


qreg_q = QuantumRegister(4, 'q')
creg_c = ClassicalRegister(4, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)




circuit.x(0)
circuit.barrier()
circuit.x(2)
circuit.barrier()


circuit.measure(0,2)
circuit.measure(1, 1)
circuit.measure(2, 0)

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()

################# Funcion Deutsch-Jozsa 1.b #################

simulator = Aer.get_backend('qasm_simulator')

circuit = QuantumCircuit(2, 2)


qreg_q = QuantumRegister(4, 'q')
creg_c = ClassicalRegister(4, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)



circuit.x(0)
circuit.x(2)
circuit.barrier()
circuit.x(2)
circuit.barrier()


circuit.measure(0,2)
circuit.measure(1, 1)
circuit.measure(2, 0)

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()

################# Funcion Deutsch-Jozsa 1.b #################

simulator = Aer.get_backend('qasm_simulator')

circuit = QuantumCircuit(2, 2)


qreg_q = QuantumRegister(4, 'q')
creg_c = ClassicalRegister(4, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)



circuit.x(0)
circuit.x(1)
circuit.barrier()
circuit.x(2)
circuit.barrier()


circuit.measure(0,2)
circuit.measure(1, 1)
circuit.measure(2, 0)

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()

################# Funcion Deutsch-Jozsa 1.b #################

simulator = Aer.get_backend('qasm_simulator')

circuit = QuantumCircuit(2, 2)


qreg_q = QuantumRegister(4, 'q')
creg_c = ClassicalRegister(4, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)



circuit.x(0)
circuit.x(1)
circuit.x(2)
circuit.barrier()
circuit.x(2)
circuit.barrier()


circuit.measure(0,2)
circuit.measure(1, 1)
circuit.measure(2, 0)

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()

################# Funcion Deutsch-Jozsa 2 #################

simulator = Aer.get_backend('qasm_simulator')

circuit = QuantumCircuit(2, 2)


qreg_q = QuantumRegister(4, 'q')
creg_c = ClassicalRegister(4, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)



circuit.barrier()
circuit.cx(0,2)
circuit.cx(1,2)
circuit.barrier()


circuit.measure(0,2)
circuit.measure(1, 1)
circuit.measure(2, 0)

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()

################# Funcion Deutsch-Jozsa 2.1 #################

simulator = Aer.get_backend('qasm_simulator')

circuit = QuantumCircuit(2, 2)


qreg_q = QuantumRegister(4, 'q')
creg_c = ClassicalRegister(4, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)


circuit.x(2)
circuit.barrier()
circuit.cx(0,2)
circuit.cx(1,2)
circuit.barrier()


circuit.measure(0,2)
circuit.measure(1, 1)
circuit.measure(2, 0)

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()

################# Funcion Deutsch-Jozsa 2.2 #################

simulator = Aer.get_backend('qasm_simulator')

circuit = QuantumCircuit(2, 2)


qreg_q = QuantumRegister(4, 'q')
creg_c = ClassicalRegister(4, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)


circuit.x(1)
circuit.barrier()
circuit.cx(0,2)
circuit.cx(1,2)
circuit.barrier()


circuit.measure(0,2)
circuit.measure(1, 1)
circuit.measure(2, 0)

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()

################# Funcion Deutsch-Jozsa 2.3 #################

simulator = Aer.get_backend('qasm_simulator')

circuit = QuantumCircuit(2, 2)


qreg_q = QuantumRegister(4, 'q')
creg_c = ClassicalRegister(4, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)


circuit.x(1)
circuit.x(2)
circuit.barrier()
circuit.cx(0,2)
circuit.cx(1,2)
circuit.barrier()


circuit.measure(0,2)
circuit.measure(1, 1)
circuit.measure(2, 0)

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()

################# Funcion Deutsch-Jozsa 2.b #################

simulator = Aer.get_backend('qasm_simulator')

circuit = QuantumCircuit(2, 2)


qreg_q = QuantumRegister(4, 'q')
creg_c = ClassicalRegister(4, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)


circuit.x(0)
circuit.barrier()
circuit.cx(0,2)
circuit.cx(1,2)
circuit.barrier()


circuit.measure(0,2)
circuit.measure(1, 1)
circuit.measure(2, 0)

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()

################# Funcion Deutsch-Jozsa 2.b #################

simulator = Aer.get_backend('qasm_simulator')

circuit = QuantumCircuit(2, 2)


qreg_q = QuantumRegister(4, 'q')
creg_c = ClassicalRegister(4, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)


circuit.x(0)
circuit.x(2)
circuit.barrier()
circuit.cx(0,2)
circuit.cx(1,2)
circuit.barrier()


circuit.measure(0,2)
circuit.measure(1, 1)
circuit.measure(2, 0)

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()

################# Funcion Deutsch-Jozsa 2.b #################

simulator = Aer.get_backend('qasm_simulator')

circuit = QuantumCircuit(2, 2)


qreg_q = QuantumRegister(4, 'q')
creg_c = ClassicalRegister(4, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.x(0)
circuit.x(1)
circuit.barrier()
circuit.cx(0,2)
circuit.cx(1,2)
circuit.barrier()


circuit.measure(0,2)
circuit.measure(1, 1)
circuit.measure(2, 0)

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()

################# Funcion Deutsch-Jozsa 2.b #################

simulator = Aer.get_backend('qasm_simulator')

circuit = QuantumCircuit(2, 2)


qreg_q = QuantumRegister(4, 'q')
creg_c = ClassicalRegister(4, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.x(0)
circuit.x(1)
circuit.x(2)
circuit.barrier()
circuit.cx(0,2)
circuit.cx(1,2)
circuit.barrier()


circuit.measure(0,2)
circuit.measure(1, 1)
circuit.measure(2, 0)

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()

################# Funcion Deutsch-Jozsa constante o balanceada #################

simulator = Aer.get_backend('qasm_simulator')

circuit = QuantumCircuit(2, 2)


qreg_q = QuantumRegister(4, 'q')
creg_c = ClassicalRegister(4, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.h(0)
circuit.h(1)
circuit.x(2)
circuit.h(2)
circuit.barrier()
circuit.cx(0,2)
circuit.cx(1,2)
circuit.barrier()
circuit.h(0)
circuit.h(1)

circuit.measure(0,1)
circuit.measure(1, 0)


compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()
