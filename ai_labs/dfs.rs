use std::collections::HashSet;
fn dfs(graph: &Vec<Vec<usize>>, node: usize, visited: &mut HashSet<usize>) {
    visited.insert(node);
    println!("Visiting: {}", node);

    for &neighbor in &graph[node] {
        if !visited.contains(&neighbor) {
            dfs(graph, neighbor, visited);
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
    let mut visited = HashSet::new();
    dfs(&graph, start_node, &mut visited);
}
