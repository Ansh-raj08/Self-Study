# Beginner-Friendly Array Questions with Solutions

## Question 1: Find the Maximum Element in an Array

**Problem:** Given an array of integers, find the maximum element.

**Input:** `[3, 7, 2, 9, 1]`
**Output:** `9`

**Solution:**
```python
def find_max(arr):
    if not arr:  # Handle empty array
        return None

    max_element = arr[0]  # Initialize with first element
    for i in range(1, len(arr)):
        if arr[i] > max_element:
            max_element = arr[i]
    return max_element

# Example usage
numbers = [3, 7, 2, 9, 1]
result = find_max(numbers)
print(f"Maximum element: {result}")  # Output: 9
```

**Explanation:**
- Start by assuming the first element is the maximum
- Compare each subsequent element with the current maximum
- Update the maximum whenever we find a larger element
- Time complexity: O(n), Space complexity: O(1)

---

## Question 2: Find the Sum of All Elements

**Problem:** Calculate the sum of all elements in an array.

**Input:** `[1, 2, 3, 4, 5]`
**Output:** `15`

**Solution:**
```python
def array_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total

# Alternative using built-in function
def array_sum_builtin(arr):
    return sum(arr)

# Example usage
numbers = [1, 2, 3, 4, 5]
result = array_sum(numbers)
print(f"Sum: {result}")  # Output: 15
```

**Explanation:**
- Initialize a variable to store the running sum
- Iterate through each element and add it to the sum
- Return the final sum
- Time complexity: O(n), Space complexity: O(1)

---

## Question 3: Reverse an Array

**Problem:** Reverse the elements of an array without using extra space.

**Input:** `[1, 2, 3, 4, 5]`
**Output:** `[5, 4, 3, 2, 1]`

**Solution:**
```python
def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        # Swap elements at left and right positions
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr

# Example usage
numbers = [1, 2, 3, 4, 5]
reversed_numbers = reverse_array(numbers.copy())  # Use copy to preserve original
print(f"Reversed: {reversed_numbers}")  # Output: [5, 4, 3, 2, 1]
```

**Explanation:**
- Use two pointers: one at the beginning (left) and one at the end (right)
- Swap elements at these positions and move pointers toward center
- Continue until pointers meet in the middle
- Time complexity: O(n), Space complexity: O(1)

---

## Question 4: Check if Array is Sorted

**Problem:** Determine if an array is sorted in ascending order.

**Input:** `[1, 2, 3, 4, 5]`
**Output:** `True`

**Solution:**
```python
def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:  # Current element is smaller than previous
            return False
    return True

# Example usage
numbers1 = [1, 2, 3, 4, 5]
numbers2 = [1, 3, 2, 4, 5]
print(f"Array 1 sorted: {is_sorted(numbers1)}")  # Output: True
print(f"Array 2 sorted: {is_sorted(numbers2)}")  # Output: False
```

**Explanation:**
- Compare each element with its previous element
- If any element is smaller than the previous one, array is not sorted
- If we complete the loop without finding violations, array is sorted
- Time complexity: O(n), Space complexity: O(1)

---

## Question 5: Find Second Largest Element

**Problem:** Find the second largest element in an array.

**Input:** `[3, 7, 2, 9, 1, 8]`
**Output:** `8`

**Solution:**
```python
def find_second_largest(arr):
    if len(arr) < 2:
        return None

    largest = float('-inf')
    second_largest = float('-inf')

    for num in arr:
        if num > largest:
            second_largest = largest  # Previous largest becomes second largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    return second_largest if second_largest != float('-inf') else None

# Example usage
numbers = [3, 7, 2, 9, 1, 8]
result = find_second_largest(numbers)
print(f"Second largest: {result}")  # Output: 8
```

**Explanation:**
- Keep track of both largest and second largest elements
- When we find a new largest, the old largest becomes second largest
- When we find a number larger than second largest (but not largest), update second largest
- Handle edge cases like arrays with fewer than 2 elements or all identical elements
- Time complexity: O(n), Space complexity: O(1)

---

## Question 6: Count Occurrences of an Element

**Problem:** Count how many times a specific element appears in an array.

**Input:** Array: `[1, 2, 3, 2, 2, 4]`, Element: `2`
**Output:** `3`

**Solution:**
```python
def count_occurrences(arr, target):
    count = 0
    for num in arr:
        if num == target:
            count += 1
    return count

# Alternative using built-in method
def count_occurrences_builtin(arr, target):
    return arr.count(target)

# Example usage
numbers = [1, 2, 3, 2, 2, 4]
target = 2
result = count_occurrences(numbers, target)
print(f"Element {target} appears {result} times")  # Output: 3
```

**Explanation:**
- Initialize a counter to zero
- Iterate through the array and increment counter when target is found
- Return the final count
- Time complexity: O(n), Space complexity: O(1)

---

## Question 7: Remove Duplicates from Array

**Problem:** Remove duplicate elements from an array, keeping only unique elements.

**Input:** `[1, 2, 2, 3, 4, 4, 5]`
**Output:** `[1, 2, 3, 4, 5]`

