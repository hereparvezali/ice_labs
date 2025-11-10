#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

// Function to create the 5x5 matrix
vector<vector<char>> createMatrix(string key) {
    string alpha = "ABCDEFGHIKLMNOPQRSTUVWXYZ";
    string seen = "";
    for (char c : key + alpha) {
        if (seen.find(c) == string::npos) {
            seen += c;
        }
    }

    vector<vector<char>> matrix(5, vector<char>(5));
    int index = 0;
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            matrix[i][j] = seen[index++];
        }
    }
    return matrix;
}

// Function to find the position of a character in the matrix
pair<int, int> findPos(vector<vector<char>> matrix, char ch) {
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            if (matrix[i][j] == ch) {
                return {i, j};
            }
        }
    }
    return {-1, -1}; // Return invalid position if character not found
}

// Function to prepare the message for encryption
string prepare(string msg) {
    msg.erase(remove(msg.begin(), msg.end(), ' '), msg.end());
    transform(msg.begin(), msg.end(), msg.begin(), ::toupper);
    replace(msg.begin(), msg.end(), 'J', 'I');

    string res = "";
    int i = 0;
    while (i < msg.length()) {
        char a = msg[i];
        char b = (i + 1 < msg.length()) ? msg[i + 1] : 'X';
        if (a == b) {
            res += a;
            res += 'X';
            i += 1;
        } else {
            res += a;
            res += b;
            i += 2;
        }
    }
    if (res.length() % 2 != 0) {
        res += 'X';
    }
    return res;
}

// Function to encrypt the message
string playfairEncrypt(string msg, string key) {
    vector<vector<char>> matrix = createMatrix(key);
    string p = prepare(msg);
    string out = "";

    for (int i = 0; i < p.length(); i += 2) {
        char a = p[i];
        char b = p[i + 1];
        auto [r1, c1] = findPos(matrix, a);
        auto [r2, c2] = findPos(matrix, b);

        if (r1 == r2) {
            out += matrix[r1][(c1 + 1) % 5];
            out += matrix[r2][(c2 + 1) % 5];
        } else if (c1 == c2) {
            out += matrix[(r1 + 1) % 5][c1];
            out += matrix[(r2 + 1) % 5][c2];
        } else {
            out += matrix[r1][c2];
            out += matrix[r2][c1];
        }
    }
    return out;
}

// Function to decrypt the message
string playfairDecrypt(string ct, string key) {
    vector<vector<char>> matrix = createMatrix(key);
    string out = "";

    for (int i = 0; i < ct.length(); i += 2) {
        char a = ct[i];
        char b = ct[i + 1];
        auto [r1, c1] = findPos(matrix, a);
        auto [r2, c2] = findPos(matrix, b);

        if (r1 == r2) {
            out += matrix[r1][(c1 - 1 + 5) % 5];
            out += matrix[r2][(c2 - 1 + 5) % 5];
        } else if (c1 == c2) {
            out += matrix[(r1 - 1 + 5) % 5][c1];
            out += matrix[(r2 - 1 + 5) % 5][c2];
        } else {
            out += matrix[r1][c2];
            out += matrix[r2][c1];
        }
    }
    return out;
}

int main() {
    string msg = "HELLO WORLD";
    string key = "KEYWORD";

    string enc = playfairEncrypt(msg, key);
    string dec = playfairDecrypt(enc, key);

    cout << "Original: " << msg << endl;
    cout << "Encrypted: " << enc << endl;
    cout << "Decrypted: " << dec << endl;

    return 0;
}
