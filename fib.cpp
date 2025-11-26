//fiboncci series
//0 1 1 2 3 5 ...
// a=0
// b=1
// c= a+b

#include<iostream>
using namespace std;
int main()
{
    int n;
    cout<<"Enter the no. of terms: ";
    cin>>n;
    int a=0;
    int b=1;
    cout<<"Fibonacci series: "<< a <<" "<<" ";

    for(int i=2; i<=n;i++)
    {
        int next = a+b;
        cout<<next<<" ";
        a=b;
        b=next;
    }
    cout<<endl;
    return 0;
}