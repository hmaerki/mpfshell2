# How to publish to pypi

[https://github.com/bast/pypi-howto]

See also `c:\Users\maerki\.pypirc`

```python
python setup.py sdist
```

## Test

```python
twine upload dist/* -r pypitest
pip install --index-url https://test.pypi.org/simple/ mpfshell2
```

## Upload

```python
twine upload dist/* -r pypi
```
