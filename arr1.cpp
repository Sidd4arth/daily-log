#include<iostream>
using namespace std;
int main()
{
    int arr[6];
    for(int i=0; i<6;i++)
    {
        cout<<"Enter "<<i<<" th element for array :" <<endl;
        cin>>arr[i];
    }
    cout<<"Enter array is:"<<endl;
    for(int i=0; i<6;i++)
    {
        cout<<arr[i]<< " ";
    }
    return 0;

}