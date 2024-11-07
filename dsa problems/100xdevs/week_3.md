- https://projects.100xdevs.com/tracks/recursion/Recursion-1

## nCr

- nCr (n!/(n-i)!r!) is no of ways we can choose r objects out of n objects => nCr = (n-1)C(r-1) + (n-1)Cr
  i.e., f(n,r)=f(n-1,r-1)+f(n-1,r)
- for base condition we see state changes i.e., n->n-1, r->r-1 => base conditions are (n,0)=1 , (0,r)=0

## merge sort

- combines method's tc is n & steps are n->n/2->n/4...1 => log2(n) hence tc of merge sort is nlog2(n)

## quick sort

# how to think recursively

## step 1 identify the function & states

- ex nCr => c(n,r) where n,r are states

## step 2 assumption

- assume except for c(i,j) we know value of c(n,r) for all values of n,r

## step 2 calculate c(i,j) from neighboring values

- considering last object if we choose to take it then next step will be c(i-1,j-1) but if we dont choose to take it thats c(i-1,j)
  =>c(i,j)=c(i-1,j-1)+c(i-1,j)

## problems

- rack in a maze, sudoku
