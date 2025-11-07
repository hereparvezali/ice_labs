use std::collections::{HashSet, VecDeque};
fn bfs(graph: &Vec<Vec<usize>>, start: usize) {
    let mut queue = VecDeque::new();
    let mut visited = HashSet::new();
    queue.push_back(start);
    visited.insert(start);
    while let Some(node) = queue.pop_front() {
        println!("Visiting {}", node);
        for &neighbor in &graph[node] {
            if !visited.contains(&neighbor) {
                visited.insert(neighbor);
                queue.push_back(neighbor);
            }
        }
    }
}
fn main() {
    let graph = vec![
        vec![1, 2],
        vec![0, 3, 4],
        vec![0, 5],
        vec![1],
        vec![1, 5],
        vec![2, 4],
    ];
    let start_node = 0;
    bfs(&graph, start_node);
}
