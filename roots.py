#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# file roots.py
def quad_roots(a=1.0, b=2.0, c=0.0):
    """Returns the roots of a quadratic equation: ax^2 + bx + c = 0.
    
    INPUTS
    =======
    a: float, optional, default value is 1
       Coefficient of quadratic term
    b: float, optional, default value is 2
       Coefficient of linear term
    c: float, optional, default value is 0
       Constant term
    
    RETURNS
    ========
    roots: 2-tuple of complex floats
       Has the form (root1, root2) unless a = 0 
       in which case a ValueError exception is raised
    
    EXAMPLES
    =========
    >>> quad_roots(1.0, 1.0, -12.0)
    ((3+0j), (-4+0j))
    """
    import cmath # Can return complex numbers from square roots
    if a == 0:
        raise ValueError("The quadratic coefficient is zero.  This is not a quadratic equation.")
    else:
        sqrtdisc = cmath.sqrt(b * b - 4.0 * a * c)
        r1 = -b + sqrtdisc
        r2 = -b - sqrtdisc
        twoa = 2.0 * a
        return (r1 / twoa, r2 / twoa)