def singleton(class_):
    class class_w(class_):
        _instance = None
        def __new__(class2, *args, **kwargs):
            if class_w._instance is None:
                class_w._instance = super(class_w, class2).__new__(class2, *args, **kwargs)
                class_w._instance._sealed = False
            return class_w._instance
        def __init__(self, *args, **kwargs):
            if self._sealed:
                return
            super(class_w, self).__init__(*args, **kwargs)
            self._sealed = True
    class_w.__name__ = class_.__name__
    return class_w

@singleton
class MyClass(object):
    def __init__(self, text):
        print text
    @classmethod
    def name(class_):
        print class_.__name__

x = MyClass(111)
x.name()
y = MyClass(222)
print id(x) == id(y)