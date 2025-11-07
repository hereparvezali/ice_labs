// Problem-7 : Write a programe to sovle n quens problem

// Author: MD. Parvez ALi,
// Roll: 210623
// Session: 2021-22

// [Algorithm]......
// Initialization:
// Create an empty N×N chessboard.
// Start with the first row.
// Place Queens:
// For each row from 1 to N:
// For each column from 1 to N:
// Check if placing a queen in the current row and column is safe.
// If safe, place the queen on the chessboard and move to the next row.
// Safe Placement Check:
// Check if the current placement is safe by ensuring no queens threaten each other.
// Queens should not share the same row, column, or diagonal.
// Backtracking:
// If a safe placement is not possible in the current configuration:
// Backtrack to the previous row and try a different column for the queen placement.
// Repeat until a valid placement is found or all possibilities are exhausted.
// Result:
// Once all N queens are successfully placed on the chessboard, a solution is found.
// Backtracking Mechanism:
// The algorithm utilizes backtracking to explore different possibilities efficiently.
// If a conflict is encountered during placement, backtrack to the previous decision point and explore alternative choices.

// [Source Code in RUST]
use std::{
    collections::HashSet,
    io::{stdin, stdout, BufRead, Write},
};

fn main() {
    print!("Enter the size of the chess: ");
    stdout().flush().unwrap();
    let n = stdin()
        .lock()
        .lines()
        .next()
        .unwrap()
        .unwrap()
        .parse::<isize>()
        .unwrap();
    let (mut col, mut d1, mut d2) = (Vec::new(), HashSet::new(), HashSet::new());
    backtrack(0, n, &mut col, &mut d1, &mut d2);
}

fn backtrack(
    r: isize,
    n: isize,
    col: &mut Vec<isize>,
    d1: &mut HashSet<isize>,
    d2: &mut HashSet<isize>,
) {
    if r == n {
        let mut ans = vec![vec!['.'; n as usize]; n as usize];
        for i in 0..col.len() {
            ans[i][col[i] as usize] = '&';
        }
        printing(&ans);
        println!();
    }

    for c in 0..n {
        if !col.contains(&c) && !d1.contains(&(r - c)) && !d2.contains(&(r + c)) {
            col.push(c);
            d1.insert(r - c);
            d2.insert(r + c);
            backtrack(r + 1, n, col, d1, d2);
            col.pop();
            d1.remove(&(r - c));
            d2.remove(&(r + c));
        }
    }
}
fn printing(vec: &Vec<Vec<char>>) {
    for v in vec {
        for &c in v {
            print!("{c} ");
        }
        println!();
    }
}
