# Go Misc

These notes cover miscellaneous Go programming topics, including file I/O, HTTP servers, URL parsing, REST APIs, Base64 encoding, random numbers, sorting, and JSON handling.

---

### 1. **Go File I/O**
   - **Reading Files**:
     - **Syntax**:
       ```go
       data, err := ioutil.ReadFile("filename.txt")
       ```
     - **Usage**: Reads the entire content of a file into memory.
     - **Example**:
       ```go
       package main

       import (
           "fmt"
           "io/ioutil"
       )

       func main() {
           data, err := ioutil.ReadFile("example.txt")
           if err != nil {
               fmt.Println("Error reading file:", err)
               return
           }
           fmt.Println("File content:", string(data))
       }
       ```
   - **Writing Files**:
     - **Syntax**:
       ```go
       err := ioutil.WriteFile("filename.txt", data, 0644)
       ```
     - **Usage**: Writes data to a file, replacing its contents if it already exists.
     - **Example**:
       ```go
       data := []byte("Hello, Go!")
       err := ioutil.WriteFile("example.txt", data, 0644)
       if err != nil {
           fmt.Println("Error writing to file:", err)
       }
       ```
   - **Append to File**:
     - **Syntax**:
       ```go
       f, err := os.OpenFile("filename.txt", os.O_APPEND|os.O_WRONLY, 0644)
       ```
     - **Usage**: Opens a file for appending data.
     - **Example**:
       ```go
       f, err := os.OpenFile("example.txt", os.O_APPEND|os.O_WRONLY, 0644)
       if err != nil {
           fmt.Println("Error opening file:", err)
           return
       }
       defer f.Close()

       if _, err = f.WriteString("More data\n"); err != nil {
           fmt.Println("Error writing to file:", err)
       }
       ```

### 2. **Go HTTP Server**
   - **Creating a Basic HTTP Server**:
     - **Syntax**:
       ```go
       http.ListenAndServe(":8080", nil)
       ```
     - **Usage**: Starts an HTTP server listening on the specified port.
     - **Example**:
       ```go
       package main

       import (
           "fmt"
           "net/http"
       )

       func handler(w http.ResponseWriter, r *http.Request) {
           fmt.Fprintf(w, "Hello, Go HTTP Server!")
       }

       func main() {
           http.HandleFunc("/", handler)
           fmt.Println("Starting server on :8080")
           http.ListenAndServe(":8080", nil)
       }
       ```
   - **Routing**:
     - **Usage**: Handle different routes using `http.HandleFunc`.
     - **Example**:
       ```go
       http.HandleFunc("/hello", helloHandler)
       http.HandleFunc("/goodbye", goodbyeHandler)
       ```

### 3. **Go URL Parsing**
   - **Parsing URLs**:
     - **Syntax**:
       ```go
       u, err := url.Parse("https://example.com/path?query=value")
       ```
     - **Usage**: Parses a raw URL string into its components (scheme, host, path, query, etc.).
     - **Example**:
       ```go
       package main

       import (
           "fmt"
           "net/url"
       )

       func main() {
           u, err := url.Parse("https://example.com/path?query=value")
           if err != nil {
               fmt.Println("Error parsing URL:", err)
               return
           }
           fmt.Println("Scheme:", u.Scheme)
           fmt.Println("Host:", u.Host)
           fmt.Println("Path:", u.Path)
           fmt.Println("Query:", u.RawQuery)
       }
       ```

### 4. **Go REST API**
   - **Creating a REST API**:
     - **Syntax**:
       ```go
       http.HandleFunc("/api/resource", resourceHandler)
       ```
     - **Usage**: Define routes and handlers for different API endpoints.
     - **Example**:
       ```go
       package main

       import (
           "encoding/json"
           "net/http"
       )

       type Response struct {
           Message string `json:"message"`
       }

       func resourceHandler(w http.ResponseWriter, r *http.Request) {
           w.Header().Set("Content-Type", "application/json")
           json.NewEncoder(w).Encode(Response{Message: "Hello, REST API!"})
       }

       func main() {
           http.HandleFunc("/api/resource", resourceHandler)
           http.ListenAndServe(":8080", nil)
       }
       ```
   - **Handling Methods (GET, POST, etc.)**:
     - **Usage**: Check the HTTP method using `r.Method`.
     - **Example**:
       ```go
       if r.Method == http.MethodGet {
           // Handle GET request
       } else if r.Method == http.MethodPost {
           // Handle POST request
       }
       ```

