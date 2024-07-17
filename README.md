**Overview**

This Python script performs several operations to find and analyze prime numbers within a specified range. 
The script first identifies all prime numbers between 1 and 100, then computes the sum of the digits of each prime number, and finally determines which of these sums are also prime numbers. 
It also eliminates any duplicate sums that are prime numbers.

**Features**

1.Finding Prime Numbers:

The script iterates through numbers from a to b (inclusive).
It checks if each number is prime.
If a number is prime, it is added to a list of prime numbers **(my_list)**.

2.Sum of Digits:

For each prime number found, the script calculates the sum of its digits.
These sums are stored in another list **(my_result)**.

3.Prime Sum Check:

The script checks if the sums of digits are prime numbers.
It stores these prime sums in a list **(prime**).

4.Removing Duplicates:

The script removes duplicate prime sums by converting the list to a set **(setprime)**.

**Usage**

To run this script, simply execute it in a Python environment. The script will output:

1.The number of prime numbers found between 1 and 100.

2.The list of prime numbers.

3.The sums of the digits of these prime numbers.

4.The prime numbers whose digit sums are also prime.

5.The set of prime numbers with digit sums that are prime, with duplicates removed.

