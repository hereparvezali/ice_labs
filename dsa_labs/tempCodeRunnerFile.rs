// Problem-2: Write a programe to find an element
// using a linear search algorithm

// Author: MD. Parvez ALi,
// Roll: 210623
// Session: 2021-22

// [Solution] starts here.
// using the Write buffer of io module from standard library
use std::io::Write;

fn main() {
    // creation of a new string literal to take input buffer
    let mut input = String::new();
    print!("Enter the array in one line: ");
    // flushing the output buffer to the user before input
    std::io::stdout().flush().unwrap();
    // taking input a whole line to the "input" literal
    std::io::stdin().read_line(&mut input).unwrap();
    // creating a vector
    let array: Vec<isize> = input
        // Spliting the string by the whitespaces
        .split_whitespace()
        // parsing every element to isize with map
        .map(|f| f.parse().unwrap())
        // collecting the values of the iterator to the Vector
        .collect();
    loop {
        // starting a loop
        // clearing the "input" before taking more user input
        input.clear();
        print!("Enter what you want to queary to the vector: ");
        // taking input from the user
        std::io::stdin().read_line(&mut input).unwrap();
        if input.trim() == "done" {
            // when the user will send the "done"
			// then the loop will be finished
            break;
        }
        // creting the query variable as ele
        let ele: isize = input.trim().parse().unwrap();
        match linear_search(&array, ele) {
            // matching the input if it is valid
            // if the element found in the vec then the desired index
            Some(index) => println!("The value in the index {index}"),
            // otherwise handling the error here
            None => println!("The value does not available"),
        }
    }
}
// function that performs the linear search
// returns the index or None if unavailable
fn linear_search(array: &Vec<isize>, ele: isize) -> Option<usize> {
    // starting linear search with for loop throught the vector
    for i in 0..array.len() {
        // if the element is equal to the queary then return the index
        // with optional value
        if array[i] == ele {
            return Some(i);
        }
    }
    // Otherwise return None that if not available
    None
}
