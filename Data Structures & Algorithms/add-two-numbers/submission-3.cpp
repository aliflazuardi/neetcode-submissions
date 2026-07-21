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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* temp = new ListNode();
        ListNode* curr = temp;
        int carryOver = 0;
        while(l1 != NULL || l2 != NULL || carryOver != 0) {
            int val = carryOver;

            if(l1 != NULL) {
                val += l1->val;
                l1 = l1->next;
            }
            if(l2 != NULL) {
                val += l2->val;
                l2 = l2->next;
            }

            carryOver = val / 10;
            val = val % 10;
            
            ListNode* sum = new ListNode(val);
            curr->next = sum;
            curr = curr->next;
        }

        return temp->next;
    }
};
