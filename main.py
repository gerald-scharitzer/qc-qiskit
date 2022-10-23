import qiskit
from qiskit_aer import AerSimulator

circuit = qiskit.QuantumCircuit(2)
circuit.h(0)
circuit.cx(0, 1)
circuit.measure_all()

aersim = AerSimulator()
result = qiskit.execute(circuit, aersim).result()
counts = result.get_counts(0)
print("counts", counts)
