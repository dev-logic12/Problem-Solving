#include <bits/stdc++.h>
 
#define mod 10000003
 
using namespace std;
 
int seq[100];
int dp[100][100001];
 
int gcd(int a, int b) { return !b ? a : gcd(b, a % b); }
 
int main()
{
    ios::sync_with_stdio(false); cin.tie(0);
 
    int n;
    cin >> n;
 
    for (int i = 0; i < n; ++i)
    {
        cin >> seq[i];
        dp[i][seq[i]] = 1;
    }
 
    for (int i = 1; i < n; ++i)
    {
        for (int j = 1; j <= 100000; ++j)
        {
            dp[i][j] += dp[i - 1][j];
            dp[i][j] %= mod;
 
            int cop = gcd(seq[i], j);
            dp[i][cop] += dp[i - 1][j];
            dp[i][cop] %= mod;
        }
    }
 
    cout << dp[n - 1][1];
}
