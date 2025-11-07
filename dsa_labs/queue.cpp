// Problem-6: Write a programme to implement queue
// with typical operations

// Author: MD. Parvez ALi,
// Roll: 210623
// Session: 2021-22

// [Explaination]......
// Link Class:
// Node with an integer data member and a pointer to the next node.
// Queue Class:
// Implements a queue using a linked list.
// head points to the head,and curr points to the last node.
// Public methods:push,pop,front,print.
// Operations:
// 	push:Adds to the end.
// 	pop:Removes from the front.
// 	front:Returns data from the front.
// 	print:Displays the queue.
// 	Memory:
// 	Uses dynamic memory allocation(new) for node creation.
// 	free is used for memory deallocation during popping.

// [Source Code in C++]
#include <bits/stdc++.h>
using namespace std;

class Link{
public:
	int data;
	Link* next;
	Link(){
		next=nullptr;
	}
	Link(int d){
		data=d;
		next=nullptr;
	}
};
class Queue{
	Link* head=new Link();
	Link* curr=head;
public:
	void push(int d){
		Link* newnode=new Link(d);
		curr->next=newnode;
		curr=curr->next;
	}
	void pop(){
		if(head->next != nullptr){
			Link* temp=head->next;
			free(head);
			head=temp;
		}
	}
	int front(){
		if(head->next != nullptr){
			return head->next->data;
		}
		return -1;
	}
	void print(){
		Link* here=head->next;
		while(here != nullptr){
			cout << here->data << ">";
			here=here->next;
		}
		cout << endl;
	}
};
int main(){
	Queue q;
	q.push(4);
	q.push(7);
	q.push(9);
	q.print();
	q.push(8);
	cout << q.front() << endl;
	q.pop();
	q.print();
	return 0;
}
