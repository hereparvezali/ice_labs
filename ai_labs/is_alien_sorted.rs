use std::collections::HashMap;

struct Solution;
impl Solution {
	pub fn new() -> Self {
		Self {}
	}
	pub fn is_alien_sorted(words: Vec<String>, order: String) -> bool {
		let mut ans = true;
		let mut map: HashMap<char, usize> = HashMap::new();
		for (i, c) in order.chars().into_iter().enumerate() {
			map.insert(i, c);
		}
		for word in words {
			let mut counting = 0_usize;
			for (i, c) in word.chars().enumerate() {
				let idx = *map.get(&c).unwrap();
				if counting>idx {
					return false;
				}
				counting = idx;
			}
		}
		true
	}
}


fn main() {
	let sol = Solution::new();
	
}