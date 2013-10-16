MCMC Cipher Solver
==================

A Python implementation of an algorithm described by Hasinoff (2003, p. 3). The program takes a file that has been encrypted using a simple cipher and decrypts it using a Markov Chain Monte Carlo method. More specifically, it performs a random walk around the set of 26! possible keys to find one that yields the most English-like text. See Chen and Rosenthal (2012) and Diaconis (2009) for more information.

Example
-------

From the command line:

> $  python decode.py example.txt

Optionally, you can also specify the number of trials and swaps to perform:

> $  python decode.py example.txt 50 4000

Higher numbers take longer but give more accurate results.

References
----------

Chen, J., & Rosenthal, J. S. (2012). Decrypting classical cipher text using Markov chain Monte Carlo. Statistical Computing, 22, 397–413. doi:10.1007/s11222-011-9232-5

Diaconis, P. (2009). The Markov Chain Monte Carlo revolution. Bulletin of the American Mathematical Society, 46, 179–205. doi:10.1090/S0273-0979-08-01238-X

Hasinoff, S. W. (2003). Solving substitution ciphers. Unpublished technical report from University of Toronto, Toronto, Canada. Available from http://people.csail.mit.edu/hasinoff/pubs/hasinoff-quipster-2003.pdf