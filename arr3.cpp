#include<iostream>
using namespace std;
int main()
{
    int arr[]={12,23,34,45,56,67};
    int seclargest=arr[0];
    int n = sizeof(arr)/ sizeof(arr[0]);
    int largest=arr[0];
    for(int i=0;i<n;i++)
    {
        if(arr[i]>largest)
        largest=arr[i];
    }
    for(int i=0;i<n;i++)
    {
        if(arr[i]>seclargest && arr[i]!=largest)
        seclargest=arr[i];
    }
    cout<<seclargest;
    return 0;
}