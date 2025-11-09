#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

// Structure for each symbol
struct Symbol {
    char name;
    double probability;
    int length;
};

// Function to compute entropy
double entropy(const vector<Symbol> &symbols) {
    double H = 0.0;
    for (auto &s : symbols) {
        H += s.probability * log2(1.0 / s.probability);
    }
    return H;
}

// Function to compute average codeword length
double avg_code_length(const vector<Symbol> &symbols) {
    double L = 0.0;
    for (auto &s : symbols) {
        L += s.probability * s.length;
    }
    return L;
}

int main() {
    // Example: Huffman code table
    vector<Symbol> symbols = {
        {'A', 0.4, 1},
        {'B', 0.3, 2},
        {'C', 0.2, 3},
        {'D', 0.1, 3}
    };

    double H = entropy(symbols);
    double L = avg_code_length(symbols);

    cout << "Entropy H(X) = " << H << endl;
    cout << "Average code length L = " << L << endl;

    cout << "\nChecking Shannon's bound..." << endl;
    if (H <= L && L < H + 1) {
        cout << "✅ Huffman code is optimal (satisfies entropy bound)." << endl;
    } else {
        cout << "❌ Huffman code is NOT optimal." << endl;
    }

    return 0;
}
