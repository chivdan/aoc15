import re
import numpy as np
import copy

def solve(part1: bool):
    inst = {}
    for line in open("input.txt"):
        lhs, rhs = line.strip().split(" -> ")
        lhs = lhs.strip().split()
        if len(lhs) == 3:
            op = lhs[1]
            if op == "AND":
                op = lambda a, b: a & b
            elif op == "OR":
                op = lambda a, b: a | b
            elif op == "LSHIFT":
                op = lambda a, b: a << b
            elif op == "RSHIFT":
                op = lambda a, b: a >> b
                
            a, b = lhs[0], lhs[2]
            if re.match("[0-9]+", a):
                inst[a] = int(a)

            if re.match("[0-9]+", b):
                inst[b] = int(b)

            inst[rhs] = (op, a, b)
        elif len(lhs) == 2:
            if lhs[0] != "NOT":
                raise RuntimeError()
            inst[rhs] = (lambda x: ~x, lhs[1])
        elif len(lhs) == 1:
            if re.match("[0-9]+", lhs[0]):
                inst[rhs] = int(lhs[0]) 
            else:
                inst[rhs] = lhs[0]

    inst_copy = copy.deepcopy(inst)
   
    def simulate():
        while True:
            if isinstance(inst["a"], int):
                break
            if all(isinstance(inst[k], int) for k in inst):
                break
            for k, v in inst.items():
                if isinstance(v, int):
                    continue
                if isinstance(v, str):
                    if isinstance(inst[v], int):
                        inst[k] = inst[v]
                        break
                    else:
                        continue
                if all(isinstance(inst[operand], int) for operand in v[1:]):
                    op = v[0]
                    inst[k] = op(*[inst[operand] for operand in v[1:]]) & 0xFFFF
                    break
 
    simulate()
    if part1:
        print(inst["a"])
    else:
        b_input = inst["a"]
        inst = inst_copy
        inst["b"] = b_input
        simulate()
        print(inst["a"])
        

if __name__ == '__main__':
    solve(True)
    solve(False)
