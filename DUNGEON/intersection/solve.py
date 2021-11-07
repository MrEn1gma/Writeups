import binascii
from sys import flags
from z3 import *

s = Solver()

x = [Int("x%d"%i) for i in range(2)]

def modular_sqrt(a, p):
    
    def legendre_symbol(a, p):
        """ Compute the Legendre symbol a|p using
            Euler's criterion. p is a prime, a is
            relatively prime to p (if p divides
            a, then a|p = 0)
            Returns 1 if a has a square root modulo
            p, -1 otherwise.
        """
        ls = pow(a, (p - 1) // 2, p)
        return -1 if ls == p - 1 else ls

    """ Find a quadratic residue (mod p) of 'a'. p
        must be an odd prime.
        Solve the congruence of the form:
            x^2 = a (mod p)
        And returns x. Note that p - x is also a root.
        0 is returned is no square root exists for
        these a and p.
        The Tonelli-Shanks algorithm is used (except
        for some simple cases in which the solution
        is known from an identity). This algorithm
        runs in polynomial time (unless the
        generalized Riemann hypothesis is false).
    """
    # Simple cases
    #
    if legendre_symbol(a, p) != 1:
        return 0
    elif a == 0:
        return 0
    elif p == 2:
        return p
    elif p % 4 == 3:
        return pow(a, (p + 1) // 4, p)

    # Partition p-1 to s * 2^e for an odd s (i.e.
    # reduce all the powers of 2 from p-1)
    #
    s = p - 1
    e = 0
    while s % 2 == 0:
        s //= 2
        e += 1

    # Find some 'n' with a legendre symbol n|p = -1.
    # Shouldn't take long.
    #
    n = 2
    while legendre_symbol(n, p) != -1:
        n += 1

    # Here be dragons!
    # Read the paper "Square roots from 1; 24, 51,
    # 10 to Dan Shanks" by Ezra Brown for more
    # information
    #

    # x is a guess of the square root that gets better
    # with each iteration.
    # b is the "fudge factor" - by how much we're off
    # with the guess. The invariant x^2 = ab (mod p)
    # is maintained throughout the loop.
    # g is used for successive powers of n to update
    # both a and b
    # r is the exponent - decreases with each update
    #
    x = pow(a, (s + 1) // 2, p)
    b = pow(a, s, p)
    g = pow(n, s, p)
    r = e

    while True:
        t = b
        m = 0
        for m in range(r):
            if t == 1:
                break
            t = pow(t, 2, p)

        if m == 0:
            return x

        gs = pow(g, 2 ** (r - m - 1), p)
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m

num1 = 0x4b5ec9227ac1c16bcc9c03656b648380f06d7e889940bf2a9dce4708047a21cd
num2 = 0x984e50d5688ee40207ad56f879c80c07ab16d82ec8075dfca5840184802b0742
mod = 0x999120a873890329cf2adc1c544150ad00f9b6b2f2c9535ea6ce2b44d5b678e7

# i called (x + y) ** 2 % mod is ans1 and (x - y) ** 2 % mod is ans2
ans1 = ((num1 ** 2) % mod + (2 * num2) % mod) % mod #60676705311640645466324373113305685254608277405378918059810035250397431854850
ans2 = ((num1 ** 2) % mod + (-2 % mod * num2) % mod) % mod #62958141735869402209967543733199390445257262504169519885927009473430123953558

#print(modular_sqrt(ans1, mod))
#print(modular_sqrt(ans2, mod))
s.add(x[0] > 0, (x[1] - x[0]) % mod == modular_sqrt(ans2, mod))
s.add(x[1] > 0, (x[0] + x[1]) % mod == modular_sqrt(ans1, mod))

if(s.check() == sat):
      m = s.model()
      flag0 = binascii.unhexlify(hex(m[x[0]].as_long())[2:]).decode()
      flag1 = binascii.unhexlify(hex(m[x[1]].as_long())[2:]).decode()
      print(flag0 + flag1)
else:
      print("No solution.")