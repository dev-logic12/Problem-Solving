#include <iostream>
#include <string>
using namespace std;
long long result=0,len;
string str;

void dfs(int idx, int m, int j, bool l, long long cnt){
    if(idx==len){
        if(l)    result+=cnt;      
        return;
    }
    char c = str[idx];
    if(c=='_'){
        bool mavail=true;
        bool javail=true;
        if(m==2)  mavail=false;
        if(j==2) javail=false;
        if(mavail)  dfs(idx+1,m+1,0,l,cnt*5);
        if(javail){
            dfs(idx+1,0,j+1,true,cnt);
            dfs(idx+1,0,j+1,l,cnt*20);
        }
    }
    else if(c=='A' || c=='E' || c=='I' || c=='O' || c=='U'){
        if(m==2) return;
        dfs(idx+1,m+1,0,l,cnt);
    }
    else{
        if(j==2) return;
        if(c=='L') dfs(idx+1,0,j+1,true,cnt);
        else dfs(idx+1,0,j+1,l,cnt);
    }
}

int main() {
    cin>>str;
    len = str.size();
    dfs(0,0,0,false,1);
    cout<<result;
    return 0;
}