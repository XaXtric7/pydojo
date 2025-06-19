class Animals:
    pass


class Pets(Animals):
    pass


class Dog(Pets):

    @staticmethod
    def bark():
        print("Bow Bow!")


d = Dog()
d.bark()


class Dog:
    def normal_bark(self):
        print("Bow Bow with self")

    @staticmethod
    def static_bark():
        print("Bow Bow without self")

# # Normal method requires object
# dog1 = Dog()
# dog1.normal_bark()   # ✅ Works
# Dog.normal_bark()    # ❌ Error (missing 'self')

# # Static method can be called with or without object
# dog1.static_bark()   # ✅ Works
# Dog.static_bark()    # ✅ Also works
