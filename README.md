# Missing Number

You are presented with two arrays, all containing positive integers. One of the arrays will have one extra number, see below:

[1,2,3] and [1,2,3,4] should return 4

[4,66,7] and [66,77,7,4] should return 77

## Getting Started
Some prerequisites are required to have achieved desired output.

    This code is written in Python3 and may have unexpected functionality when run with Python 2.x


Install pytest:
```
$ pip install pytest

```
Alternatively, Install nose
```
$ pip install nose

```

### Using the Code

clone the code from git using this limk:
```
git clone https://github.com/Bryoo/MissingNumber
```
Ensure you're in the main directory 'MissingNumber' and then run the code
```
python3 missingnumber.py

## Executing the tests included

if you've got pytest
```
$ py.test test_missing_number.py
```
If you've got nosetests
```
$ nosetests test_missing_number.py
```
Alternatively, if you do not have either nosetests or pytest installed, use:

```
$ python3 test_http_client.py
```

## How it works

The Algorithm uses a hashtable so as to boost it's performance.

Each element from the first array is stored in a hashtable plus its frequency

Then, it loops through all the elements in the second array and hashes each key to the frequency recorded in hashtable, a non existent record would have a frequecy of 0 hence is the missing element.

Complexity O(n)



