#include <bits/stdc++.h>
using namespace std;
class Node
{

int data;
Node* next;
};
void push(Node** head_ref,int new_data)
{
    Node* new_node=new Node();
    new_node->data=new_data;
    new_node->next=(*head_ref);

}
void insertafter(Node* prev,int ner)
{
    if(prev==NULL)
    {
        cout<<"the given previous node cannnot be null";
        return ;

    }
    Node* nn=new Node();
    nn->data=ner;
    nn->next=prev->next;
    prev->next=nn;

}
void append(Node** head_ref,int new_data)
{
    Node* new_node=new Node();
    Node* last=*head_ref;
    new_node->data=new_data;
    if(head_ref==NULL)
    {
        head_ref=new_node;
        return;
    }
    if(last->next!=NULL)
    {
        last=last->next;

    }
    last->next=new_node;
    return;
}