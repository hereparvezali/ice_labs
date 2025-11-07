// Problem-3: Write a programme to sort a linear array
// using merge sort algorithm
// Author: MD. Parvez ALi,
// Roll: 210623
// Session: 2020-21

// [Algorithm]......
// Divide:
// If the array has one element or is empty, it is already considered sorted, so no changes are needed.
// Otherwise, divide the array into two halves: a left half and a right half.
// Conquer:
// Recursively apply the merge sort algorithm to each of the two halves.
// Continue this process until each subarray has at most one element.
// Merge:
// Combine the sorted left and right halves into a single sorted array.
// Compare the elements from the left and right halves, placing them in sorted order.
// Continue this process until all elements are merged.
// Base Case:
// The base case is when a subarray has at most one element, as a single element is considered sorted.
// Result:
// The final result is a completely sorted array.

// [Source Code in RUST]......
use std::{
    io::{stdin, stdout, BufRead, Write},
    ops::Range,
};
fn main() {
    let mut lines = stdin().lock().lines().map(|f| f.unwrap());
    print!("Enter the size of the array: ");
    stdout().flush().unwrap();
    let n: usize = lines.next().unwrap().parse().unwrap();
    print!("Enter the array in one line: ");
    stdout().flush().unwrap();
    let mut v: Vec<isize> = lines
        .next()
        .unwrap()
        .trim()
        .split_whitespace()
        .map(|f| f.parse().unwrap())
        .collect();
    merge_sort(&mut v, 0..n);
    println!("The sorted array is: {:?}", v);
}
fn merge_sort(v: &mut Vec<isize>, range: Range<usize>) {
    if range.len() <= 1 {
        return;
    }
    let m = (range.end + range.start) / 2;
    merge_sort(v, range.start..m);
    merge_sort(v, m..range.end);
    merge(v, range.start, m, range.end);
}
fn merge(v: &mut Vec<isize>, l: usize, m: usize, r: usize) {
    let (mut i, mut j) = (l, m);
    let mut temp: Vec<isize> = Vec::with_capacity(r - l);
    while i < m && j < r {
        if v[i] < v[j] {
            temp.push(v[i]);
            i += 1;
        } else {
            temp.push(v[j]);
            j += 1;
        }
    }
    while i < m {
        temp.push(v[i]);
        i += 1;
    }
    while j < r {
        temp.push(v[j]);
        j += 1;
    }
    for t in l..r {
        v[t] = temp[t - l];
    }
}
