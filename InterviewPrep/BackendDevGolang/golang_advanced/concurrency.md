# Go Concurrency

---

### 1. **Go Concurrency**
   - **Definition**: Concurrency in Go is the ability to perform multiple tasks simultaneously. Go achieves concurrency through goroutines and channels.
   - **Goroutines**: 
     - **Definition**: A lightweight thread managed by the Go runtime.
     - **Syntax**:
       ```go
       go functionName()
       ```
     - **Usage**: Goroutines are used to execute functions concurrently. They are cheaper than threads, making Go efficient for concurrent tasks.
     - **Example**:
       ```go
       func sayHello() {
           fmt.Println("Hello")
       }

       func main() {
           go sayHello()
           fmt.Println("Main function")
       }
       ```
     - **Notes**: The `main` function must wait for goroutines to complete, or the program may terminate before they run.

   - **Channels**:
     - **Definition**: Channels are the pipes that connect concurrent goroutines. They allow goroutines to communicate with each other and synchronize their execution.
     - **Syntax**:
       ```go
       ch := make(chan type)
       ch <- value // send value to channel
       value := <-ch // receive value from channel
       ```
     - **Usage**: Used to pass data between goroutines safely.
     - **Example**:
       ```go
       func sum(a int, b int, ch chan int) {
           ch <- a + b
       }

       func main() {
           ch := make(chan int)
           go sum(1, 2, ch)
           fmt.Println(<-ch) // Output: 3
       }
       ```

### 2. **Go Race**
   - **Definition**: A race condition occurs when multiple goroutines read and write shared variables concurrently, leading to unpredictable behavior.
   - **Race Detector**:
     - Go provides a race detector to identify race conditions.
     - **Usage**: Run the program with the `-race` flag to detect race conditions.
       ```bash
       go run -race yourprogram.go
       ```
   - **Prevention**: Use synchronization primitives like `Mutex`, `Channels`, or `Atomic` operations to avoid race conditions.

### 3. **Go Mutex**
   - **Definition**: A mutex is a mutual exclusion lock that prevents multiple goroutines from accessing shared resources simultaneously.
   - **Types**:
     - **sync.Mutex**: Used to lock critical sections of code.
     - **sync.RWMutex**: Allows multiple readers but only one writer at a time.
   - **Usage**:
     ```go
     var mu sync.Mutex

     func main() {
         mu.Lock()
         // Critical section
         mu.Unlock()
     }
     ```
   - **Example**:
     ```go
     var mu sync.Mutex
     var counter int

     func increment() {
         mu.Lock()
         counter++
         mu.Unlock()
     }

     func main() {
         for i := 0; i < 1000; i++ {
             go increment()
         }
         time.Sleep(time.Second)
         fmt.Println("Final Counter:", counter)
     }
     ```
   - **Notes**: Always unlock a mutex in the same function where it was locked to prevent deadlocks.

### 4. **Go Atomic Variable**
   - **Definition**: Atomic operations allow safe access to variables without using locks.
   - **Package**: `sync/atomic`
   - **Usage**: Useful for simple counters or flags where the overhead of mutexes is unnecessary.
   - **Syntax**:
     ```go
     atomic.AddInt32(&variable, delta)
     atomic.LoadInt32(&variable)
     atomic.StoreInt32(&variable, newValue)
     ```
   - **Example**:
     ```go
     var counter int32

     func increment() {
         atomic.AddInt32(&counter, 1)
     }

     func main() {
         for i := 0; i < 1000; i++ {
             go increment()
         }
         time.Sleep(time.Second)
         fmt.Println("Final Counter:", atomic.LoadInt32(&counter))
     }
     ```
   - **Notes**: Atomic operations are faster but limited in functionality compared to mutexes.

### 5. **Go Channel**
   - **Definition**: Channels are used for communication between goroutines, ensuring safe data transfer.
   - **Types**:
     - **Buffered Channels**: Allow sending multiple values before the channel is blocked.
       - **Syntax**:
         ```go
         ch := make(chan int, bufferSize)
         ```
     - **Unbuffered Channels**: Block the sender until the receiver is ready to receive.
       - **Syntax**:
         ```go
         ch := make(chan int)
         ```
   - **Closing Channels**:
     - **Usage**: Closing a channel signals that no more data will be sent on it.
     - **Syntax**:
       ```go
       close(ch)
       ```
     - **Example**:
       ```go
       ch := make(chan int, 5)
       go func() {
           for i := 0; i < 5; i++ {
               ch <- i
           }
           close(ch)
       }()
       
       for v := range ch {
           fmt.Println(v)
       }
       ```
   - **Select Statement**:
     - **Definition**: A `select` statement is used to wait on multiple channel operations.
     - **Syntax**:
       ```go
       select {
       case msg := <-ch1:
           // Process msg
       case ch2 <- msg:
           // Send msg
       default:
           // Default case
       }
       ```
     - **Usage**: Helps in handling multiple channels and implementing timeouts.

### 6. **Go Worker Pools**
   - **Definition**: A pattern where a set of worker goroutines is used to process jobs concurrently, improving efficiency.
   - **Usage**: Useful for tasks that can be parallelized, such as processing files, web scraping, etc.
   - **Implementation**:
     1. **Create a Job Channel**: Where tasks are sent.
     2. **Spawn Workers**: Goroutines that listen on the job channel and process tasks.
     3. **Send Tasks**: Into the job channel.
   - **Example**:
     ```go
     func worker(id int, jobs <-chan int, results chan<- int) {
         for j := range jobs {
             fmt.Printf("Worker %d processing job %d\n", id, j)
             results <- j * 2
         }
     }

     func main() {
         jobs := make(chan int, 100)
         results := make(chan int, 100)

         for w := 1; w < 4; w++ {
             go worker(w, jobs, results)
         }

         for j := 1; j <= 9; j++ {
             jobs <- j
         }
         close(jobs)

         for a := 1; a <= 9; a++ {
             fmt.Println(<-results)
         }
     }
     ```
   - **Notes**: Worker pools help in managing resources efficiently by controlling the number of active goroutines.
