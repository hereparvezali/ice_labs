// Problem-8 : Consider a set S=[5,10,12,13,15,18] and d=30.
// Write a program to solve the sum of subset problem
// Author: MD. Parvez ALi,
// Roll: 210623
// Session: 2020-21

// [Algorithm]......
// Function check_subsets:
// Recursively explores all subsets of the set.
// If the sum of a subset equals the target sum, adds a clone to the result vector.
// Base Case:
// If at the end of the set, check for the sum and return.
// Recursive Calls:
// Include and exclude the current element in the subset and make recursive calls.
// Usage:
// Call check_subsets with appropriate parameters to find subsets with the desired sum.

// [Source Code in RUST].....
fn main() {
    let set: Vec<isize> = vec![5, 10, 12, 13, 15, 18];
    let d: isize = 30;
    let mut subset: Vec<isize> = vec![];
    let mut subsets: Vec<Vec<isize>> = vec![];
    check_subsets(0, &d, &set, &mut subset, &mut subsets);
    println!("{:?}", subsets);
}
fn check_subsets(i: usize,d: &isize,set: &Vec<isize>,subset: &mut Vec<isize>,subsets: &mut Vec<Vec<isize>>) {
    if i == set.len() {
        if subset.iter().sum::<isize>() == *d {
            subsets.push(subset.clone());
        }
        return;
    }
    subset.push(set[i]);
    check_subsets(i + 1, d, set, subset, subsets);
    subset.pop();
    check_subsets(i + 1, d, set, subset, subsets);
}
