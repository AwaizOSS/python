## binary search

- for time complexity we go like N -> N/2 -> N/4 -> N/8 -> N/16 -> ..... -> 1

We can also write this as,
N -> N/2 -> N/(2^2) -> N/(2^3) -> ..... -> N/(2^k)

where N/(2^k) = 1 and it runs for k iterations.

So k = log2(N)

```
int findIndex(int arr[], int n, int x) {
	 // lo, hi points to the lowest and highest indices of search space. Currently,
	 // we are considering the entire array so 0 and n-1 respectively.
   int lo = 0, hi = n-1;
   while (lo <= hi) {
	   int mid = (lo + hi) / 2;
	   if (arr[mid] == x) return mid;
	   else if (arr[mid] < x) {
		   // x is on the right hand side, reject left half
		   lo = mid + 1;
	   } else {
		   // x is on the left hand side, reject right half
		   hi = mid - 1;
	   }
   }

   // If we come here, then we did not find the element.
   return -1;
}
```
