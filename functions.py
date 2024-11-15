from backpack import Backpack
from jetpack import Jetpack
from Complex import ComplexNumber

def test_backpack():
    backpack = Backpack(name="John", colour="blue", max_size=3)
    backpack.put("pen")
    backpack.put("notebook")
    backpack.put("book")
    backpack.put("pencil")
    print(backpack)
    backpack.dump()
    print(backpack)

def test_jetpack():
    jetpack = Jetpack("Bob", "red")
    jetpack.put("pen")
    jetpack.put("book")
    jetpack.put("pencil")
    print(jetpack)
    jetpack.fly(7)
    print(jetpack)
    jetpack.fly(7)
    print(jetpack)

def test_complex_number():
    n1 = ComplexNumber(3,2)
    n2 = ComplexNumber(4, 5)
    print(f"n1: {n1}\nn2: {n2}")
    print(f"n1+n2 = {n1+n2}")
    print(f"n1-n2 = {n1-n2}")
    print(f"n1*n2 = {n1*n2}")
    print(f"n1/n2 = {n1/n2}")
    print(f"|n1| = {abs(n1)}")
    print(f"n1 conjugate: {n1.conjugate()}")
