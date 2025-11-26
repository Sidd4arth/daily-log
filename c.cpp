//largest element in an array
#include<iostream>
using namespace std;
int main()
{
    int n;
    int* arr= new int[n];
    cout<<"Enter length of array: ";
    cin>>n;
    cout<<endl;

    for(int i=0; i<n;i++)
    {
        cout<<"Enter "<<i+1<<"  value for an array: ";
        cin>>arr[i];
    }
    int largest =arr[0];
    for(int i=0; i<n;i++)
    {
        if(arr[i]>largest)
        largest=arr[i];
    }
    cout<<largest;
    return 0;
}