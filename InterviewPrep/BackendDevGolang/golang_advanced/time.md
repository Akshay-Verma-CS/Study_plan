# Go Time

---

### 1. **Go Time**
   - **Definition**: Go provides the `time` package to handle time-related functionality such as measuring time, parsing dates, formatting dates, and more.
   - **Current Time**:
     - **Syntax**:
       ```go
       currentTime := time.Now()
       ```
     - **Usage**: Returns the current local time.
     - **Example**:
       ```go
       package main

       import (
           "fmt"
           "time"
       )

       func main() {
           currentTime := time.Now()
           fmt.Println("Current Time: ", currentTime)
       }
       ```
   - **Formatting Time**:
     - **Syntax**:
       ```go
       formattedTime := currentTime.Format("2006-01-02 15:04:05")
       ```
     - **Usage**: Formats the time according to a specified layout. The layout must follow the reference time `"Mon Jan 2 15:04:05 MST 2006"`.
     - **Example**:
       ```go
       formattedTime := currentTime.Format("2006-01-02 15:04:05")
       fmt.Println("Formatted Time: ", formattedTime)
       ```

   - **Parsing Time**:
     - **Syntax**:
       ```go
       parsedTime, err := time.Parse("2006-01-02", "2024-08-02")
       ```
     - **Usage**: Converts a string into a `time.Time` object according to a specified layout.
     - **Example**:
       ```go
       parsedTime, err := time.Parse("2006-01-02", "2024-08-02")
       if err != nil {
           fmt.Println("Error parsing time:", err)
       } else {
           fmt.Println("Parsed Time: ", parsedTime)
       }
       ```

### 2. **Go Epoch**
   - **Definition**: The Unix epoch is the number of seconds that have elapsed since 00:00:00 Coordinated Universal Time (UTC), Thursday, 1 January 1970.
   - **Current Unix Time**:
     - **Syntax**:
       ```go
       currentUnixTime := time.Now().Unix()
       ```
     - **Usage**: Returns the current Unix time in seconds.
     - **Example**:
       ```go
       currentUnixTime := time.Now().Unix()
       fmt.Println("Current Unix Time: ", currentUnixTime)
       ```
   - **Unix Time to Time Object**:
     - **Syntax**:
       ```go
       timeObj := time.Unix(unixTime, 0)
       ```
     - **Usage**: Converts a Unix time (seconds since the epoch) to a `time.Time` object.
     - **Example**:
       ```go
       timeObj := time.Unix(1690993200, 0)
       fmt.Println("Time Object: ", timeObj)
       ```
   - **Elapsed Time**:
     - **Syntax**:
       ```go
       elapsed := time.Since(startTime)
       ```
     - **Usage**: Measures the time elapsed since a particular `time.Time` object.
     - **Example**:
       ```go
       startTime := time.Now()
       time.Sleep(2 * time.Second)
       elapsed := time.Since(startTime)
       fmt.Println("Elapsed Time: ", elapsed)
       ```

### 3. **Go Tickers**
   - **Definition**: A ticker is used to send events periodically at a specified interval. It’s useful for timing operations that need to occur regularly.
   - **Creating a Ticker**:
     - **Syntax**:
       ```go
       ticker := time.NewTicker(time.Duration)
       ```
     - **Usage**: The ticker will send the current time on its channel every `Duration` interval.
     - **Example**:
       ```go
       ticker := time.NewTicker(1 * time.Second)
       defer ticker.Stop()

       for t := range ticker.C {
           fmt.Println("Tick at", t)
       }
       ```
   - **Stopping a Ticker**:
     - **Syntax**:
       ```go
       ticker.Stop()
       ```
     - **Usage**: Stops the ticker to release resources. Always call `Stop()` to prevent memory leaks.
     - **Example**:
       ```go
       func main() {
           ticker := time.NewTicker(1 * time.Second)
           defer ticker.Stop()

           go func() {
               for t := range ticker.C {
                   fmt.Println("Tick at", t)
               }
           }()
           time.Sleep(5 * time.Second)
           fmt.Println("Ticker stopped")
       }
       ```
   - **Use Cases**:
     - **Heartbeat signals**: Regularly send a signal to ensure a service is alive.
     - **Periodic tasks**: Perform an operation at regular intervals.
