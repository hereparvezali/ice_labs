#include <iostream>
#include <vector>
using namespace std;

// mod function ensures positive results
inline int mod(int x, int m) {
    x %= m;
    if (x < 0) x += m;
    return x;
}

// Extended Euclidean algorithm for modular inverse
inline int mod_inverse26(int a) {
    a = mod(a, 26);
    for (int x = 1; x < 26; x++)
        if ((a * x) % 26 == 1)
            return x;
    return -1; // not invertible
}

// Gauss-Jordan elimination for inverse mod 26
inline vector<vector<int>> inverse(vector<vector<int>> mat) {
    int n = mat.size();
    vector<vector<int>> ans(n, vector<int>(n, 0));
    for (int i = 0; i < n; i++) ans[i][i] = 1; // identity

    for (int i = 0; i < n; i++) {
        int pivot = mod(mat[i][i], 26);
        int inv_pivot = mod_inverse26(pivot);
        if (inv_pivot == -1) {
            cerr << "❌ Matrix not invertible mod 26\n";
            exit(1);
        }

        // Normalize pivot row
        for (int j = 0; j < n; j++) {
            mat[i][j] = mod(mat[i][j] * inv_pivot, 26);
            ans[i][j] = mod(ans[i][j] * inv_pivot, 26);
        }

        // Eliminate other rows
        for (int k = 0; k < n; k++) {
            if (k == i) continue;
            int factor = mat[k][i];
            for (int j = 0; j < n; j++) {
                mat[k][j] = mod(mat[k][j] - factor * mat[i][j], 26);
                ans[k][j] = mod(ans[k][j] - factor * ans[i][j], 26);
            }
        }
    }

    return ans;
}

// Print matrix
inline void printvec(vector<vector<int>>& vec) {
    for (auto &row : vec) {
        for (auto x : row) cout << x << " ";
        cout << "\n";
    }
}

// // Example usage
// int main() {
//     vector<vector<int>> key = {
//         {2, 3, 4},
//         {3, 7, 5},
//         {6, 4, 9}
//     };

//     auto inv = inverse(key);
//     cout << "Inverse mod 26:\n";
//     printvec(inv);
// }
