public static Node removeDuplicates(Node head) {
  if(head.next == null || head == null){
     return head;
  }
  Node nextNode = removeDuplicates(head.next);

  if(nextNode.data == head.data){
      head.next = nextNode.next;
  }
  return head;
}
