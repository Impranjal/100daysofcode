#include <bits/stdc++.h>
using namespace std;
int max(int arr[],int n)
{ int max=INT_MIN;
    for(int i=0;i<n;i++)
    {
        if(arr[i]> max)
        {
            max=arr[i];
        }

    }
    return max;
}
int min(int arr[],int n)
{
    int min=INT_MAX;
    for(int i=0;i<n;i++)
    {
        if(arr[i]<min)
        {
            min=arr[i];
        }
    }

return min;
}
int main()
{
    int arr[]={1,2,3,4,5,6,7};
    int n=sizeof(arr)/sizeof(arr[0]);
    cout<<max(arr,n);
    cout<<min(arr,n);
    return 0;
}