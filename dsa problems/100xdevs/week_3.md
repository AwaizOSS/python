- https://projects.100xdevs.com/tracks/recursion/Recursion-1

## nCr

- nCr is no of ways we can choose r objects out of n objects => nCr = (n-1)C(r-1) + (n-1)Cr
  i.e., f(n,r)=f(n-1,r-1)+f(n-1,r)
- for base condition we see state changes i.e., n->n-1, r->r-1 => base conditions are (n,0)=1 , (0,r)=0
