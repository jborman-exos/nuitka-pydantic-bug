import my_module as mm

def test_minimum_failure() -> None:
    a = mm.A()
    b = mm.B(member_a=a)
    print(f'b: {b}', type(b))
    print(f'b.member_a: {b.member_a}', type(b.member_a))
    b.bar(bar_arg='some argument')

def test_working() -> None:
    a = mm.A()
    b2 = mm.B2(member_a=a)
    print(f'b2: {b2}', type(b2))
    print(f'b2.member_a: {b2.member_a}', type(b2.member_a))
    b2.bar(bar_arg='some argument')

if __name__ == '__main__':
    test_working()
    test_minimum_failure()
