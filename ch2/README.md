# Chapter 2

In this chapter we will add a so-called scripting mode to our framework.

Why could scripting mode be useful? Suppose you want to use the framework, but
you can not use python (and suppose that actual ops are in fact written in
C/C++/Asm - that's the case for PyTorch ops). In that case you can not do

```

    a = Tensor([7,3])
    a.print()
```
But instead you need another way to describe the same sequence of actions.

## Parsing scripts
Let's introduce a simple language for this. The program in our language will
be just a list of statements, and each statement has a form of `OUTPUT OPERATION
INPUTS`, where `OUTPUT` is an ID of the output tensor, `OPERATION` is the name
of the operation to perform, `INPUTS` is a space delimeted list of IDs of input
tensors.

A program in such language would then look like the following:

```

    c mul a b
    d and c c
    d print
```

Let's parse it into our IR, but first let's introduce the IR itself.

The top-level object in our IR would be `Program`, which would contain a list of
`Node`s. Each `Node` will have an output (`Value`), an opcode (string), and
inputs (a list of `Value`s). Each `Value` will have a name and a list of uses (a
list of `Node`s).

The parsing of our primitive language into this, also quite primitive, IR is
very straightforward (see the source code in `ir.py`).

## Executing IR
Now we need to learn how to execute the parsed IR. Note that our `Value` objects
contain no actual data - they are just symbols. To be able to actually invoke
operators on real data, we will need to store it somewhere. We will introduce a
class `ExecutionState` for this. This class will model execution environment -
it will keep track of all actual tensors we create, on their relationship with
symbolic `Value`s and it will also perform some basic dispatching.

One last missing piece before this entire design would work is initialization of
Tensors.  To keep the implementation simple, we will pass a list of initial
tensor values on creation of `ExecutionState` object and use it for initializing
our tensors. To specify, which exact tensors to initialize, we let's add a new
operation to our language - `input` - which will take the next value from the
init-list and save it to our tensor.

Once we iron this all out, we just need to iterate over all nodes in our IR and
execute them one by one, preserving the state (actual Tensors and their relation
to Values). The complete code for this can be found in `execution.py`.

Now, if we run our program in scripting mode, we will get exactly the same
result as in the eager mode:

```

    $ python main.py
    === Scripting mode ===
    Parsed IR: {
      t0 input
      t1 input
      t2 mul t0 t1
      t3 and t2 t2
      t3 print
    }
    Executing parsed program:
    >> [35, 18]
```
