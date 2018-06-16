public static int getHeight(Node root){
     if(root == null )
         return -1;
     if(root.left== null && root.right == null )
         return 0;
     return 1 + Math.max( getHeight(root.left), getHeight(root.right));
  }
