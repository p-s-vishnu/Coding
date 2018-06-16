static void levelOrder(Node root){
      Node element;
      Queue<Node> queue = new LinkedList<Node>();
      queue.add(root);
      while(!queue.isEmpty()){
          element = queue.remove();
          System.out.print(element.data +" ");
          if(element.left != null )
              queue.add(element.left);
          if(element.right != null )
              queue.add(element.right);
      }
  }
