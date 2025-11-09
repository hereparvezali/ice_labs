#include <iostream>
#include <vector>
using namespace std;
void printvec(vector<vector<double>> &vec) {
    for (auto x : vec) {
        for (auto y : x) {
            cout << y << ' ';
        }
        cout << endl;
    }
}
void add_unit(vector<vector<double>> &mat) {
    for (int i = 0; i < mat.size(); i++) {
        for (int j = 0; j < mat.size(); j++) {
            if (i == j) {
                mat[i].push_back(1.0);
            } else {
                mat[i].push_back(0.0);
            }
        }
    }
}
vector<vector<double>> inverse(vector<vector<double>> mat) {
    add_unit(mat);
    for (int i = 0; i < mat.size(); i++) {
        double temp = mat[i][i];
        for (int j = 0; j < mat[i].size(); j++) {
            mat[i][j] /= temp;
        }
        for (int k = 0; k < mat.size(); k++) {
            if (k == i)
                continue;
            temp = mat[k][i];
            for (int j = 0; j < mat[i].size(); j++) {
                mat[k][j] -= mat[i][j] * temp;
            }
        }
    }
    vector<vector<double>> ans(mat.size(), vector<double>(mat.size()));
    for (int i = 0; i < mat.size(); i++) {
        for (int j = 0; j < mat.size(); j++) {
            ans[i][j] = mat[i][j + mat.size()];
        }
    }
    return ans;
}

int main() {
    vector<vector<double>> mat = {{2, 3, 4}, {3, 7, 5}, {6, 4, 9}};
    auto inverted = inverse(mat);
    printvec(inverted);
}
