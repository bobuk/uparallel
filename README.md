# uparallel
μparallel - oversimplified helper for easy parallel functions execution

Yes, it's oversimplified:

```python
from uparallel import uparallel
import requests

@uparallel(3)
def wikipedia(word):
    return requests.get(f"https://www.wikiwand.com/en/{word.capitalize()}")

results = [wikipedia(word) for word in 'fork spoon spork knife cup home'.split()]
for line in results:
    print(line.url, line.status_code)
```

So, `unparallel(num)` is a wrapper for any function to execute `num` of them in parallel.
There's three limitations:

1. It will wait until last of calls finish their execution
2. It will break on any execption, so catch it inside the function
3. Returned result is a thin wrapper, not result of function itself.

Last one need more explanation. Instead of result of function you will got a special proxy object. It will behave more or less like your normal object (like in this example with `requests`). If it's not, call `result.wait()` or even just `result()` instead of just `result`.

```python
@uparallel(2)
def add2(x):
    return x+2
	
results = [add2(x) for x in range(10)]
for y in results:
	print(y()-2, y)
```

And don't afread to read the code, it's less than 100 lines long.
