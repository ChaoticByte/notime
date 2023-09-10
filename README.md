# notime

notime is a simple python library that represents the daytime on a scale of `0` - `100000000` in a most probably mathematically inaccurate way.

## Examples

```python
>>> from notime import notime
>>> a = notime(10000)
>>> a
10000
>>> b = notime.from_time(15, 30, 0, 0)
>>> b
64583333
>>> a + b
64593333
```
