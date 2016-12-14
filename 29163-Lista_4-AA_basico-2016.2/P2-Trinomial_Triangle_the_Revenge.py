def modularPower(base, power, module):
    if (power == 0):
        return 1
    result = modularPower(base, power / 2, module)
    
    result = (result * result) % module
    if (power % 2 == 1):
        result = (base * result) % module

    return int(result)

print modularPower(3, int(raw_input()), 2147483647)
