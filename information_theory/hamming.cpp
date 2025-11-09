#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

// Function to generate Hamming code from data bits
vector<int> gen_hamming(vector<int> &data) {
    int m = (int)data.size();
    int r = 0;
    // Find number of parity bits needed
    while (pow(2, r) < m + r + 1) {
        r += 1;
    }

    vector<int> hamming_code(m + r, 0);

    // Insert data bits into positions that are NOT powers of 2
    int j = 0;
    for (int i = 1; i <= (int)hamming_code.size(); i++) {
        if ((i & (i - 1)) != 0) { // not power of 2
            hamming_code[i - 1] = data[j++];
        }
    }

    // Calculate parity bits
    for (int i = 0; i < r; i++) {
        int parity = 0;
        int parity_idx = pow(2, i);
        for (int j = 1; j <= (int)hamming_code.size(); j++) {
            if ((j & parity_idx) != 0) {
                parity ^= hamming_code[j - 1];
            }
        }
        hamming_code[parity_idx - 1] = parity;
    }

    return hamming_code;
}

// Function to detect and correct a single-bit error
void error_fix(vector<int> &hamming_code) {
    int n = hamming_code.size();
    int r = 0;
    while (pow(2, r) < n + 1) {
        r += 1;
    }

    int syndrome = 0;

    // Calculate syndrome bits
    for (int i = 0; i < r; i++) {
        int parity_idx = pow(2, i);
        int parity = 0;
        for (int j = 1; j <= n; j++) {
            if ((j & parity_idx) != 0) {
                parity ^= hamming_code[j - 1];
            }
        }
        if (parity != 0) {
            syndrome += parity_idx;
        }
    }

    // Correct error if syndrome != 0
    if (syndrome != 0) {
        cout << "Error detected at position: " << syndrome << endl;
        hamming_code[syndrome - 1] ^= 1; // flip the bit
    } else {
        cout << "No error detected." << endl;
    }
}

int main() {
    vector<int> data{1, 0, 1, 1};

    // Generate Hamming code
    auto hamming_code = gen_hamming(data);
    cout << "Hamming code to transmit: ";
    for (auto bit : hamming_code) cout << bit << " ";
    cout << endl;

    // Introduce a single-bit error
    vector<int> received = hamming_code;
    received[3] ^= 1; // flip one bit to simulate an error

    cout << "Received code (with error): ";
    for (auto bit : received) cout << bit << " ";
    cout << endl;

    // Detect and correct error
    error_fix(received);

    cout << "Corrected code: ";
    for (auto bit : received) cout << bit << " ";
    cout << endl;

    return 0;
}
