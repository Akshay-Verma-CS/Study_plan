# Recursion

[Recursion Playlist by take u forward](https://www.youtube.com/playlist?list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9)

When a function calls itself until a specified condition is met.

## Contents

1. [terms](https://github.com/Akshay-Verma-CS/Study_plan/blob/main/CompetitiveCoding/DynamicProgramming/Recursion/recursion.md#terms)
2. [Basic Recursion Problems](https://github.com/Akshay-Verma-CS/Study_plan/blob/main/CompetitiveCoding/DynamicProgramming/Recursion/recursion.md#basic-recursion-problems)
3. [Parameterized and Functional Recursion](https://github.com/Akshay-Verma-CS/Study_plan/blob/main/CompetitiveCoding/DynamicProgramming/Recursion/recursion.md#parameterized-and-functional-recursion)
4. [Multiple Recursion Calls](https://github.com/Akshay-Verma-CS/Study_plan/blob/main/CompetitiveCoding/DynamicProgramming/Recursion/recursion.md#multiple-recursion-calls)
5. [Recursion on Subsequences](https://github.com/Akshay-Verma-CS/Study_plan/blob/main/CompetitiveCoding/DynamicProgramming/Recursion/recursion.md#recursion-on-subsequences)

## terms

1. Stack Overflow - When the recursion is infinite then after a time the memory gets exhausted, this situation is called stack overflow.
2. Base Condition - The condition where the recursion ends.
3. Recursion Tree - you cannot perform a dry run on a code implementing recursion using stack. It is best represent it in the form of a tree.

## Basic Recursion Problems

Problem 1 : Print name 5 times

```python
def printName(name: string,count: int) -> None:
    if count < 1:
        return
    print(name)
    printName(name,count-1)
name: string = input("Enter name")
count: int = 5
printName(name,count)
```

Problem 2 : Print linearly from 1 to N

```python
def printNumbers(n: int) -> None:
    if count < 1:
        return
    printNumbers(n-1)
    print(n)
n: int = int(input())
printNumbers(10)
```

Problem 3 : Print linearly from N to 1

```python
def printNumbers(n: int) -> None:
    print(n)
    if count < 1:
        return
    printNumbers(n-1)
n: int = int(input())
printNumbers(n) 
```

## Parameterized and Functional Recursion

Problem 1 : Sum of first N numbers

Parameterised way

```python
def getSumOfFirstNNumbers(counter: int,sum: int) -> int:
    if counter < 1:
        print(sum)
    else:
        getSumOfFirstNNumbers(counter - 1, sum + counter)
    n = int(input("Enter a number"))
    getSumOfFirstNNumbers(n)
```

Functional way

```python
def getSumOfFirstNNumbers(n: int) -> int:
    if n > 0:
        return n + getSumOfFirstNNumbers(n-1)
n = int(input("Enter a number"))
print(getSumOfFirstNNumbers(n))
```

## Multiple Recursion Calls

Here we will call a function multiple times inside a single function.

Fibonacci numbers is a great example of this,

in fibonacci f(n) = f(n-1) + f(n-2)

pseudo code for fibonacci

```bash
function(n){
    if( n <= 1 ){
        return n;
    } else {
        return function( n - 1 ) + function ( n - 2 );
    }
}
```

I case of multiple recursion calls you should consider a dry run with recursion tree, I will explain it for the basic formula

```bash
        f(n)
        /  \
    f(n-1) f(n-2)
```

The below function will give you Nth fibonacci number

```python
def fibonacci(n: int) -> int:
    if n <= 1: return n
    return fibonacci(n-1) + fibonacci(n-2)
```

## Recursion On Subsequences

This topic is very **Important**


