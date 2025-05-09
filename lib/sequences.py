#!/usr/bin/env python3

def print_fibonacci(length):
    fib = []
    if length > 0:
        fib.append(0)
    if length > 1:
        fib.append(1)
    for i in range(2, length):
        fib.append(fib[i-1] + fib[i-2])
    print(f"{fib}")

    pass