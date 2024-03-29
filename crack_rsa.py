# Find p & q for a given product p.q = N
import sys
from prime_factors import prime_factors_gen
from gcd import gcd
import random
from math import floor

sys.set_int_max_str_digits(100000)

def guess_g(N):
    return random.randrange(floor(N/2))

def select_g_with_no_common_factors_of(N):
    # g must be even
    g = 1
    while g % 2 != 0:
        g = guess_g(N)    
        print(f'g: {g}')

    g1 = g + 1
    g2 = g - 1
    print(f'g: {g} g1: {g1} g2: {g2}')
    if gcd(N, g) == 1:
        return g
    elif gcd(N, g2) == 1:
        return g2
    return 0

def calculate_gr_modN_eq_1(N, g):
    r = 1
    modN = 0
    while modN != 1:
        gr = g**r        
        modN = (gr) % N
        if gr == 0 and modN == 0:
            break
        print(f'g**r: {gr} modN: {modN}')
        if modN == 1:
            return r
        r += 1

def factor_out_p_and_q(N, g, r):
    p = -1
    q = -1
    try:
        gr = g**(r/2)
    except OverflowError:
        return p, q
    
    value1 = gr+1
    modulo = N
    while int(p) != 0:
        r1 = value1 % modulo
        # print(f'r1: {value1} % {modulo} = {r1}')
        if r1 == 0:
            p = int(modulo)
            print(f'p: {p}')
            break
        else:
            value1 = modulo
            modulo = r1

    value2 = gr-1
    modulo = N
    while int(q) != 0:
        r2 = value2 % modulo
        # print(f'r2: {value2} % {modulo} = {r2}')
        if r2 == 0:
            q = int(modulo)
            print(f'q: {q}')
            break
        else:
            value2 = modulo
            modulo = r2
    
    return p, q

def crack(N):    
    # print(f'N: {N}')
    p = 1
    q = 1
    while (p <= 1 or q <= 1) or (p*q != N):
        g = select_g_with_no_common_factors_of(N)
        r = calculate_gr_modN_eq_1(N, g)
        if r and r > 1:
            p, q = factor_out_p_and_q(N, g, r)

    print(f'N: {N} g: {g} r: {r} p: {p} q: {q}')

if __name__ == "__main__" and len(sys.argv) > 0:
    crack(int(sys.argv[1]))