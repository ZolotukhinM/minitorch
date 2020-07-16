# Chapter 3

In this chapter we will add a tracing to bridge the gap between scripting and
eager execution.

Suppose you start experimenting in our framework and for faster iterations you
used eager mode. But now you finished the experiment and you want to start using
scripting mode. How do you transition? Tracing is supposed to help you there.

We can modify our operations in such a way that they create a corresponding
`Node` every time we execute them. A tricky part is to reconstruct relations
between inputs and outputs - we need to make sure that if we run two ops
consecutively on the same tensors, the constructed `Program` refers to the same
`Value`s. To achieve that, we can use `id(tensor)` as an identifier of our
`Value`s - when we see a new `id`, we create a new `Value`, otherwise we reuse
the one we created earlier for this `id`.

A code for `trace_op` function along with the way we invoke it could be found in
`ops.py`. We also add a couple of functions to turn on and off tracing:
`start_tracing` and `stop_tracing`.

Now we can run our eager code and get an IR from it automatically. The code for
this can be found in `main.py`, and the output of the program will look like
this:

```

    Executing eagerly with tracing:
    >> [35, 18]
    Traced IR: {
      t0 input
      t1 input
      t2 input
      t3 input
      t2 mul t0 t1
      t3 and t2 t2
      t3 print
    }
    Executing traced program:
    >> [35, 18]
```

