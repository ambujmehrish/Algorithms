#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 18:25:06 2020

@author: root
"""
def karatsuba(x,y):
    if len(str(x)) ==1 or len(str(y)) == 1:
        return x*y
    else:
        n = max(len(str(x)),len(str(y)))
        nby2 = n//2
        a = x //10**(nby2)
        b = x % 10**(nby2)
        c = x//10**(nby2)
        d = x %10**(nby2)
        
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        ad_plus_bc = karatsuba((a+b), (c+d)) - ac - bd
        
        
        prod = ac*10**(2*nby2) + (ad_plus_bc*10**nby2) + bd
        
        return prod
    
    
    
print(karatsuba(1302334, 190943))