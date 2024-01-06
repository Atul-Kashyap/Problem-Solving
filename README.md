# Problem-Solving


**JAVA**









**Python**

1. Queue
Implement Queue using List
```
    # Create an empty list to act as a queue
    queue = []

    # Enqueue elements to the queue
    queue.append(1)
    queue.append(2)
    queue.append(3)

    # Dequeue elements from the queue
    print(queue.pop(0))  # Output: 1
    print(queue.pop(0))  # Output: 2
    print(queue.pop(0))  # Output: 3
```
Implement Queue usign inbuilt queue
```
    import queue

    # Create a new queue
    q = queue.Queue()

    # Add elements to the queue
    q.put(1)
    q.put(2)
    q.put(3)

    # Get and remove elements from the queue
    print(q.get())  # Output: 1
    print(q.get())  # Output: 2
    print(q.get())  # Output: 3

```

Implement Queue using collections dequeue
```
    from collections import deque

    Create a deque
    d = deque([1, 2, 3])

    Append and pop elements from both ends
    d.append(4)  # Append to the right
    d.appendleft(0)  # Append to the left
    d.pop()  # Remove from the right
    d.popleft()  # Remove from the left

```