### 5. **Go Base64 Encoding**
   - **Encoding to Base64**:
     - **Syntax**:
       ```go
       encoded := base64.StdEncoding.EncodeToString(data)
       ```
     - **Usage**: Converts binary data to a Base64 encoded string.
     - **Example**:
       ```go
       package main

       import (
           "encoding/base64"
           "fmt"
       )

       func main() {
           data := "Hello, Go!"
           encoded := base64.StdEncoding.EncodeToString([]byte(data))
           fmt.Println("Encoded:", encoded)
       }
       ```
   - **Decoding Base64**:
     - **Syntax**:
       ```go
       decoded, err := base64.StdEncoding.DecodeString(encoded)
       ```
     - **Usage**: Converts a Base64 encoded string back to binary data.
     - **Example**:
       ```go
       decoded, err := base64.StdEncoding.DecodeString(encoded)
       if err != nil {
           fmt.Println("Error decoding:", err)
           return
       }
       fmt.Println("Decoded:", string(decoded))
       ```

### 6. **Go Random Number**
   - **Generating Random Numbers**:
     - **Syntax**:
       ```go
       n := rand.Intn(max)
       ```
     - **Usage**: Generates a random integer between 0 and `max-1`.
     - **Example**:
       ```go
       package main

       import (
           "fmt"
           "math/rand"
           "time"
       )

       func main() {
           rand.Seed(time.Now().UnixNano())
           fmt.Println("Random number:", rand.Intn(100))
       }
       ```
   - **Random Float**:
     - **Syntax**:
       ```go
       f := rand.Float64()
       ```
     - **Usage**: Generates a random float between 0.0 and 1.0.
     - **Example**:
       ```go
       f := rand.Float64()
       fmt.Println("Random float:", f)
       ```

### 7. **Go Sorting**
   - **Sorting Slices**:
     - **Syntax**:
       ```go
       sort.Ints(slice)
       ```
     - **Usage**: Sorts a slice of integers in ascending order.
     - **Example**:
       ```go
       package main

       import (
           "fmt"
           "sort"
       )

       func main() {
           numbers := []int{3, 1, 4, 1, 5, 9}
           sort.Ints(numbers)
           fmt.Println("Sorted:", numbers)
       }
       ```
   - **Custom Sorting**:
     - **Syntax**:
       ```go
       sort.Slice(slice, func(i, j int) bool {
           return slice[i] < slice[j]
       })
       ```
     - **Usage**: Sorts a slice based on a custom comparison function.
     - **Example**:
       ```go
       sort.Slice(people, func(i, j int) bool {
           return people[i].Age < people[j].Age
       })
       ```

### 8. **Go JSON**
   - **Encoding to JSON**:
     - **Syntax**:
       ```go
       json.NewEncoder(w).Encode(data)
       ```
     - **Usage**: Serializes Go data structures to JSON format.
     - **Example**:
       ```go
       package main

       import (
           "encoding/json"
           "fmt"
       )

       type Person struct {
           Name string `json:"name"`
           Age  int    `json:"age"`
       }

       func main() {
           person := Person{Name: "Alice", Age: 25}
           jsonData, err := json.Marshal(person)
           if err != nil {
               fmt.Println("Error encoding JSON:", err)
               return
           }
           fmt.Println("JSON:", string(jsonData))
       }
       ```
   - **Decoding JSON**:
     - **Syntax**:
       ```go
       err := json.NewDecoder(r.Body).Decode(&data)
       ```
     - **Usage**: Deserializes JSON data into Go data structures.
     - **Example**:
       ```go
       var person Person
       err := json.Unmarshal(jsonData, &person)
       if err != nil {
           fmt.Println("Error decoding JSON:", err)
           return
       }
       fmt.Println("Decoded:", person)
       ```

