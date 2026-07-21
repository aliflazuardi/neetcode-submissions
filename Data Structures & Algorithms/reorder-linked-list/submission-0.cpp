/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    void reorderList(ListNode* head) {
        ListNode* slowP = head;
        ListNode* fastP = head->next;
        // split list into two section
        while(fastP != nullptr && fastP->next != nullptr) {
            slowP = slowP->next; // end of first half
            fastP = fastP->next->next; 
        }

        ListNode* second = slowP->next; // second part
        slowP->next = nullptr; // detached second part from first part
        ListNode* prev = nullptr;
        // reverse second part of list
        while(second != nullptr) {
            ListNode* temp = second->next;
            second->next = prev;
            prev = second;
            second = temp;
        }

        ListNode* first = head;
        second = prev; // end of list (already reversed)
        while (second != nullptr) { // only need to check second because first length can be longer
            ListNode* temp1 = first->next;
            ListNode* temp2 = second->next;
            first->next = second;
            second->next = temp1;
            first = temp1;
            second = temp2;
        }
    }
};
