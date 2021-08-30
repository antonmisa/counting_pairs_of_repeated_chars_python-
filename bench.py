import string
import random
from main import count_doubles_zip, count_doubles_regexp, count_doubles_classic, count_doubles_iter, count_doubles_itertools, count_doubles_numpy, count_doubles_comprehension
import myrustlib

val = ''.join(random.choice(string.ascii_letters) for i in range(1000000))

def test_pure_python(benchmark):
    benchmark(count_doubles_zip, val)

def test_regexp(benchmark):
    benchmark(count_doubles_regexp, val)

def test_python_classic(benchmark):
    benchmark(count_doubles_classic, val)

def test_python_iter(benchmark):
    benchmark(count_doubles_iter, val)

def test_python_itertools(benchmark):
    benchmark(count_doubles_itertools, val)

def test_python_numpy(benchmark):
    benchmark(count_doubles_numpy, val)
    
def test_python_comprehension(benchmark):
    benchmark(count_doubles_comprehension, val)

def test_rust_pure(benchmark):
    benchmark(myrustlib.count_doubles, val)    

def test_rust_once(benchmark):
    benchmark(myrustlib.count_doubles_once, val)    