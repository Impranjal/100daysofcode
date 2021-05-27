// Example program
#include <iostream>
#include<bits/stdc++.h>
#include <string>
using namespace std;
void shift(int arr[],int n)
{
    int low=0;
    int mid=0;
    int high=n-1;
    while(mid<=high)
    {
        switch(arr[mid])
        {
            case 0:
            swap(arr[low],arr[mid]);
            low++;
            mid++;
            break;
            case 1:
            mid++;
            break;
            case 2:
            swap(arr[mid],arr[high]);
            high--;
            break;
        }
        
            
}}

int main()
{
 int arr[]={0,1,1,2,2,0,0};
 int n=sizeof(arr)/sizeof(arr[0]);
 shift(arr,n);
 for(int i=0;i<n;i++)
 {
     cout<<arr[i];
 }
 return 0;
}
