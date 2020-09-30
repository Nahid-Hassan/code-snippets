Here is my fibonacci code:
    
    def fib1(n: int) -> int:
        if n < 2: # base case
            return n
        return fib1(n -1) + fib1(n - 2)

    if __name__ == "__main__":
        print(fib1(50))
## Using code blocks
    How to use code blocks
    ```language_type
        Write your code here
        Or paste your code here
    ```
    For python:
    ```py
       Write your code here.
    ```
    For java
    ```java
       write your code here.
    ```

```py
def fib1(n: int) -> int:
    if n < 2: # base case
        return n
    return fib1(n -1) + fib1(n - 2)

if __name__ == "__main__":
    print(fib1(50))
```

Hey did you try `print(fib1(10))`

## Use diff
    ```diff
        - for delete a line
        + for add a line
    ```

```diff
var x = 10;
- var y = 100;
+ var y = 300;

```