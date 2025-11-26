/*
n 
divide by 2
store remainder
repeat while ( n!=0)
reverse ans
*/
#include<iostream>
using namespace std;
#include<math.h>
int main()
{
    int ans=0;
    int i=0;
    int n;
    cin>>n;

    while(n!=0)
    {
        int bit = n & 1;
        ans = (bit * pow(10, i)) + ans;
        n=n>>1;
        i++;
    }
    cout<<"Answere is: "<<ans<<endl;

}