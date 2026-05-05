import galois
import utilities

# convert the mesg to polinomyal coefficients
def msg_as_poly(msg):
    msg_list =[ord(ch) for ch in msg]
    msg_coeffs = msg_list
    poly = galois.Poly(msg_coeffs, order="asc",  field=utilities.GF)
    return poly

# construct the code word (evaluate the polynomial at each given point)
def evaluate_code_word(poly, eval_pts):
    codeword = [poly(eval_pt) for eval_pt in eval_pts ] 
    return  codeword

def encoder(msg, eval_pts):
    poly = msg_as_poly(msg)
    codeword = evaluate_code_word(poly, eval_pts)
    return codeword