# ARFIMA

Python implementation of ARFIMA process with an aim to simulate series.

## Typical usage

```python
import arfima

series = arfima.arfima([], 0.3, [], 2**16, warmup=2**16)
```

The code snippet above would generate time series of ARFIMA(0, 0.3, 0)
process. To simulate process with AR or MA terms simply pass the
coefficients as arguments:

```python
series = arfima.arfima([0.3, 0.2], 0.15, [0.5], 2**16, warmup=2**16)
```

This would simulate time series of ARFIMA(2, 0.15, 1) process with given
parameters.
