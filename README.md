<h1 align="center"> Algorithms </h1>
This file contains basic information about each algorithm I learn.

<h2 align='center'> Searching and Sorting Algorithms: </h2>  

|Name of Algorithm    |Time Complexity                                                             |Space Complexity |Comment|Implementation|
|:-------------------:|:--------------------------------------------------------------------------:|:---------------:|:------|:------------:|
|linear search        |O(n)                                                                        |O(1)             |Rarely used.<br>Used for sorted arrays.|linear.py|
|binary search        |O(log(n)                                                                    |O(1)             |Used for sorted arrays.|binary.py|
|jump search          |O(n^0.5)                                                                    |O(1)             |Combines binary search and linear search.<br>Used for sorted arrays.<br>Optimal jump size is n^0.5<br>Time complexity is between linear search and binary search.|jump.py|
|interpolation search |average case: O(log2(log2 n))<br>worst case: O(n)                           |O(1)             |Used for sorted arrays with uniform distribution.<br>Similar to binary search, different method of calculating position.|interpolation.py|
|exponential search   |O(log(n)                                                                    |O(1)             |Used for sorted arrays.<br>Divides array by exponential factor. Than uses binary search on specific slice of the original array.|exponential.py|
|ternary search       |O(log3 n)                                                                   |O(1)             |Used for sorted arrays.<br>Similar to binary search, the difference is that we divide array (or slice) into 3 parts instead of 2 parts.|ternary.py|
|selection sort       |O(n)                                                                        |O(1)             | |selection.py|
|bubble sort          |worst / average case: O(n^2)<br>best case: O(n)                             |O(1)             | |bubble.py|
|insertion sort       |O(n*2)                                                                      |O(n)             | |insertion.py|
|merge sort           |O(n*log(n))                                                                 |O(n)             | |merge.py|
|quick sort           |worst case: O(n^2)<br>average case: O(n*log(n)<br>best case: O(n)           |O(log(n))        | |quick.py|
|heap sort            |On*log(n))                                                                  |O(1)             | |heap.py|
|count sort           |O(n + k): 0>k>=n                                                            |O(n+k)           |Best for small range of values (k).|count.py|
|radix sort           |O(d*(n+b))<br>d- number of digits<br>n- number of elements<br>b- system base|O(b+n)           | |radix.py|
|bucket sort          |average case: O(n+k)<br>worst case: O(n^2)                                  |O(n+k)           |Best for uniformly distributed values.<br>Breaks list into sublists and uses another algorithm to sot them.|bucket.py|
|shell sort           |O(n^2)                                                                      |O(1)             | |shell.py|
|comb sort            |O(n^2/2^p)<br>p- number of increments<br>n- number of elements              |O(1)             | |comb.py|
|pigeonhole sort      |O(R+n)<br>R- range of values<br>n- number of elements                       |O(n)             | |pigeonhole.py|
|cycle sort           |O(n^2)                                                                      |O(1)             | |cycle.py|

<h2 align='center'> Time complexity: </h2>

### Full view: 
![full view](https://raw.githubusercontent.com/FilipM13/algorithms/main/time%20complexity.png "Full view")
### Detail:
![detail](https://raw.githubusercontent.com/FilipM13/algorithms/main/time%20complexity%20close%20up.png "detail")
