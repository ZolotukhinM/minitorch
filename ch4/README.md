# Chapter 4

In this chapter we will look into simple optimizations we can do on our IR.

Here we implement a simple peephole optimization replacing `A = AND(B,B)` with
`A = ASSIGN(B)`.  The code can be found in `ir.py`.
