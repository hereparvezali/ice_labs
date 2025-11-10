#include <bits/stdc++.h>
using namespace std;

// Permutation utility
vector<int> permute(const vector<int> &input, const vector<int> &p) {
    vector<int> output(p.size());
    for (size_t i = 0; i < p.size(); ++i)
        output[i] = input[p[i] - 1];
    return output;
}

// Left shift
vector<int> leftShift(const vector<int> &key, int shifts) {
    vector<int> shifted = key;
    rotate(shifted.begin(), shifted.begin() + shifts, shifted.end());
    return shifted;
}

// XOR operation
vector<int> XOR(const vector<int> &a, const vector<int> &b) {
    vector<int> result(a.size());
    for (size_t i = 0; i < a.size(); ++i)
        result[i] = a[i] ^ b[i];
    return result;
}

// S-box lookup
vector<int> sboxLookup(const vector<int> &input, const vector<vector<int>> &sbox) {
    int row = input[0] * 2 + input[3];
    int col = input[1] * 2 + input[2];
    int val = sbox[row][col];
    return { (val / 2) % 2, val % 2 };
}

// Convert bit vector to string
string bitsToString(const vector<int> &bits) {
    string s;
    for (int b : bits) s += (b ? '1' : '0');
    return s;
}

// fK function
vector<int> fK(const vector<int> &bits, const vector<int> &subkey) {
    vector<int> L(bits.begin(), bits.begin() + 4);
    vector<int> R(bits.begin() + 4, bits.end());

    vector<int> EP = {4,1,2,3,2,3,4,1};
    vector<int> R_expanded = permute(R, EP);
    vector<int> xorRes = XOR(R_expanded, subkey);

    vector<int> left4(xorRes.begin(), xorRes.begin() + 4);
    vector<int> right4(xorRes.begin() + 4, xorRes.end());

    vector<vector<int>> S0 = {
        {1,0,3,2},
        {3,2,1,0},
        {0,2,1,3},
        {3,1,3,2}
    };
    vector<vector<int>> S1 = {
        {0,1,2,3},
        {2,0,1,3},
        {3,0,1,0},
        {2,1,0,3}
    };

    vector<int> s0_out = sboxLookup(left4, S0);
    vector<int> s1_out = sboxLookup(right4, S1);
    vector<int> s_output = {s0_out[0], s0_out[1], s1_out[0], s1_out[1]};

    vector<int> P4 = {2,4,3,1};
    vector<int> P4_out = permute(s_output, P4);

    vector<int> result = XOR(L, P4_out);
    result.insert(result.end(), R.begin(), R.end());
    return result;
}

// Key generation
pair<vector<int>, vector<int>> generateKeys(vector<int> key10) {
    vector<int> P10 = {3,5,2,7,4,10,1,9,8,6};
    vector<int> P8 = {6,3,7,4,8,5,10,9};

    key10 = permute(key10, P10);
    vector<int> left5(key10.begin(), key10.begin() + 5);
    vector<int> right5(key10.begin() + 5, key10.end());

    left5 = leftShift(left5, 1);
    right5 = leftShift(right5, 1);
    vector<int> K1 = permute(
        vector<int>(left5.begin(), left5.end()) + vector<int>(right5.begin(), right5.end()), P8);

    left5 = leftShift(left5, 2);
    right5 = leftShift(right5, 2);
    vector<int> K2 = permute(
        vector<int>(left5.begin(), left5.end()) + vector<int>(right5.begin(), right5.end()), P8);

    return {K1, K2};
}

// Concatenate two vectors
vector<int> concat(const vector<int> &a, const vector<int> &b) {
    vector<int> res = a;
    res.insert(res.end(), b.begin(), b.end());
    return res;
}

// Encryption/Decryption
vector<int> sdes(const vector<int> &input, const vector<int> &K1, const vector<int> &K2, bool decrypt = false) {
    vector<int> IP = {2,6,3,1,4,8,5,7};
    vector<int> IPinv = {4,1,3,5,7,2,8,6};

    vector<int> data = permute(input, IP);
    vector<int> firstKey = decrypt ? K2 : K1;
    vector<int> secondKey = decrypt ? K1 : K2;

    data = fK(data, firstKey);
    vector<int> L(data.begin(), data.begin() + 4);
    vector<int> R(data.begin() + 4, data.end());
    data = concat(R, L);
    data = fK(data, secondKey);
    data = permute(data, IPinv);
    return data;
}

int main() {
    // 10-bit key
    vector<int> key = {1,0,1,0,0,0,0,0,1,0};
    auto [K1, K2] = generateKeys(key);

    cout << "K1: " << bitsToString(K1) << endl;
    cout << "K2: " << bitsToString(K2) << endl;

    // 8-bit plaintext
    vector<int> plaintext = {1,0,1,0,1,0,1,0};
    vector<int> ciphertext = sdes(plaintext, K1, K2, false);
    vector<int> decrypted = sdes(ciphertext, K1, K2, true);

    cout << "Plaintext : " << bitsToString(plaintext) << endl;
    cout << "Ciphertext: " << bitsToString(ciphertext) << endl;
    cout << "Decrypted : " << bitsToString(decrypted) << endl;
}
