- https://projects.100xdevs.com/tracks/DSA-3/Arrays-2

## we dont represent time complexity using the input

```
for(let i=0; i<k; i++) {
    for(let j=0; j<=i; j++) {
        console.log(i + " " + j);
    }
}

for i=0 j run 1 time
i=1 j 2 times
i=2 j 3 times...
so for 1=k-1 j runs n times
i.e., j runs as 0+1+2+3+4+...n which is O(n^2)
```

```
for(let i=1; i<n; i *= 2) {
	console.log(i);
}
1 iteration => i=1 > 2^0
2 iteration => i=2 > 2^1
3 iteration => i=4 > 2^2
4 iteration => i=8 > 2^3
so for nth iteration  i=2^(n-1) i.e., O(log2(n))
```

```
for(let i=1; i<n; i++) {
  for(let j=1; j<n; j+=i) {
     console.log(i + " " + j);
  }
}

i=1 => j runs like 1,2,3,4,5,...n-1 => n times
i=2 => j runs like 1,3,5,7,9,...n-1 => n/2 times
i=3 => j runs like 1,4,7,11,14,...n-1 => n/3 times
...
i=n-1 => j runs 1 time => n/n times
so n,n/2,n/3....3,2,1
=> n(1+ 1/2+ 1/3+ 1/4+ 1/5+ 1/6+ 1/7+ 1/8+ 1/9... 1/n) <=n( 1+ 1/2+ 1/2+ 1/4+ 1/4+ 1/4+ 1/4+ 1/8+ 1/8+... 1/16+... 1/2^k) where 2^k<=n, as per concept of bigO which states f(n)<=c.g(n) & f(n)=O(g(n))
=>(1+ 2*1/2 + 4*1/4 + ... + 2^k*1/2^k) =>k times
k is log2(n) => O(n*log2(n))
```

## some popular complexities

- O(1): Constant time complexity. Example: a + b, a % b, swap(a, b)

- O(log2(n)): Logarithmic complexity. Example: Binary search

- O(sqr(n)): Example: Finding divisors of a number

- O(n): Linear time complexity. Example: Linear search, finding maximum element

- O(n\*log2(n)): Example: Sorting, Seive of Eratosthenes

- O(n^2): Quadratic complexity. Example: Insertion sort

- O(n^3): Cubic complexity. Example: Floyd Warshall algorithm

- O(2^n): Exponential complexity. Example: bitmasking

```
h/w problems
for(i=0;i<n;i++){
    for(j=0;j<(1<<i);j++)
        // print statement
}
while(i<n){
    for(j=i;j<i+5;j++)
        // print statement
    i+=j
}
```
