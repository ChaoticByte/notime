# notime

notime is a simple python library that represents the daytime on a scale of `0` - `99999999` in a most probably mathematically inaccurate way.

## Examples

```python
>>> from notime import notime
>>> a = notime(50000000)
>>> b = notime.from_time(12, 5, 0, 0)
>>> b
50347222
>>> a + b
347222
```
