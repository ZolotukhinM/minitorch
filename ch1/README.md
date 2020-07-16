# Chapter 1

Let's start by creating a simple framework that can execute primitive operations
on tensors of some fixed size. To begin with, we will start with so called eager
mode: all operations will be explicitly invoked by the user.

Our tensors will actually be [1x2] vectors of ints (for the sake of simplicity of this
tutorial) and we will only support the following ops:

 - add: arithmetic add
 - mul: arithmetic multiply
 - and: logical and
 - print: print contents of the tensor
 - assign: copy contents from another tensor

We implement these operations as methods of Tensor class and they mutate the
current tensor. E.g. operation `A.add_op(B, C)` mutates takes inputs `B` and `C` and
mutates `A`.

Below are the sources of the `Tensor` class and the driver program:

`ops.py`:

```python

    class Tensor:
        def __init__(self, init_val=[0, 0]):
            self.val = init_val

        def and_op(self, A, B):
            (a, b) = (A.val, B.val)
            self.val = [a[i] & b[i] for i in range(len(a))]

        def add_op(self, A, B):
            (a, b) = (A.val, B.val)
            self.val = [a[i] + b[i] for i in range(len(a))]

        def mul_op(self, A, B):
            (a, b) = (A.val, B.val)
            self.val = [a[i] * b[i] for i in range(len(a))]

        def print_op(self):
            print('>> ' + str(self.val))

        def assign_op(self, A):
            self.val = A.val
```

`main.py`:

```python

    from ops import Tensor

    def main():
        print("Executing eagerly:")
        a = Tensor([7, 3])
        b = Tensor([5, 6])
        c = Tensor()
        d = Tensor()
        c.mul_op(a, b)
        d.and_op(c, c)
        d.print_op()

    if __name__ == '__main__':
        main()
```

If we execute the program, we should see:

```
    
    $ python main.py
    Executing eagerly:
    >> [35, 18]
```
