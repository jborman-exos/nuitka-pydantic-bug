import my_module as mm

def test_minimum_failure() -> None:
    a = mm.A()
    b = mm.B(member_a=a)

    b.bar(bar_arg='some argument')

def test_working() -> None:
    a = mm.A()
    b = mm.B2(member_a=a)

    b.bar(bar_arg='some argument')

if __name__ == '__main__':
    test_working()
    test_minimum_failure()
