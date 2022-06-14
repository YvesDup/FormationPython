import functools
import math
import os
import signal
import sys
import time
import traceback


_indent = """

if True:

print("okkkkkkkay")

    a = 10

"""

def recurs(n):
    """
    """
    recurs(n-1)

def test_exception():
    """
    """
    data_tests = (
                 (TypeError,            "s = 'hello' ; s[0] = 'H'"),
                 (TypeError,            ""),
                 (ValueError,           ""),
                 (IndexError,           ""),
                 (KeyError ,            ""),
                 (NameError,            ""),
                 (ImportError ,         ""),
                 (SyntaxError,          ""),
                 (IndentationError,     ""),
                 (OSError,              ""),
                 (FileNotFoundError,    ""),
                 (ZeroDivisionError,    ""),
                 (AssertionError,       ""),
                 (AttributeError,       ""),
                 (RecursionError,       ""),
                 (StopIteration,        ""),
                 (SystemExit,           ""),
                 (MemoryError,          ""),
                 (OverflowError,        ""),
                 (RuntimeError,         ""),
                 (Exception,            ""),
                 )

    l = 20
    for pos, (error, code) in enumerate(data_tests):
        try:
            a = exec(code, globals(), locals())
        except error as e:
            print(f"{pos:02d}\tWaiting for {error.__name__:{l}s},\tok - {e} !!")
            if e.__context__:
                print(e.__context__)
        except Exception as e:
            print(f"{pos:02d}\tSo waiting for {error.__name__:{l}s},\tbut {type(e), str(e)} came, so bad !!")
            if e.__context__:
                print(e.__context__)
            detail = e.args[0]
            cl, exc, tb = sys.exc_info()
            line_number = traceback.extract_tb(tb)[-1][1]
        else:
            print(f"{pos:02d}\tWaiting for {error.__name__:>{l}s},\tnever come on {code!r}")

def main():
    """
    """
    test_exception()

if __name__ == "__main__":
    main()



