
import utilities
import sympy as sp
from sage.all import *
import math
import numpy as np

# 1. Constructing Q(x, y) — Interpolation

def build_monomials(deg_x, deg_y):
    # Generate all (i, j) monomials such that 0 ≤ i ≤ deg_x and 0 ≤ j ≤ deg_y. 
    # These represent terms x^i * y^j in the bivariate polynomial Q(x, y).
    return [(i, j) for i in range(deg_x+1) for j in range(deg_y + 1)]

def build_interpolation_matrix(pairs, monomials):
    #Construct the interpolation matrix, where each row corresponds to evaluating monomials at a given (alpha, y) pair over GF(p).
    A = []
    for alpha, y in pairs:
        row = []
        for (i, j) in monomials:
            val = (utilities.GF(alpha)**i) * (utilities.GF(y)**j)
            row.append(int(val))
        A.append(row)
    return A

def coeffs_to_poly(coeffs, deg_x, deg_y):
    # Convert a flat list of coefficients into a bivariate polynomial over GF(p).
    polynomial = 0
    x, y = PolynomialRing(GF(utilities.p), 2, ['x', 'y']).gens()
    for i in range(deg_x + 1):
        for j in range(deg_y + 1):
            coeff = int(coeffs[((deg_y + 1) * i) + j]) % utilities.p
            polynomial += coeff * x ** i * y ** j
    return polynomial

def build_Qs(matrix, n, deg_x, deg_y):
    # Solve for the right nullspace of the interpolation matrix to find Q(x, y)
    # Polynomials that satisfy Q(alpha_i, y_i) = 0 for all i.
    M = MatrixSpace(GF(utilities.p), n, (deg_x + 1) * (deg_y + 1))
    A = M(matrix)
    Qs_coeffs = A.right_kernel_matrix(basis="computed")
    return [coeffs_to_poly(coefficients, deg_x, deg_y) for coefficients in Qs_coeffs]

def construct_Q(codeword, n, k, eval_pts):
    # Constructing candidate Q(x, y) polynomials.
    deg_x = math.floor(math.sqrt(n * (k - 1)))
    deg_y = 1 if deg_x == 0 else math.floor(n / math.sqrt(n * (k - 1)))
    pairs = zip(eval_pts, codeword)
    monomials = build_monomials(deg_x, deg_y)
    A = np.array(build_interpolation_matrix(pairs, monomials))
    return build_Qs(A, n, deg_x, deg_y)

# 2. Factoring

def factors(qs):
    # Factor all Q(x, y) polynomials and return linear factors of the form y - f(x). (Where f(x) is a candidate message polynomial)
    all_factors = []
    y = PolynomialRing(GF(utilities.p), 1, 'y').gen()
    for q in qs:
        for factor in q.factor():
            all_factors.append(y - factor[0])
    return all_factors

# 3. Retrieve message strings from candidate polynomials
def msg_retrieve(poly):
    # Convert a polynomial f(x) = a_0 + a_1*x + ... into a string message by interpreting coefficients as ASCII values. 
    msg = ""
    for ch in poly.coefficients():
        msg += chr(ch)
    return msg[::-1]

# Full decoder
    
def decoder(codeword, n, k, e, eval_pts):
    # Decode a potentially corrupted codeword using Sudan's algorithm.
    # Returns a list of all candidate decoded messages.

    all_poss_Qs = construct_Q(codeword, n, k, eval_pts)
    all_factors = set(factors(all_poss_Qs))
    list_decoding = [msg_retrieve(factor) for factor in all_factors]
    return list_decoding