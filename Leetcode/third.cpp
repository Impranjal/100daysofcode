#include <bits/stdc++.h>
using namespace std;
int sum(int ar[],int b[],int n)
{
    int first=0;
    int second=n-1;
    int c=0;
    while(first <n && second>=0)
    {
        if(ar[first]>b[second])
        {
            second--;
        }
        else if(ar[first]<b[second])
        {
            first++;
        }
        else
        {
            c++;
            first++;
            second--;
        }
    }
    return c;


}
int main()
{
    int arr[3]={2,3,4};
    int b[3]={2,3,5};
    int n=sizeof(arr)/sizeof(int);
    cout<<sum(arr,b,n);
    return 0;
}