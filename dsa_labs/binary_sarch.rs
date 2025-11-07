// Problem-4: Write a programme to find an element
// using the binary search algorithm

// Author: MD. Parvez ALi,
// Roll: 210623
// Session: 2021-22

// [Algorithm]......
// Initialize: Set low to the start of the array (usually 0) and high to the end of the array (length - 1).
// Search Iteration:
// While low is less than or equal to high, continue the search.
// Calculate the middle index: mid = (low + high) / 2.
// Comparison:
// If the element at index mid is equal to the target:
// Return mid (target found).
// If the element at index mid is less than the target:
// Update low to mid + 1 (search in the right half).
// If the element at index mid is greater than the target:
// Update high to mid - 1 (search in the left half).
// Repeat:
// Repeat steps 2-3 until low exceeds high.
// Result:
// If the target is found during the search, return the index where it was found.
// If the target is not found, return -1 to indicate its absence in the array.

// [Source Code in RUST]......
use std::io::{stdin, stdout, BufRead, Write};
fn main() {
    let mut lines = stdin().lock().lines().map(|f| f.unwrap());
    print!("Enter the size of the array: ");
    stdout().flush().unwrap();
    let n = lines.next().unwrap().parse::<usize>().unwrap();
    print!("Enter the array in sorted order: ");
    stdout().flush().unwrap();
    let array: Vec<isize> = lines
        .next()
        .unwrap()
        .split_whitespace()
        .map(|f| f.parse().unwrap())
        .collect();
    loop {
        print!("Enter what you want to query to the vector: ");
        stdout().flush().unwrap();
		let input = lines.next().unwrap();
        if input.trim() == "done" {
            break;
        }
        let ele: isize = input.trim().parse().unwrap();
        match binary_sarch(&array, ele) {
            Some(index) => println!("The value in the index {index}"),
            None => println!("The value does not available"),
        }
    }
}

fn binary_sarch(array: &Vec<isize>, ele: isize) -> Option<usize> {
    let (mut i, mut j) = (0 as isize, (array.len() - 1) as isize);
    while i <= j {
        let m: usize = ((j + i) / 2) as usize;
        if array[m] == ele {
            return Some(m);
        } else if array[m] > ele {
            j = m as isize - 1;
        } else {
            i = m as isize + 1;
        }
    }
    None
}
