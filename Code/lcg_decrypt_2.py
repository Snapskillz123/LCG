from Crypto.Util.number import *
from secrets import randbelow

c = ?
a = ?
b = ?
f_n = ?
f_f_n = ?

s = ?
t = a * s + b

i = 1

while True:
    print("[*] current I:",i)
    guessed_prime = (t - f_n) // i
    if isPrime(guessed_prime) == 1:
        if (a * f_n + b) % guessed_prime == f_f_n:
            print("[*] Found prime number:", guessed_prime)
            p_str = long_to_bytes(guessed_prime - c)
            print(p_str)
            break
    i+=1