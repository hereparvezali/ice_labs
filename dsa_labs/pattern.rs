// Problem-3: Write a programme to sort a linear array
// using merge sort algorithm
// Author: MD. Parvez ALi,
// Roll: 210623
// Session: 2021-22

// [Algorithm].....
// Function find:
// Input: str (text string), pattern (pattern string).
// Output: Option containing the index where the pattern is found in the text or None if not found.
// Iterate and Compare:
// For each starting index i from 0 to str.len() - pattern.len() (inclusive):
// Check if the characters in str from i to i + pattern.len() match the characters in pattern.
// If a match is found, return Some(i + 1) (indexing is 1-based).
// Pattern Not Found:
// If no match is found after iterating over all starting positions, return None.

// [Source Code in RUST].....
use std::io::{stdin, stdout, BufRead, Write};
fn main() {
	let mut lines = stdin().lock().lines().map(|f| f.unwrap());
    print!("Enter the text: ");
    stdout().flush().unwrap();
    let str = lines.next().unwrap();
    print!("Enter the pattern to find: ");
    stdout().flush().unwrap();
    let pattern = lines.next().unwrap();
    match find(str, pattern) {
        Some(idx) => println!("The pattern found in {} position", idx),
        None => println!("The pattern did not match!"),
    }
}
fn find(str: String, pattern: String) -> Option<usize> {
    for i in 0..=str.len() - pattern.len() {
        for j in 0..pattern.len() {
            if j + 1 == pattern.len() && str[i + j..i + j + 1] == pattern[j..j + 1] {
                return Some(i + 1);
            }
            if str[i + j..i + j + 1] != pattern[j..j + 1] {
                break;
            }
        }
    }
    None
}
