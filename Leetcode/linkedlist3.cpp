#include <bits/stdc++.h>
using namespace std;
class Node{
    int data;
    Node* next;
    
};
void push(Node** head,int data)
{
    Node new_node=new Node();
    new_node->data=data;
    new_node->next=(*head);
    *head=new_node;
}
Node* merge(Node* head1,Node* head2)
{
  
    Node* dummy;
    if (head1 == NULL) {
      return head2;
   }
   if (head2 == NULL) {
      return head1;
   }
    while(head1!=NULL && head2!=NULL)
    {
        if(head1->data<head2->data)
        {
            dummy=head1;
             dummy->next=merge(head1->next,head2);
        }
        else
        {
            dummy=head2;
            dummy->next=merge(head1,head2->next);
        }
    }
    return result;
    
}