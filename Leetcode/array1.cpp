#include <bits/stdc++.h>
using namespace std;
int rotate(int arr[],int n)
{
    int start=0;
    int end=n-1;
    while(start<end)
    {
        int temp;
        temp=arr[start];
        arr[start]=arr[end];
        arr[end]=temp;
        start++;
        end--;
    }

}
int printarray(int arr[],int n)
{
    for(int i=0;i<n;i++)
    {
        cout<<arr[i];
    }
    cout<<endl;
}
int main()
{
    int arr[]={1,2,3,4,5,6};
    int n=sizeof(arr)/sizeof(arr[0]);
    rotate(arr,n);
    printarray(arr,n);
    return 0;

}