#include <algorithm> // for algorithms like remove and transform
#include <iomanip>   // for setw used in matrix printing (commented out)
#include <iostream>  // for input-output operations
#include <string>    // for using string type
#include <vector>    // for using vectors

using namespace std;

// Function to create the 5x5 Playfair cipher matrix using the key
vector<vector<char>> createMatrix(string key) {
    string alpha = "ABCDEFGHIKLMNOPQRSTUVWXYZ"; // Alphabet without 'J'
    string seen = ""; // To keep track of characters already added

    // Add characters from key + remaining alphabet to 'seen', ignoring
    // duplicates
    for (char c : key + alpha) {
        if (seen.find(c) == string::npos) { // If character not already included
            seen += c;                      // Add it to the seen string
        }
    }

    vector<vector<char>> matrix(5, vector<char>(5)); // Create 5x5 matrix
    int index = 0;

    // Fill the matrix row-wise with characters from 'seen' string
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            matrix[i][j] = seen[index++];
        }
    }

    // Optional: print matrix (currently commented out)
    // for(auto x: matrix){
    //     for(auto y: x){
    //         cout << setw(5) << y << ' ';  // Print each char with width 5
    //     }
    //     cout << endl;
    // }

    return matrix; // Return the completed matrix
}

// Function to find the row and column index of a character in the matrix
pair<int, int> findPos(vector<vector<char>> matrix, char ch) {
    // Loop through the matrix rows
    for (int i = 0; i < 5; i++) {
        // Loop through columns
        for (int j = 0; j < 5; j++) {
            if (matrix[i][j] == ch) { // If character found
                return {i, j};        // Return its position
            }
        }
    }
    return {-1, -1}; // Return invalid position if character not found
}

// Function to prepare the plaintext message for Playfair encryption
string prepare(string msg) {
    msg.erase(remove(msg.begin(), msg.end(), ' '), msg.end()); // Remove spaces
    transform(msg.begin(), msg.end(), msg.begin(),
              ::toupper);                      // Convert to uppercase
    replace(msg.begin(), msg.end(), 'J', 'I'); // Replace 'J' with 'I'

    string res = ""; // Result string to hold prepared message
    int i = 0;

    // Process the message two characters at a time
    while (i < msg.length()) {
        char a = msg[i]; // First character
        char b = (i + 1 < msg.length()) ? msg[i + 1]
                                        : 'X'; // Second char, or 'X' if none

        if (a == b) {   // If both chars are the same
            res += a;   // Add first character
            res += 'X'; // Add 'X' to separate duplicates
            i += 1;     // Move forward by one to re-check next char pair
        } else {
            res += a; // Add both characters as a pair
            res += b;
            i += 2; // Move forward by two positions
        }
    }

    // If the result length is odd, append 'X' to complete pair
    if (res.length() % 2 != 0) {
        res += 'X';
    }
    return res; // Return the prepared message string
}

// Function to encrypt the message using the Playfair cipher
string playfairEncrypt(string msg, string key) {
    vector<vector<char>> matrix = createMatrix(key); // Create cipher matrix
    string p = prepare(msg);                         // Prepare the message
    string out = "";                                 // Result encrypted string

    // Process message two characters at a time
    for (int i = 0; i < p.length(); i += 2) {
        char a = p[i];
        char b = p[i + 1];

        auto [r1, c1] = findPos(matrix, a); // Find position of first char
        auto [r2, c2] = findPos(matrix, b); // Find position of second char

        if (r1 == r2) {                      // Same row case
            out += matrix[r1][(c1 + 1) % 5]; // Replace each by character to
                                             // right (wrap around)
            out += matrix[r2][(c2 + 1) % 5];
        } else if (c1 == c2) { // Same column case
            out += matrix[(r1 + 1) % 5]
                         [c1]; // Replace each by character below (wrap around)
            out += matrix[(r2 + 1) % 5][c2];
        } else {                   // Rectangle case
            out += matrix[r1][c2]; // Replace by characters in same row but
                                   // columns swapped
            out += matrix[r2][c1];
        }
    }
    return out; // Return the encrypted ciphertext
}

// Function to decrypt the Playfair ciphertext
string playfairDecrypt(string ct, string key) {
    vector<vector<char>> matrix = createMatrix(key); // Create cipher matrix
    string out = "";                                 // Result decrypted string

    // Process ciphertext two characters at a time
    for (int i = 0; i < ct.length(); i += 2) {
        char a = ct[i];
        char b = ct[i + 1];

        auto [r1, c1] = findPos(matrix, a); // Find position of first char
        auto [r2, c2] = findPos(matrix, b); // Find position of second char

        if (r1 == r2) { // Same row case
            out += matrix[r1][(c1 - 1 + 5) %
                              5]; // Replace each by character to left
            out += matrix[r2][(c2 - 1 + 5) % 5];
        } else if (c1 == c2) { // Same column case
            out +=
                matrix[(r1 - 1 + 5) % 5][c1]; // Replace each by character above
            out += matrix[(r2 - 1 + 5) % 5][c2];
        } else {                   // Rectangle case
            out += matrix[r1][c2]; // Replace by characters in same row but
                                   // columns swapped
            out += matrix[r2][c1];
        }
    }
    return out; // Return the decrypted plaintext
}

int main() {
    string msg = "HELLO WORLD"; // Original plaintext message
    string key = "KEYWORD";     // Encryption key

    string enc = playfairEncrypt(msg, key); // Encrypt the message using the key
    string dec =
        playfairDecrypt(enc, key); // Decrypt the ciphertext using the key

    cout << "Original: " << msg << endl;
    cout << "Encrypted: " << enc << endl;
    cout << "Decrypted: " << dec << endl;

    return 0; // Indicate successful program termination
}
