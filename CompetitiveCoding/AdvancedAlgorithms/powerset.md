# PowerSet

Reference from take U forward by Striver
[source](https://www.youtube.com/watch?v=b7AYbpM5YrE&ab_channel=takeUforward)

## When To Use PowerSet

1. When you want to generate all possible non contiguous subsequence

Example if you have string s = "abc" then it's possible subsequnces are "","a","b","c","ab","ac","bc","abc"
here n = 3 , therefore 2<sup>3</sup> is 8

## Prerequisite

The prerequisite of this topic is bit manipulation

```text
example if you take the binary of 5
     2 1 0
5 -> 1 0 1
where 1 is at 0th index, 0 is at 1th index and again 1 is at 2nd index

if you want to check if bit at index i is set or not , lets check for 2nd bit here
take binary where you place 1 at i and the rest is 0
then if 5 -> 101 then do an AND operation with 100 i.e 101 & 100 is 100 
if the result is not equal to 0 i.e 000 then we say bit is set which is the case here

so how you can get the number to do AND with, you can do 1 << i ( <<  is left shift)  and the you do AND with n i.e (n & (1 << i))
if (n & (1 << i)) != 0 then we can say that the bit at index i is set

if you think that s = "abc" and then draw a table of binary value from 0 to 7 (total 8)

_ _|_2_1_0_
0  | 0 0 0
1  | 0 0 1
2  | 0 1 0
3  | 0 1 1
4  | 1 0 0
5  | 1 0 1
6  | 1 1 0
7  | 1 1 1

If you analyse the pattern of the binary values and consider that 0 means the element at this index will be not picked and vice versa for 1
then you start maaping it with the string and print values you will get the subsequences
```

## Main Algo

If you now think about it and write a for loop to print all subsequences
you will go from 0 to pow(2,n) - 1 where pow(2,n) is equivalent to (1 << n) - 1

pseudo code

```text
s = "anyString"
for(num from 0 to pow(2,n)-1){
    subString=""
    for(i from 0 to n-1){
        if(num & (1 << i)){
            subString+=s[i]
        }
    }
    print(subString)
}
```

if we talk about the time complexity the outer loop runs for pow(2,n) and inner loop for n
O(pow(2,n) * n)
And Space Complexity is O(1)
