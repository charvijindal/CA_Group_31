# demo_classes.py

class ClassA:
    def __init__(self, class_b):
        self.class_b = class_b

    def setB()


class ClassB:
    def __init__(self, class_a):
        self.class_a = class_a

    def method_b(self):
        print("Method B in ClassB")
        # Call method_a in ClassA
        self.class_a.method_a()

