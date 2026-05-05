# 📘 Sudan List Decoding of Reed–Solomon Codes
This project implements **Sudan’s list decoding algorithm** for Reed–Solomon codes over a finite field **GF(p)**, using **Python** and **SageMath**.

It demonstrates how to recover original messages from noisy codewords—even beyond the classical decoding limit.

---

## 📚 Background
Reed–Solomon codes are powerful error-correcting codes used in CDs, QR codes, and communication systems. They represent messages as polynomials evaluated over a finite field.

While traditional decoding can correct only up to a certain number of errors, Sudan’s algorithm goes further. It uses list decoding to return all possible messages that could match a corrupted codeword—even when more than half the symbols are wrong.

This project works over GF(257) to match ASCII values, and is based on the book:
📖 * Essential Coding Theory by Madhu Sudan and Atri Rudra (chapters 5, 11 and 12).

🔗[Reference]: (https://cse.buffalo.edu/faculty/atri/courses/coding-theory/book/web-coding-book.pdf)


## 🗂️ Project Structure
.

├── encoder.py            # Converts messages to polynomials and encodes them

├── decoder.py            # Implements Sudan's decoder: interpolation + factorization

├── encoder_decoder.py    # Full run: encode, add noise, decode, and print results

├── utilities.py          # Defines the finite field GF(p)

├── README.md             # Project documentation

---

## 🚀 How to Run
### 🔧 Requirements
- Python 3.x
- SageMath (must be available in your Python environment)
- `galois` library

### ▶️ Run the Code
```bash
python3 tests.py
```
### Notes:
- You can customize the message, codeword length, and number of errors.
- Enable/disable tests by commenting them in tests.py.
