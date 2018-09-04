def DivisionEntera(dividendo, divisor):
    cociente=0
    resto=0
    while dividendo >=divisor:
        dividendo= dividendo-divisor
        cociente=cociente+1
    resto=dividendo
    print(dividendo,resto)