**Solution:**
```python
def remove_duplicates(arr):
    unique_elements = []
    seen = set()

    for num in arr:
        if num not in seen:
            unique_elements.append(num)
            seen.add(num)

    return unique_elements

# Alternative preserving order using list comprehension
def remove_duplicates_alt(arr):
    seen = set()
    return [x for x in arr if not (x in seen or seen.add(x))]

# Example usage
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = remove_duplicates(numbers)
print(f"Without duplicates: {unique_numbers}")  # Output: [1, 2, 3, 4, 5]
```

**Explanation:**
- Use a set to keep track of elements we've already seen
- Only add elements to result if they haven't been seen before
- This preserves the order of first occurrence
- Time complexity: O(n), Space complexity: O(n)

---

## Question 8: Find Missing Number

**Problem:** Given an array containing n-1 numbers from 1 to n, find the missing number.

**Input:** `[1, 2, 4, 5, 6]` (missing 3 from 1-6)
**Output:** `3`

**Solution:**
```python
def find_missing_number(arr, n):
    # Method 1: Using sum formula
    expected_sum = n * (n + 1) // 2  # Sum of 1 to n
    actual_sum = sum(arr)
    return expected_sum - actual_sum

# Method 2: Using XOR (more memory efficient)
def find_missing_number_xor(arr, n):
    xor_all = 0
    xor_arr = 0

    # XOR all numbers from 1 to n
    for i in range(1, n + 1):
        xor_all ^= i

    # XOR all numbers in array
    for num in arr:
        xor_arr ^= num

    return xor_all ^ xor_arr

# Example usage
numbers = [1, 2, 4, 5, 6]
n = 6
missing = find_missing_number(numbers, n)
print(f"Missing number: {missing}")  # Output: 3
```

**Explanation:**
- Method 1: Calculate expected sum of 1 to n, subtract actual sum
- Method 2: Use XOR properties - XOR of all numbers 1 to n, then XOR with array elements
- Both methods work because the missing number is the difference
- Time complexity: O(n), Space complexity: O(1)

---

## Question 9: Rotate Array to the Right

**Problem:** Rotate an array to the right by k positions.

**Input:** Array: `[1, 2, 3, 4, 5]`, k: `2`
**Output:** `[4, 5, 1, 2, 3]`

**Solution:**
```python
def rotate_right(arr, k):
    if not arr or k == 0:
        return arr

    n = len(arr)
    k = k % n  # Handle cases where k > n

    # Method 1: Using slicing
    return arr[-k:] + arr[:-k]

# Method 2: In-place rotation using reversal
def rotate_right_inplace(arr, k):
    if not arr or k == 0:
        return arr

    n = len(arr)
    k = k % n

    # Helper function to reverse a portion of array
    def reverse(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    # Reverse entire array
    reverse(0, n - 1)
    # Reverse first k elements
    reverse(0, k - 1)
    # Reverse remaining elements
    reverse(k, n - 1)

    return arr

# Example usage
numbers = [1, 2, 3, 4, 5]
k = 2
rotated = rotate_right(numbers.copy(), k)
print(f"Rotated by {k}: {rotated}")  # Output: [4, 5, 1, 2, 3]
```

**Explanation:**
- Method 1: Use array slicing to take last k elements and first n-k elements
- Method 2: Use three reversals for in-place rotation
- Handle edge cases like k being larger than array length
- Time complexity: O(n), Space complexity: O(1) for in-place method

---

## Question 10: Merge Two Sorted Arrays

**Problem:** Merge two sorted arrays into one sorted array.

**Input:** `arr1 = [1, 3, 5]`, `arr2 = [2, 4, 6]`
**Output:** `[1, 2, 3, 4, 5, 6]`

**Solution:**
```python
def merge_sorted_arrays(arr1, arr2):
    merged = []
    i = j = 0  # Pointers for arr1 and arr2

    # Compare elements and add smaller one to result
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    # Add remaining elements from arr1 (if any)
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    # Add remaining elements from arr2 (if any)
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged

# Example usage
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
merged = merge_sorted_arrays(arr1, arr2)
print(f"Merged array: {merged}")  # Output: [1, 2, 3, 4, 5, 6]
```

**Explanation:**
- Use two pointers to traverse both arrays simultaneously
- Compare elements at current positions and add smaller one to result
- Move the pointer of the array from which element was taken
- After one array is exhausted, add remaining elements from the other
- Time complexity: O(m + n), Space complexity: O(m + n)

---

## Practice Tips:

1. **Start Simple:** Begin with problems 1-4 to build confidence
2. **Understand Complexity:** Always consider time and space complexity
3. **Handle Edge Cases:** Empty arrays, single elements, duplicates
4. **Test Your Solutions:** Try different inputs including edge cases
5. **Optimize Gradually:** First make it work, then make it better
6. **Practice Regularly:** Consistency is key to mastering arrays

## Key Array Concepts Covered:

- **Traversal:** Iterating through array elements
- **Searching:** Finding specific elements or properties
- **Manipulation:** Modifying array contents
- **Two Pointers:** Efficient technique for many problems
- **Space-Time Tradeoffs:** Using extra space for better time complexity
- **Edge Cases:** Handling empty arrays, single elements, etc.