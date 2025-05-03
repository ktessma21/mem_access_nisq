import re

# Helper methods

def read_QASM_file(filename):
    """Read a QASM file and return the lines as a list of strings"""
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines

def read_QASM_line(line):
    """Read a QASM line and return the full gate name and the qubit indices
    
    E.g. 'cx q[0], q[1];' -> 'cx', [0, 1]
    rz(1.7917125) q[14]; -> 'rz', [14]
    """
    
    # capture using regular expression
    # 1. gate name
    # 2. qubit indices
    
    # remove \n if present
    line = line.strip()
    
    if "OPENQASM" in line:
        return None
    
    if "measure" in line:
        return None
    
    if "include" in line:
        return None
    
    if line[:2] == "//":
        return None
    
    if "barrier" in line:
        return None
    
    if " " not in line:
        return None

    gate, targs = line.split(" ", 1)
    
    # split targs by ","
    targ_list = targs.split(",")
    targ_qubits = []
    for i in range(len(targ_list)):
        targ_list[i] = targ_list[i].strip()
        match = re.match(r'[a-zA-Z_0-9]+\[(\d+)\]', targ_list[i])
        
        if match is None:
            print("Invalid QASM line: ", line)
            return ValueError("Invalid QASM line")
        
        targ_qubits.append(int(match.group(1)))
    
    # return the gate name and the qubit indices
    return gate, targ_qubits

def get_rz_angle(gate_str):
    """Extract the angle from an Rz gate string"""
    # capture using regular expression
    # 1. angle
    
    match = re.match(r'rz\((?P<ANGLE>.+)\)', gate_str)
    
    # attempt to match the line
    if match is None:
        return None
    
    # return the angle
    return float(match.group('ANGLE'))

##### YOUR TURN #####
# Perform the following tasks
# 1. Using the `read_QASM_line` function, get the different gates and qubits used in the QASM file

def get_gates_and_qubits(QASM_lines):
    """Get the different gates and qubits used in the QASM file"""
    gates = []
    qubits = []
    
    for line in QASM_lines:
        gate = read_QASM_line(line)
        if gate is not None:
            gates.append(gate[0])
            qubits += gate[1]
    
    return gates, qubits

# 2. Count the type of each QASM gate used in the file using a dictionary

def count_gates(gates_list):
    """Count the type of each QASM gate used in the file using a dictionary"""
    gate_count = {}

    for gate in gates_list:
        gate_name = re.match(r'(?P<GATE>^[a-zA-Z]+)', gate)
        gate_name = gate_name.group('GATE')
        
        if gate_name is not None:
            if gate_name in gate_count:
                gate_count[gate_name] += 1
            else:
                gate_count[gate_name] = 1
    
    return gate_count

# 3. Count the number of times each qubit is used in the file using a dictionary

def count_qubit_usage(qubits_list):
    """Count the number of times each qubit is used in the file using a dictionary"""
    qubit_count = {}

    for qubit in qubits_list:
        if qubit in qubit_count:
            qubit_count[qubit] += 1
        else:
            qubit_count[qubit] = 1
    
    return qubit_count



    