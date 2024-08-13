# CSE3110 - Iterative Algorithms
Iterative algorithms are algorithms that use loops to process large amounts of data. This includes while loops and for loops. In construct, Recursive algorithms are functions that call the same function over and over again to divide a large set of data into smaller and smaller sets. Once the function has the smallest set possible, it will process the data of the set. Interactive algorithms tend to be easier to program, but the overall efficiency of the algorithms will increase when recursive aspects are applied. 

While sort algorithms can sort a wide variety of entities (i.e. numbers, Strings, etc.), these units will focus on sorting integers. 

## Linear Search
Linear Search is the easiest to program but least efficient method of search. It processes the data line-by- line, similar to brute force decryption algorithms.

```python
FOUND = False
for i in range(len(A_LIST)):
    if A_LIST[i] == VALUE
        FOUND = True
        break
```

Linear search processing time is dependent on the length of the arrays. Arrays that are 10 000 indices or higher can take a noticeable amount of time to process.

### Measuring processing time
We use ```time.perf_counter()``` as a measuring tool for the efficiency of an algorithm. It will record the approximate process length at the time it is run. 

For accurate results, we use the average of thirty trails and then use ```statistics.mean()```. 

## Binary Search

Binary Search follows the _divide and conquer_ technique of finding a value. It takes an **ordered** set of data and tests the midpoint value. Then it cuts the list in half and reruns the process. 

### Steps for Binary Search
1. Determine the midpoint index of the list. (Floor divide)
2. Test if the midpoint value is the same as the searched value
   1. If the midpoint value and searched value match, end.
   2. If the midpoint value is greater than the searched value, define the highest index value in the range as being one below the midpoint index. 
   3. If the midpoint value is less than the searched value, define the lowest index of the range as being one above the midpoint index.
3. Repeat until value is found.


* Advantages of Binary Search
  * It is significantly faster than linear search
* Disadvantages of Binary Search
  * List must already be ordered
  * List must contain the same data type

## Sorting Data
Just like searching algorithms, sorting algorithms have a varying level of efficiency. There are several types of sort algorithms including bubble, selection, insertions, and merge. (Python uses Timsort, which is a hybrid of merge and insertion sort designed by Tim Peters in 2002).

Sorting algorithms exist to optimize memory usage. Historic computers did not have enough ram to hold multiple list in memory. While this limitation does not exist in modern computers, for data storage and management on a global scale, resources are still limited. The efficiency of processing algorithms is still noticeable today. 

### Bubble Sort
Bubble sort compares two adjacent values on the list and arranges them from lowest to highest. Then it moves to the next index pari and repeats until it reaches the end of the unsorted list. 

Advantages are that it is easy to program and takes less memory, but the disadvantages are that its processing time is directly proportional to the square of the length of the dataset. However, the set is often fully sorted before the last iteration. 

| 1 | 5 | 3 | 19 | 11 | 17 | 7 | 13 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 5 | 11 | 17 | 7 | 13 | __19__ |
| 1 | 3 | 5 | 11 | 7 | 13 | __17__ | 19 |
| 1 | 3 | 5 | 7 | 11 | __13__ | 17 | 19 |
| 1 | 3 | 5 | 7 | __11__ | 13 | 17 | 19 |
| 1 | 3 | 5 | __7__ | 11 | 13 | 17 | 19 |
| 1 | 3 | __5__ | 7 | 11 | 13 | 17 | 19 |
| 1 | __3__ | 5 | 7 | 11 | 13 | 17 | 19 |


### Selection Sort
Selection sort compares the current index value with the rest of the set. It will store the index of the lowest and switch its position with the lowest index of the unsorted section of the list.


| 1 | 5 | 3 | 19 | 11 | 17 | 7 | 13 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| __*1*__ | 5 | 3 | 19 | 11 | 17 | 7 | 13 |
| 1 | __3__ | _5_ | 19 | 11 | 17 | 7 | 13 |
| 1 | 3 | __*5*__ | 19 | 11 | 17 | 7 | 13 |
| 1 | 3 | 5 | __7__ | 11 | 17 | _19_ | 13 |
| 1 | 3 | 5 | 7 | __*11*__ | 17 | 19 | 13 |
| 1 | 3 | 5 | 7 | 11 | __13__ | 19 | _17_ |
| 1 | 3 | 5 | 7 | 11 | 13 | __17__ | _19_ |

### Insertion Sort
Insertion Sort splits the list into two sections sorted and unsorted. As it progresses through the list, it takes the value at the lowest index of the unsorted half of the list and places it in the correct relative location in the sorted section of the list.

