# Chapter 5

In this chapter we will add caching to our interpreter.

Suppose that we are running a service that interprets our IR on every incoming
request. It is possible that we will get the same external inputs several times
and in that case it would be possible to just memoize what we should print and
skip all actual computations.

Let's look at an example. Suppose our original IR looks like this:

```

    a input
    b input
    c mul a b
    d and c c
    d print
```

And suppose we run it over and over again with the following inputs:
`a = [1, 2], b = [0, 6]`.

What if we modify our interpreter so that it would record outputs of all ops? It
would record something like this:

```

    a input    ==> [1,2]
    b input    ==> [0,6]
    c mul a b  ==> [0,12]
    d and c c  ==> [0,12]
    d print 
```

Having this data, on the next request instead of executing the original IR with
`external_inputs=[[1, 2], [0, 6]]` we could execute optimized IR looking like
the following:

```

    d input
    d print 
```
with `external_inputs=[[0, 12]]`.

Generally, we could have a cache of optimized, or specialized, IRs and we could
use them instead of the original IR if we happen to get the same inputs again.

This is roughly what is called specialized graphs in PyTorch. The difference is
that in PyTorch we use input tensor rank rather than values as a key in the
cache.

TODO: Add actual implementation.
