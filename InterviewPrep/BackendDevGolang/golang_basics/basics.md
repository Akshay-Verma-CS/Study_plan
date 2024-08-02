# Basics of Golang

## Go Package , import and Visibility ([Ref](https://www.javatpoint.com/go-package-import-visibility))

### Packages 

1. Packages are used to categorize our program so that it can be easy to maintain. 
2. Every go-file belongs to some package. Each Go application must have "main" package so that it can be compiled.
3. An application can consist of different packages. Many different .go file can belong to one main package.
4. We can save Go program by any name but it must have main package. The package name should be written in lowercase letters.
5. If a package is changed and recompiled, all the client programs that use this package must be recompiled too!

### Import 

A Go program is linked to different packages through the import keyword.

The package names are enclosed within double quotes "". Import loads the public declarations from the compiled package, it does not insert the source code.

example

```go
import (  
     "fmt"  
     "os"  
)  
```

### Visibility

An identifier can be variable, constant, function, type or struct field. We can declare identifier in lowercase or uppercase letters.

If we declare identifier in lowercase letter, it will be visible within the package only. But if we declare package in uppercase letter, it will be visible within and outside the package which is also known as exported.

The dot . Operator is used to access the identifier e.g. pack.Age where pack is the package name and Age is the identifier.

## Go Controls

---

### 1. **Go if-else**
   - **Syntax**:
     ```go
     if condition {
         // code block
     } else if condition {
         // code block
     } else {
         // code block
     }
     ```
   - **Usage**: Controls flow based on boolean expressions. The `else if` and `else` parts are optional.
   - **Example**:
     ```go
     if x > 10 {
         fmt.Println("x is greater than 10")
     } else if x == 10 {
         fmt.Println("x is 10")
     } else {
         fmt.Println("x is less than 10")
     }
     ```

### 2. **Go Switch**
   - **Syntax**:
     ```go
     switch variable {
     case value1:
         // code block
     case value2:
         // code block
     default:
         // code block
     }
     ```
   - **Usage**: A more readable alternative to multiple `if-else` statements. It can evaluate expressions.
   - **Example**:
     ```go
     switch day {
     case "Monday":
         fmt.Println("Start of the workweek")
     case "Friday":
         fmt.Println("Almost weekend")
     default:
         fmt.Println("Midweek day")
     }
     ```

### 3. **Go For**
   - **Syntax**:
     ```go
     for initializer; condition; increment {
         // code block
     }
     ```
   - **Usage**: The only looping construct in Go. Can act as a traditional loop, a `while` loop, or an infinite loop.
   - **Example**:
     ```go
     for i := 0; i < 10; i++ {
         fmt.Println(i)
     }
     ```

### 4. **Go For Range**
   - **Syntax**:
     ```go
     for index, value := range collection {
         // code block
     }
     ```
   - **Usage**: Iterates over arrays, slices, maps, and strings. The `range` keyword returns both the index and the value.
   - **Example**:
     ```go
     for index, value := range arr {
         fmt.Println(index, value)
     }
     ```

### 5. **Go Goto**
   - **Syntax**:
     ```go
     goto label
     // code block
     label:
         // code block
     ```
   - **Usage**: Transfers control to a labeled statement within the function. Not commonly used due to its potential to create unreadable code.
   - **Example**:
     ```go
     if x > 0 {
         goto positive
     }
     positive:
         fmt.Println("x is positive")
     ```

### 6. **Go Break**
   - **Syntax**:
     ```go
     break
     ```
   - **Usage**: Exits a loop or `switch` statement prematurely.
   - **Example**:
     ```go
     for i := 0; i < 10; i++ {
         if i == 5 {
             break
         }
         fmt.Println(i)
     }
     ```

### 7. **Go Continue**
   - **Syntax**:
     ```go
     continue
     ```
   - **Usage**: Skips the remaining code in the current iteration and proceeds to the next iteration of the loop.
   - **Example**:
     ```go
     for i := 0; i < 10; i++ {
         if i%2 == 0 {
             continue
         }
         fmt.Println(i)
     }
     ```

