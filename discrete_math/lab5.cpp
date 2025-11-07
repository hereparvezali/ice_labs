#include <iostream>
#include <vector>
#include <list> // Use list for adjacency list representation
#include <algorithm>
using namespace std;

vector<int> welshPowell(vector<list<int>>& adj) {
    int V = adj.size();
    vector<int> color(V, -1);
    vector<pair<int, int>> vertices;
    for (int i = 0; i < V; ++i) {
        vertices.push_back({-adj[i].size(), i});
    }
    sort(vertices.begin(), vertices.end());
    for (int i = 0; i < V; ++i) {
        int v = vertices[i].second;
        if (color[v] == -1) {
            bool colorAvailable[V];
            for (int j = 0; j < V; ++j) {
                colorAvailable[j] = true;
            }
            for (int u : adj[v]) {
                if (color[u] != -1) {
                    colorAvailable[color[u]] = false;
                }
            }
            for (int col = 0; col < V; ++col) {
                if (colorAvailable[col]) {
                    color[v] = col;
                    break;
                }
            }
        }
    }
    return color;
}

int main() {
    vector<list<int>> adjList = {
        {1, 2},
        {0, 2, 3},
        {0, 1, 3},
        {1, 2, 4},
        {3, 5, 6},
        {4, 6},
        {4, 5}
    };

    vector<int> colors = welshPowell(adjList);

    cout << "Vertex\tColor" << endl;
    for (int i = 0; i < colors.size(); ++i) {
        cout << i << "\t" << colors[i] << endl;
    }

    return 0;
}
