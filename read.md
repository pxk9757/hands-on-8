2: Implement and upload your source code to github for: stack, queue, and singly linked list.

## Answers

## Stack sorce code
#include <iostream>
#include <stdexcept>

using namespace std;

class StackException : public runtime_error {
public:
    StackException(const string& msg) : runtime_error(msg) {}
};

class FixedStack {
private:
    static const int MAX_SIZE = 100;
    int arr[MAX_SIZE];
    int top;

public:
    FixedStack() : top(-1) {}

    void push(int data) {
        if (top >= MAX_SIZE - 1) {
            throw StackException("Stack overflow");
        }
        arr[++top] = data;
    }

    int pop() {
        if (top < 0) {
            throw StackException("Stack underflow");
        }
        return arr[top--];
    }

    int peek() {
        if (top < 0) {
            throw StackException("Empty stack");
        }
        return arr[top];
    }

    bool isEmpty() {
        return top == -1;
    }

    int getSize() {
        return top + 1;
    }
};

### Queue Source Code
#include <iostream>
using namespace std;

const int MAX_SIZE = 100;

class Queue {
private:
    int queue[MAX_SIZE];
    int front;
    int rear;

public:
    Queue() {
        front = -1;
        rear = -1;
    }

    void enQueue(int value) {
        if ((rear + 1) % MAX_SIZE == front) {
            cout << "Queue is full!" << endl;
            return;
        }
        if (front == -1) {
            front = 0;
        }
        rear = (rear + 1) % MAX_SIZE;
        queue[rear] = value;
    }

    int deQueue() {
        if (isEmpty()) {
            cout << "Queue is empty!" << endl;
            return -1;
        }
        int value = queue[front];
        if (front == rear) {
            front = -1;
            rear = -1;
        } else {
            front = (front + 1) % MAX_SIZE;
        }
        return value;
    }

    bool isEmpty() {
        return front == -1 || front > rear;
    }

    int size() {
        if (isEmpty()) {
            return 0;
        }
        if (rear >= front) {
            return rear - front + 1;
        } else {
            return MAX_SIZE - front + rear + 1;
        }
    }

    int frontValue() {
        if (isEmpty()) {
            cout << "Queue is empty!" << endl;
            return -1;
        }
        return queue[front];
    }

    int rearValue() {
        if (isEmpty()) {
            cout << "Queue is empty!" << endl;
            return -1;
        }
        return queue[rear];
    }
};

   ### singly linked list
   #include <iostream>
#include <stdexcept>

using namespace std;

class ListException : public runtime_error {
public:
    ListException(const string& msg) : runtime_error(msg) {}
};

class Node {
public:
    int data;
    Node* next;

    Node(int data) : data(data), next(nullptr) {}
};

class SinglyLinkedList {
private:
    Node* head;

public:
    SinglyLinkedList() : head(nullptr) {}

    void insertAtBeginning(int data) {
        Node* newNode = new Node(data);
        newNode->next = head;
        head = newNode;
    }

    int removeAtBeginning() {
        if (head == nullptr) {
            throw ListException("Empty list");
        }
        int data = head->data;
        Node* temp = head;
        head = head->next;
        delete temp;
        return data;
    }

    bool isEmpty() {
        return head == nullptr;
    }

    int getSize() {
        int size = 0;
        Node* current = head;

        while (current != nullptr) {
            size++;
            current = current->next;
        }

        return size;
    }
};