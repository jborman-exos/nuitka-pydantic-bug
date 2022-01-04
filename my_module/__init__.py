from pydantic import BaseModel

class A:
    def foo(self, foo_arg):
        print(f'A.foo({foo_arg})')

class B(BaseModel):
    member_a: A

    def bar(self, bar_arg: str) -> None:
        self.member_a.foo(bar_arg)

    class Config:
        arbitrary_types_allowed = True


class B2:
    def __init__(self, member_a: A) -> None:
        self.member_a = member_a

    def bar(self, bar_arg: str) -> None:
        self.member_a.foo(bar_arg)
