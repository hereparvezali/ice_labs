// Problem-2: Write a programme to find an element
// using a linear search algorithm

// Author: MD. Parvez ALi,
// Roll: 210623
// Session: 2021-22

// [Algorithm].....
// Initialization:
// Start at the beginning of the array.
// Iterate through the array:
// For each element in the array:
// Check if the current element is equal to the target value.
// Comparison:
// If the current element is equal to the target value:
// Return the index of the current element.
// If the end of the array is reached and the target is not found:
// Return None to indicate that the target is not present in the array.
// Result:
// If the target is found during the search, return the index where it was found.
// If the target is not found, return None.

// [Source Code in RUST]
use std::io::{stdin, stdout, BufRead, Write};
fn main() {
    let mut lines = stdin().lock().lines().map(|f| f.unwrap());
    print!("Enter the size of the array: ");
    stdout().flush().unwrap();
    let n: usize = lines.next().unwrap().parse().unwrap();
    print!("Enter the array: ");
    stdout().flush().unwrap();
    let array: Vec<isize> = lines
        .next()
        .unwrap()
        .split_whitespace()
        .map(|f| f.parse().unwrap())
        .collect();
    loop {
        print!("Enter what you want to queary to the vector: ");
        std::io::stdout().flush().unwrap();
        let input = lines.next().unwrap();
        if input.trim() == "done" {
            break;
        }
        let ele: isize = input.trim().parse().unwrap();
        match linear_search(&array, ele) {
            Some(index) => println!("The value in the index {index}"),
            None => println!("The value does not available"),
        }
    }
}
fn linear_search(array: &Vec<isize>, ele: isize) -> Option<usize> {
    for i in 0..array.len() {
        if array[i] == ele {
            return Some(i);
        }
    }
    None
}
