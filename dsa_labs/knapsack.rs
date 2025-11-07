// Problem-3: Write a programme to sort a linear array
// using merge sort algorithm

// Author: MD. Parvez ALi,
// Roll: 210623
// Session: 2021-22

// [Algorithm]......
// Initialization:
// Create a table dp with dimensions [number of items + 1] x [knapsack capacity + 1].
// Set n as the number of items, and W as the knapsack capacity.
// Dynamic Programming Table:
// dp[i][w] represents the maximum value with the first i items and knapsack capacity w.
// Fill in the Table:
// Iterate over each item i and knapsack capacity w.
// dp[i][w] is the maximum of not including the current item (dp[i-1][w]) or including it (values[i-1] + dp[i-1][w-weights[i-1]]).
// Result:
// The final result is in dp[n][W], representing the maximum value.
// Backtracking (Optional):
// If needed, backtrack to identify selected items.

// [Source Code in RUST]......
use std::cmp::max;
fn main() {
    let n: usize = 4;
    let mut c: isize = 20;
    let profit: Vec<isize> = vec![15, 25, 13, 23];
    let weight: Vec<isize> = vec![2, 6, 12, 9];
    println!("{}", rec(n, c, &weight, &profit));
}
fn rec(n: usize, c: isize, wt: &Vec<isize>, pro: &Vec<isize>) -> isize {
    let mut dp: Vec<Vec<isize>> = vec![vec![0; c as usize + 1]; n + 1];
    for i in 1..=n {
        for w in 1..=c as usize {
            if w as isize >= wt[i - 1] {
                dp[i][w]=max(dp[i-1][w],pro[i-1]+dp[i-1][w-wt[i-1] as usize]);
            } else {
                dp[i][w]=dp[i-1][w];
            }
        }
    }
    dp[n][c as usize]
}
