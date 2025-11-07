// Problem-4: Write a programme to sort a linear array
// using the bubble sort algorithm

// Author: MD. Parvez ALi,
// Roll: 210623
// Session: 2021-22

// [Algorithm]......
// Initialize: Start with the first element (index 0) as the current element.
// Iterate through the array:
// Compare the current element with the next element.
// If the current element is greater than the next element, swap them.
// Continue Iterating:
// Move to the next pair of elements (next element becomes the current element).
// Repeat the comparison and swap process until reaching the end of the array.
// One Pass Complete:
// After one pass through the array, the largest unsorted element is at the end.
// Repeat:
// Repeat steps 2-4 for the remaining unsorted elements, excluding the ones already sorted.
// Completion:
// Continue this process until the entire array is sorted.


// [Source Code in RUST].....
use std::io::{stdin, stdout, BufRead, Write};
fn main() {
    let mut lines = stdin().lock().lines().map(|f| f.unwrap());
	print!("Enter the size of the array: ");
	stdout().flush().unwrap();
    print!("Enter the array in one line to sort: ");
	stdout().flush().unwrap();
    let mut arr: Vec<isize> = lines
        .next()
        .unwrap()
        .split_whitespace()
        .map(|f| f.parse().unwrap())
        .collect();
    bubble_sort(&mut arr);
    println!("{:?}", arr);
}
fn bubble_sort(arr: &mut Vec<isize>) {
    for i in 0..arr.len() - 1 {
        for j in 0..arr.len() - i - 1 {
            if arr[j] > arr[j + 1] {
                arr.swap(j, j + 1);
            }
        }
    }
}
