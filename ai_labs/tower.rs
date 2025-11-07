use std::io::{stdin, stdout, BufRead, Write};
fn main() {
	print!("Enter number of disks: ");
	stdout().flush().unwrap();
	let n = stdin().lock().lines().next().unwrap().unwrap().parse::<isize>().unwrap();
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