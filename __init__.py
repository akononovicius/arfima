"""Simulate ARFIMA process.

This module allows simulation of the ARFIMA(p, d, q) processes:
    AR(B) (1-B)^d x = MA(B) epsi .
If d = 1, the process becomes ARMA(p, q) process:
    x[t] = ar[1]*x[t-1] + ar[2]*x[t-2] + ... + ar[p]*x[t-p] +
           + ma[1]*epsi[t-1] + ma[2]*epsi[t-2] + ... + ma[q]*epsi[t-q] +
           + epsi[t]
Fractional differencing is done by using Fourier space, as proposed by Jensen
& Nielsen (2014).

Typical usage example:
    import arfima
    series = arfima.arfima([], 0.3, [], 2**16, warmup=2**16)
"""
from ._arfima import arfima
