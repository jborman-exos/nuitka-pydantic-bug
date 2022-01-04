# nuitka-pydantic-bug

A reproducible example indicating a possible bug with Nuitka/Pydantic.

## The bug

A module utilizing Pydantic's `BaseModel` class is compiled via Nuitka. The plain source code runs fine in `test_my_module.py`,
however the compiled code fails to pass. The resulting error when trying to invoke `b.bar(bar_arg='some argument')`

```
Traceback (most recent call last):
  File "/home/[user1]/.pyenv/versions/3.9.9/lib/python3.9/runpy.py", line 197, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/home/[user1]/.pyenv/versions/3.9.9/lib/python3.9/runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "/mnt/c/Users/[user1]/github/nuitka-pydantic-bug/test_my_module.py", line 19, in <module>
    test_minimum_failure()
  File "/mnt/c/Users/[user1]/github/nuitka-pydantic-bug/test_my_module.py", line 8, in test_minimum_failure
    b.bar(bar_arg='some argument')
TypeError: bar() missing 1 required positional argument: 'self'
```

## How to Reproduce

On windows execute `run.bat` or unix `bash run.bash`

## Env Info

Confirming this issue affects the following envs:

```
(.venv) [user1]@LAPTOP-54N6HJS3:/mnt/c/Users/[user1]/github/nuitka-pydantic-bug$ python -m nuitka --version
0.6.18.6
Commercial: None
Python: 3.9.9 (main, Dec 29 2021, 12:20:17)
Flavor: pyenv
Executable: /mnt/c/Users/[user1]/github/nuitka-pydantic-bug/.venv/bin/python
OS: Linux
Arch: x86_64
Distribution: Ubuntu "16.04.6
```

```
(.venv) [user1]@LAPTOP-54N6HJS3:/mnt/c/Users/[user1]/github/nuitka-pydantic-bug$ python -m nuitka --version
0.6.15.3
Python: 3.9.9 (main, Dec 29 2021, 12:20:17)
Executable: /mnt/c/Users/[user1]/github/nuitka-pydantic-bug/.venv/bin/python
OS: Linux
Arch: x86_64
```
