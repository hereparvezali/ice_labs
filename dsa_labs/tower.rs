// Problem-10 : Write a programe to sovle the tower of hanoi problem for the N disk

// Author: MD. Parvez ALi,
// Roll: 210623
// Session: 2021-22

// [Algorithm].....
// Function tower_of_hanoi:
// Inputs: n, source, target, auxiliary.
// Output: Moves required.
// Base Case:
// If n is 1, move disk from source to target.
// Recursive Calls:
// Move n-1 disks from source to auxiliary, using target as auxiliary.
// Move remaining disk from source to target.
// Move n-1 disks from auxiliary to target, using source as auxiliary.
// Usage:
// Call tower_of_hanoi with parameters.

// [Source Code in RUST]
use std::io::{stdin, stdout, BufRead, Write};
fn main() {
	println!("Enter number of disks: ");
	stdout().flush().unwrap();
	let mut n = stdin().lock().lines().next().unwrap().unwrap().parse::<isize>().unwrap();
	tofh(n, &'A', &'B', &'C');
}
fn tofh(n: isize, source: &char, helper: &char, dest: &char) {
	if n == 0 {
		return;
	}
	tofh(n - 1, source, dest, helper);
	println!("Disk {} moved from {} to {}", n, source, dest);
	tofh(n - 1, helper, source, dest);
}
