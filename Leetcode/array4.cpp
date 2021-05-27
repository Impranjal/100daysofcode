// Example program
#include <iostream>
#include<bits/stdc++.h>
#include <string>
using namespace std;
void shift(int arr[],int n)
{
   int temp=arr[n-1];
  for(int i=0;i<n;i++)
    {
      arr[i]=arr[i-1];
    }
  arr[0]=temp;
            
}

int main()
{
 int arr[]={2,2,2,3,1};
 int n=sizeof(arr)/sizeof(arr[0]);
 shift(arr,n);
 for(int i=0;i<n;i++)
 {
     cout<<arr[i];
 }
 return 0;
}
