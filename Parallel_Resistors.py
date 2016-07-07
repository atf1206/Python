def resistor_parallel(*args):
    resistance = 0.0
    for x in args:
        resistance += 1.0/x
    return 1.0/resistance
