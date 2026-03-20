# Multiple inheritance

class A:
    def method_a(self):
        print("This is method A")

class B:
    def method_b(self):
        print("This is method B")

class C(A, B):
    def method_c(self):
        print("This is method C")

c = C()

c.method_a()
c.method_b()
c.method_c()
