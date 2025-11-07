use std::{
    collections::HashSet,
    io::{stdin, Read},
};

fn main() {
    let mut table: Vec<Vec<isize>> = vec![vec![-1; 3]; 3];
    println!("{:?}", table);
    run(&mut table);
}
fn run(table: &mut Vec<Vec<isize>>) {
    let mut set: HashSet<(isize, isize)> = HashSet::new();
    let mut count = 0;

    while count < 5 {
        let mut strinp = String::new();
        stdin().read_line(&mut input).unwrap();
        let i: isize = strinp.parse().unwrap();
        strinp.clear();
        stdin().read(&mut strinp).unwrap();
        let j: isize = strinp.parse().unwrap();
        if let Some(_) = set.get(&(i, j))
            && i < 0
            && i > 2
            && j < 0
            && j > 2
            && table[i as usize][j as usize] != -1
        {
            println!("Invalid input");
            continue;
        }
        set.insert((i, j));
        table[i][j] = 0;

        if count > 2 {
            if check(table, i as usize, j as usize, 0) == true {
				println!("You won!!");
				return;
			}
        }

		while count<4 {
			let r = 
		}

        count += 1;
    }
}
fn check(table: Vec<Vec<isize>>, i: usize, j: usize, sign: isize) -> bool {
    let mut count = 0;
    for jj in 0..3 {
        if table[i][jj] == sign {
            count += 1;
        }
    }
    if count == 3 {
        return true;
    }
    count = 0;
    for ii in 0..3 {
        if table[ii][j] == sign {
            count += 1;
        }
    }
    if count == 3 {
        return true;
    }
    count = 0;
    for c in 0..3 {
        if table[c][c] == sign {
            count += 1;
        }
    }
    if count == 3 {
        return true;
    }
    count = 0;

    for c in 0..3 {
        if table[c][2 - c] == sign {
            count += 1;
        }
    }
    if count == 3 {
        return true;
    }
    false
}
