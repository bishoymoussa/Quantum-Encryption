from qubit import *

def superdense_coding():
    print "==========Superdense coding protocol=========="
    print

    a = TwoQubit()

    print

    a.hgate()
    print a

    print "and then with controlled Not gate on the two qubits:"

    a.cnot()
    print a
    x = raw_input("First bit: ")
    while x not in ["0", "1"]:
        print "Wrong input (0 or 1 only)"
        x = raw_input("First bit: ")

    y = raw_input("Second bit: ")
    while y not in ["0", "1"]:
        print "Wrong input (0 or 1 only)"
        y = raw_input("Second bit: ")

    x = int(x)
    y = int(y)

    print
    if x == 0 and y == 0:
        print "For encoding 00, nothing is done (I gate is applied)"
    elif x == 0 and y == 1:
        print "For encoding 01, the X (NOT) gate is applied"
        a.xgate()
    elif x == 1 and y == 0:
        print "For encoding 10, the Z gate is applied"
        a.zgate()
    else:
        print "For encoding 11, the X and Z gates are applied"
        a.xgate().zgate()

    print a
    print

    print "First a controlled Not:"
    a.cnot()
    print a

    print "first Qubit:"
    a.hgate()
    print a

    print

    res = a.measure()
    print "The result of Bob's measurement is", res, ", Alice's two bits."

if __name__ == '__main__':
    superdense_coding()
