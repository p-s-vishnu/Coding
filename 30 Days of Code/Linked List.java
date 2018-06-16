public static  Node insert(Node head,int data) {
    Node element = new Node(data);
    element.next= null;

    if(head == null){
        head = element;
    }else{
        Node p = head;
        while (p.next !=null ){
            p = p.next;
        }
        p.next = element;


    }
    return head;
}