### 8. **Go Comments**
   - **Single-line**:
     ```go
     // This is a single-line comment
     ```
   - **Multi-line**:
     ```go
     /*
       This is a
       multi-line comment
     */
     ```
   - **Usage**: Used to explain code, which helps with readability and maintainability. Comments are ignored by the compiler.

### 9. **Go Constants**
   - **Syntax**:
     ```go
     const name = value
     ```
   - **Usage**: Defines a value that cannot be changed. Can be of any data type.
   - **Example**:
     ```go
     const Pi = 3.14
     fmt.Println(Pi)
     ```

### 10. **Go Type Casting**
   - **Syntax**:
     ```go
     typeA(value).(typeB)
     ```
   - **Usage**: Converts a value from one data type to another. Explicit type conversion is necessary in Go.
   - **Example**:
     ```go
     var x int = 10
     var y float64 = float64(x)
     fmt.Println(y)
     ```

---

## Go Functions

---

### 1. **Go Functions**
   - **Syntax**:
     ```go
     func functionName(parameters) returnType {
         // code block
     }
     ```
   - **Usage**: Functions encapsulate reusable blocks of code. Go supports multiple return values and named return values.
   - **Example**:
     ```go
     func add(a int, b int) int {
         return a + b
     }
     fmt.Println(add(2, 3))
     ```

### 2. **Go Recursion**
   - **Definition**: A function calling itself directly or indirectly to solve a problem.
   - **Usage**: Useful for tasks that can be divided into similar sub-tasks, such as factorial calculation or tree traversal.
   - **Example**:
     ```go
     func factorial(n int) int {
         if n == 0 {
             return 1
         }
         return n * factorial(n-1)
     }
     fmt.Println(factorial(5)) // Output: 120
     ```

### 3. **Go Closure**
   - **Definition**: A function value that references variables from outside its body.
   - **Usage**: Useful when you need a function with its own private environment.
   - **Example**:
     ```go
     func incrementer() func() int {
         x := 0
         return func() int {
             x++
             return x
         }
     }
     incr := incrementer()
     fmt.Println(incr()) // Output: 1
     fmt.Println(incr()) // Output: 2
     ```

## Go Arrays

---

### 1. **Go Array**
   - **Syntax**:
     ```go
     var arr [size]datatype
     ```
   - **Usage**: Arrays store a fixed-size sequential collection of elements of the same type.
   - **Example**:
     ```go
     var arr [3]int
     arr[0] = 1
     arr[1] = 2
     arr[2] = 3
     fmt.Println(arr)
     ```

### 2. **Go Slice**
   - **Syntax**:
     ```go
     slice := make([]datatype, length, capacity)
     ```
   - **Usage**: Slices are dynamically-sized, more powerful than arrays. Slices are references to an underlying array.
   - **Example**:
     ```go
     slice := []int{1, 2, 3}
     fmt.Println(slice)
     ```

### 3. **Go Command Args**
   - **Definition**: Access command-line arguments passed to a Go program.
   - **Usage**: Useful for writing command-line utilities.
   - **Example**:
     ```go
     import (
         "fmt"
         "os"
     )

     func main() {
         args := os.Args
         fmt.Println("Arguments:", args)
     }
     ```

## Go Strings

---

### 1. **Go String**
   - **Definition**: A sequence of bytes. Strings are immutable in Go.
   - **Usage**: Strings are used to represent text in Go.
   - **Example**:
     ```go
     str := "Hello, Go!"
     fmt.Println(str)
     ```

### 2. **Go Regex**
   - **Definition**: Regular expressions are patterns used to match character combinations in strings.
   - **Usage**: Go’s `regexp` package is used for handling regular expressions.
   - **Example**:
     ```go
     import "regexp"

     func main() {
         match, _ := regexp.MatchString("H(a|e)llo", "Hello")
         fmt.Println(match) // Output: true
     }
     ```

## Go Types

---

