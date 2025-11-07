fn main() {
    let graph = vec![
        vec![0, 10, 15, 20],
        vec![5, 0, 25, 10],
        vec![15, 30, 0, 5],
        vec![15, 10, 20, 0],
    ];
    let mut trace: Vec<usize> = Vec::new();
    let mut path: Vec<usize> = Vec::new();
    let mut ans = i32::MAX;
    recursion(0, &graph, &mut trace, &mut path, 0, &mut ans);
    println!("Shortest distance: {}", ans);
	println!("Shortest path: {:?}", path);
}
fn recursion(
    i: usize, graph: &Vec<Vec<i32>>, trace: &mut Vec<usize>, path: &mut Vec<usize>, cost: i32, ans: &mut i32,
) {
    if trace.len() == graph[i].len() && i == 0 {
        if *ans > cost {
            *ans = cost;
            *path = trace.clone();
        }
    }
    if trace.contains(&i) {
        return;
    }
    trace.push(i);
    for j in 0..graph[i].len() {
        recursion(j, graph, trace, path, cost + graph[i][j], ans);
    }
    trace.pop();
}
