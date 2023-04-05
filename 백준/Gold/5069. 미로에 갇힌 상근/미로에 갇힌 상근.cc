#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <cmath>
#include <queue>
#include <stack>
#include <string>
typedef long long ll;
using namespace std;
const int MAX = 15;
const int INF = 1e9 + 7;
int N, d[MAX] = { 0, 0, 6, 12, 90, 360, 2040,
10080, 54810, 290640, 1588356, 8676360, 47977776, 266378112,
1488801600 };
int main() {
	cin.tie(0);
	cout.tie(0);
	ios::sync_with_stdio(false);

	int t;
	cin >> t;
	while (t--) {
		cin >> N;
		cout << d[N] << "\n";
	}
}