//array2
#include<iostream>
using namespace std;
int main()
{
    int n;
    cout<<"Enter the length of an array:  ";
    cin>>n;
    int* arr= new int[n];
    for(int i=0; i<n;i++)
    {
    cout<<"Enter " <<i+1<< " value of an array";
    cin>>arr[i];
    }

    cout<<"Entered array: ";
    for(int i=0;i<n;i++)
    {
        cout<<arr[i]<<" ";
    }
    return 0;
}