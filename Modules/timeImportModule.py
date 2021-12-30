#timeit module tests the efficiency i.e. how fast a code would be executed
import timeit

first = timeit.timeit('[]', number=10*4)
second = timeit.timeit('list()', number=10*4)
print(first)
print(second)