| 1 | 5 | 3 | 19 | 11 | 17 | 7 | 13 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |__*5*__ | 3 | 19 | 11 | 17 | 7 | 13 |
| 1 | _3_ | __5__ | 19 | 11 | 17 | 7 | 13 |
| 1 | 3 | 5 | __*19*__ | 11 | 17 | 7 | 13 |
| 1 | 3 | 5 | _11_ | __19__ | 17 | 7 | 13 |
| 1 | 3 | 5 | _7_ | 11 | 17 | __19__ | 13 |
| 1 | 3 | 5 | 7 | 11 | _13_ | 17 | __19__ | 

# CSE3110 - Recursive Algorithm Notes

A __recusive algorithm__ calls itself with smaller or simpler datasets. Recursive algorithms have a _base case_, which is the simplest input values. Then there are subprocesses that simplify more complex datasets and return the simplified database into a new instance of the same algorithm. 

All iterative algorithms can be written recursively and vice versa; certain functions are easier to write in one from over another. 

## Example 1: Testing for the correct input data
```python
def checkInt(VALUE):
    if VALUE.isnumeric(): # base case
        return int(VALUE)
    else:
        NEW_VALUE = input("Number: ") # update to the data going into the function
        checkInt(NEW_VALUE) # calling the function with the new data


def checkInt2(VALUE): 
    while True:
        if VALUE.isnumeric():
            return int(VALUE)
        else:
            VALUE = input("Number: ")

```

## Iteration vs. Recursion
In general, iterative algorithms require more lines of code and more variables to create. It relies on while and for loops to complete the process. Iterative algorithms work best with consistent changes (i.e. counting, traversing, etc.) Whereas, recursive algorithms do not use as many variables and rely on return values that are re-entered into the function to continue processing the data. Recursion can use more physical memory than iterative algorithms because each instance of the recursive function must stay in memory until the base case is found. Because recursive algorithms can manipulate the data before recurring back into the function, it can change data in way iteration cannot. Finally, iterative functions tend to be faster than exclusive recursive ones.  

Hybrid iterative and recursive algorithms are often faster than exclusively iterative or exclusively recursive algorithms. 

## Example 2: Factorials
### Calculate 7!

```
7! = 7 * 6 * 5 * 4 * 3 * 2 * 1 * 1 = 5040
// BUT 
6! = 6 * 5 * 4 * 3 * 2 * 1 * 1 
// WE CAN REWRITE 7!
7! = 7 * 6!
// EXTEND this reasoning
7! = 7 * (6 * (5 * (4 * (3 * (2 * (1 * (1)))))))
// GENERALIZE the statement
f(x) = x * f(x-1), x > 0
    and
f(x) = 1, x = 0
```

## Sorting
Recursive sorting uses both recursive and iterative processes. In general, these hybrid sort algorithms are exponentially faster with longer lists. (They are measured on a logarithmic scale).

### Merge Sort
Merge sort follows a divide and conquer method of sorting, where the array is split into its base length and then rebuilt by combining progressively larger sorted lists together. The recursive portion is the splitting of the lists and the iterative process is the actual merging of two smaller sorted lists. 

Oftentimes, this function is separated into splitting and merging functions.

### Quick Sort
Quick Sort (quicksort) is another divide and conquer method of sorting. Quicksort utilizes an arbitrary value as its pivot, which is then used to place the pivot value in the correct index position in the array. It does this by placing all smaller values to the left of the pivot and all larger values to the right of the pivot. Then it places the pivot value where the smaller and larger portions intersect and moves to the next value. It then recurs through the algorithm until the inputted list is one value long. 

NOTE: Quicksort efficiency is from separating the list into two sections that will never compare values with each other again. 

### Heap Sort

Heap Sort uses a binary tree organization of an array to sort higher values on the top of the tree. The process of moving larger values higher in the binary tree is called __heapifying__ (or to heapify). To build the binary tree, each index (starting at 0) will have a left child and a right child (hence binary tree). The index values can be calculated from the following:

```
left_child = 2 * parentIndex + 1
right_child = 2 * parentIndex + 2

# sample tree
LIST = [5, 17, 13, 11, 1, 7, 3]


       5[0]
      /    \
   17[1]    13[2]
  /     \     /   \
 11[3]  1[4] 7[5]  3[6]
      
```

#### Heapify
to Heapify th binary tree, the value of the parent index must be higher than to two children. Therefore, the process starts at the bottom of the tree and works its way to the top. If the parent is smaller than one of the children values, it swaps the highest child with the parent. As heapifying moves through the tree, the higher values will progressively get to the top (low index values ) of the tree. 

When the heapifying process reaches the top, the top value swaps with the highest index number in the unsorted tree. Then the heapifying process begins again with the highest number removed from the tree.








