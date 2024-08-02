# Go Practice Questions

## Go Controls

1. **if-else Statements:**
   - Write a function that takes an integer and returns whether the number is positive, negative, or zero using if-else statements.

2. **Switch Statement:**
   - Create a switch statement that prints out the name of the day of the week based on an integer input (1 for Monday, 7 for Sunday).

3. **For Loop:**
   - Write a program that prints the first 10 Fibonacci numbers using a for loop.

4. **For Range Loop:**
   - Write a function that calculates the sum of all elements in a slice using a for range loop.

5. **Goto Statement:**
   - Implement a function that uses the `goto` statement to retry an operation a specified number of times before giving up.

6. **Break and Continue:**
   - Write a loop that processes a list of integers, skipping negative numbers (`continue`) and stopping entirely if a zero is encountered (`break`).

## Go Functions

7. **Basic Function:**
   - Write a function that takes two integers and returns their sum. Then, modify it to return their product as well.

8. **Recursion:**
   - Implement a recursive function to calculate the factorial of a given number.

9. **Closure:**
   - Create a closure in Go that captures a variable from its environment and increments it every time the closure is called.

## Go Arrays

10. **Array Operations:**
    - Create an array of integers and write a function that calculates the average of its elements.

11. **Slice Operations:**
    - Write a function that takes a slice of integers and returns a new slice containing only the even numbers.

12. **Command-line Arguments:**
    - Write a program that reads command-line arguments and prints them out, one per line.

## Go Strings

13. **String Operations:**
    - Write a function that reverses a given string.

14. **Regex:**
    - Write a program that uses regex to validate an email address format.

## Go Types

15. **Structs:**
    - Define a struct `Person` with fields for name and age. Write a function that takes a `Person` and returns a formatted string like "Name: John, Age: 30".

16. **Interfaces:**
    - Create an interface `Shape` with a method `Area() float64`. Implement this interface for two types: `Circle` and `Rectangle`.

17. **Pointers:**
    - Write a function that takes a pointer to an integer and increments the value it points to by 1.

18. **Reflection:**
    - Write a program that uses the `reflect` package to print the type and value of a variable.

19. **Runes:**
    - Write a function that counts the number of runes in a string, ensuring it handles multibyte characters correctly.

## Go Map

20. **Map Operations:**
    - Create a map that associates names (strings) with ages (integers). Write a function that finds the average age of all entries in the map.

21. **Check and Delete from Map:**
    - Write a function that checks if a given key exists in a map and removes it if it does.

## Go Error Handling

22. **Custom Error:**
    - Write a function that returns an error if a given string is empty. Then, handle this error in a way that informs the user.

23. **Recover:**
    - Write a function that deliberately panics and then recovers from the panic using `defer` and `recover`.

24. **Defer:**
    - Write a function that opens a file and ensures it is closed properly using `defer`.

25. **Panic:**
    - Create a scenario where a `panic` occurs if an invalid operation is attempted (e.g., division by zero). Handle this using `recover`.

## Go Concurrency

26. **Basic Goroutine:**
    - Write a program that launches a goroutine to print "Hello from Goroutine!" and ensures the main function waits for it to finish.

27. **Race Condition:**
    - Create a program that demonstrates a race condition. Then, fix it using a mutex.

28. **Mutex:**
    - Implement a counter that is safely incremented by multiple goroutines using a mutex to prevent race conditions.

29. **Atomic Variable:**
    - Rewrite the above counter using atomic operations instead of a mutex.

30. **Channel Communication:**
    - Write a program where two goroutines communicate through a channel. One goroutine should send numbers to the channel, and the other should print them.

31. **Worker Pool:**
    - Create a simple worker pool where multiple goroutines process jobs from a job queue.

## Go Time

32. **Current Time:**
    - Write a function that prints the current date and time in the format `YYYY-MM-DD HH:MM:SS`.

33. **Unix Epoch:**
    - Write a program that prints the current Unix time and then converts it back to a human-readable format.

34. **Ticker:**
    - Implement a ticker that prints "Tick" every second for 10 seconds.

## Go Misc

35. **File I/O:**
    - Write a program that reads from one file and writes the contents to another file. Ensure the program handles errors, such as missing files.

36. **HTTP Server:**
    - Create an HTTP server with a single endpoint `/greet` that responds with a JSON object containing a greeting message.

37. **URL Parsing:**
    - Write a function that parses a URL and extracts the protocol, host, and path components.

38. **REST API:**
    - Implement a basic REST API with endpoints to create, read, update, and delete (CRUD) records of a `Product` struct.

39. **Base64 Encoding:**
    - Write a function that encodes a string into Base64 and then decodes it back to the original string.

40. **Random Number:**
    - Write a program that generates a random number between 1 and 100 and asks the user to guess the number.

41. **Sorting:**
    - Write a function that sorts a slice of strings alphabetically.

42. **JSON Encoding/Decoding:**
    - Write a function that encodes a struct to JSON and then decodes the JSON back into a struct.
