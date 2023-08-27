class IterableProxy:
    def __init__(self, iterable):
        self._iterable = iterable
    
    def __getattr__(self, attr):
        return getattr(self._iterable, attr)

# Usage
my_list = [1, 2, 3, 4]
proxy = IterableProxy(my_list)

# You can now call any method applicable to lists on the proxy
print(proxy[2])  # Prints: 3 (indexing)
print(len(proxy))  # Prints: 4 (length)