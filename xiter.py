from typing import Callable

class DynamicList(list):
    def __init__(self, iterable, mutable=True):
        super().__init__(iterable)
        self.base_data = iterable
        self.mutable = mutable
        
        for method_name in dir(list):
            method_value = getattr(self, method_name)
            if method_name != "__class__":
                setattr(self, method_name, self.__wrap_method(method_value))

    def __setitem__(self, key, value):
        self.base_data.__setitem__(key, value)
    
    def __delitem__(self, key):
        return self.base_data.__delitem__(key)
    
    def __wrap_method(self, method):
        def wrapped_method(*args, **kwargs):
            self.__update()
            return method(*args, **kwargs)
        return wrapped_method
    
    def __update(self):
        if self.mutable:
            self[:] = [i() if callable(i) else i for i in self.base_data]
            print("work pls")

arr = DynamicList([1, lambda: 2, 3])
print(", ".join([str(i) for i in arr]))
arr.append(lambda: 4)
print(arr)