import java.io.*;
import java.util.*;


public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        Stack s=new Stack();

        for(int i=0; i < n; i++){

        s.push(in.nextInt());

        }
        while(!s.empty()){
            System.out.print( (int)s.pop()+ " ");
        }
        in.close();
    }
}
