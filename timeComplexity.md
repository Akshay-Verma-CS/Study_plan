# Time Complexity Analysis

## Big O Notation
- **Big O** is the language and metric used to describe the efficiency of algorithms.
- Regardless of how large the constant is or how slow the linear increase is, a linear algorithm will eventually surpass a constant.

## Comparisons of Notations
- **Big O (big O)** - Describes an upper bound on the time an algorithm takes.
- **Big Omega (Ω)** - An equivalent concept to Big O but for the lower bound.
- **Big Theta (Θ)** - Means both Big O and Big Omega, providing a tight bound.

## Cases in Algorithm Performance
### Best Case
- If all elements are equal then quicksort will, on average, just traverse the array once. This is O(N).

### Worst Case
- The pivot is repeatedly the largest element in the array. This will degenerate to an O(N^2) runtime.

### Expected Case
- The pivot will be very low or very high, but it won't happen repeatedly. We can expect a runtime of O(N log N).

## Space Complexity
- Space complexity is a parallel concept to time complexity.
- If we create an array of size N, it requires O(N) space and similarly for an NxN matrix, it requires O(N^2) space.

### Simplifying Complexities
- Drop the constants (e.g., O(2N) → O(N)).
- Drop the non-dominant terms (e.g., O(N^2 + N) → O(N^2)).

## Multi-Part Algorithms: Add vs Multiply
- When to add vs. multiply runtimes:
  - If one algorithm executes and then another, add the complexities (O(A+B)).
  - If one algorithm is nested in another algorithm, then multiply (O(A*B)).

## Amortized Time
- In cases where the size of an array increases by 2 every time it reaches its limit, the majority of insertions will be O(1), but creating a new array when needed will be O(N). Amortized time allows us to describe that the worst case happens only occasionally.

## Log N Runtimes
- Log base 2 of N equals k implies 2^k equals N.

## Recursive Runtimes
- Recursive functions that make multiple calls have runtimes that look like O(branch^depth), where branch is the number of times a recursive call branches.


