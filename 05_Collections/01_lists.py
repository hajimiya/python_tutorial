numbers = [10, 20, 30]
numbers.append(40)
numbers.extend([50, 60])
numbers.insert(1, 15)
print(numbers)
numbers.remove(30)  # Removes the first matching value
last = numbers.pop() # Returns and removes the last item
print("popped:", last, numbers)
numbers.sort()
print("sorted:", numbers)
print("length:", len(numbers), "count of 20:", numbers.count(20))
print("first two:", numbers[:2])