### 1. **Go Struct**
   - **Syntax**:
     ```go
     type StructName struct {
         field1 datatype
         field2 datatype
     }
     ```
   - **Usage**: Used to group together variables of different types into a single type.
   - **Example**:
     ```go
     type Person struct {
         Name string
         Age  int
     }

     func main() {
         p := Person{"John", 30}
         fmt.Println(p)
     }
     ```

### 2. **Go Interface**
   - **Definition**: A type that specifies a set of method signatures.
   - **Usage**: Enables polymorphism by allowing different types to implement the same set of methods.
   - **Example**:
     ```go
     type Shape interface {
         Area() float64
     }

     type Circle struct {
         Radius float64
     }

     func (c Circle) Area() float64 {
         return 3.14 * c.Radius * c.Radius
     }

     func main() {
         var s Shape = Circle{Radius: 5}
         fmt.Println(s.Area())
     }
     ```

### 3. **Go Pointer**
   - **Syntax**:
     ```go
     var ptr *datatype
     ptr = &variable
     ```
   - **Usage**: Pointers hold the memory address of a value. Allows for efficient passing of large structs or arrays.
   - **Example**:
     ```go
     var x int = 10
     var ptr *int = &x
     fmt.Println(*ptr) // Output: 10
     ```

### 4. **Go Reflect**
   - **Definition**: A package in Go that allows inspection of types at runtime.
   - **Usage**: Useful for writing generic code, though it can be complex and less efficient.
   - **Example**:
     ```go
     import (
         "fmt"
         "reflect"
     )

     func main() {
         var x float64 = 3.4
         fmt.Println(reflect.TypeOf(x)) // Output: float64
     }
     ```

### 5. **Go Rune**
   - **Definition**: A Unicode code point in Go, which is an alias for `int32`.
   - **Usage**: Useful for handling individual characters in strings, especially non-ASCII.
   - **Example**:
     ```go
     for _, r := range "Hello, 世界" {
         fmt.Printf("%c ", r)
     }
     ```

## Go Map

---

### 1. **Go Map**
   - **Syntax**:
     ```go
     var m map[keyType]valueType
     m = make(map[keyType]valueType)
     ```
   - **Usage**: Maps are Go’s built-in associative data type (hash table), allowing for the storage of key-value pairs.
   - **Example**:
     ```go
     m := make(map[string]int)
     m["a"] = 1
     m["b"] = 2
     fmt.Println(m)
     ```

## Go Error

---

### 1. **Go Error**
   - **Syntax**:
     ```go
     err := errors.New("error message")
     ```
   - **Usage**: Go handles errors by returning an error value as the last return value of functions. The built-in `error` interface is used for error handling.
   - **Example**:
     ```go
     import (
         "errors"
         "fmt"
     )

     func divide(a, b int) (int, error) {
         if b == 0 {
             return 0, errors.New("division by zero")
         }
         return a / b, nil
     }

     func main() {
         result, err := divide(10, 0)
         if err != nil {
             fmt.Println("Error:", err)
         } else {
             fmt.Println("Result:", result)
         }
     }
     ```

### 2. **Go Recover**
   - **Definition**: A built-in function that allows the program to manage the panic and recover from it, typically used inside `defer` functions.
   - **Usage**: Helps to gracefully handle panics and prevent the program from crashing.
   - **Example**:
     ```go
     func main() {
         defer func() {
             if r := recover(); r != nil {
                 fmt.Println("Recovered from", r)
             }
         }()
         panic("something went wrong")
     }
     ```

### 3. **Go Defer**
   - **Definition**: A keyword that postpones the execution of a function until the surrounding function returns.
   - **Usage**: Often used to ensure that cleanup tasks like file closing or unlocking mutexes happen at the end of a function.
   - **Example**:
     ```go
     func main() {
         defer fmt.Println("Deferred call")
         fmt.Println("Regular call")
     }
     // Output:
     // Regular call
     // Deferred call
     ```

### 4. **Go Panic**
   - **Definition**: A function that causes a runtime error and stops the normal execution of the program.
   - **Usage**: Used when the program encounters an error that it cannot recover from.
   - **Example**:
     ```go
     func main() {
         panic("an unrecoverable error occurred")
         fmt.Println("This line will not execute")
     }
     ```

---

