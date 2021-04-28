class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int temp = 0;
        ListNode t1,t2 = new ListNode(0);
        t1 = t2;// we dont t1 is a shallow copy t1 t2 is the same thing here in memory t1 is t2 
        while(l1 != null || l2!= null || temp != 0){
            if(l1 != null){
                temp +=l1.val;
                l1= l1.next;
            }if(l2!= null){
                temp += l2.val;
                l2 =l2.next;
            }
            t1.next = new ListNode(temp%10);
            temp/=10;
            t1 = t1.next;
        }
        
        return t2.next; // return t2 is because Java is actually passed by a copy of the reference.
        // So here, dummy remains as the start node, while p gets iteratively built up by the program.
        // System.out.println(t1);
    }
}