#include <iostream>
#include <map>
#include <string>
#include <utility>
#include <vector>
using namespace std;

vector<pair<int, char>> encode(string s) {
  vector<pair<int, char>> out;
  map<string, int> mp;
  int indexing = 0;

  string w = "";
  for (auto c : s) {
    string curr = w + c;
    if (mp.find(curr) == mp.end()) {
      out.push_back({mp[w], c});
      mp[curr] = indexing + 1;
      indexing++;
      w = "";
    } else {
      w = curr;
    }
  }
  return out;
}
string decode(vector<pair<int, char>> &encoded) {
  string decoded = "";
  map<int, string> mp;
  int cnt = 1;
  for (auto [i, c] : encoded) {
    string k = (mp[i] + c);
    decoded += k;
    mp[cnt++] = k;
  }
  return decoded;
}
int main() {
  string s;
  cin >> s;
  auto ans = encode(s);
  for (auto [i, c] : ans) {
    cout << "(" << i << "," << c << ") ";
  }
  cout << endl;
  cout << decode(ans) << endl;
}
