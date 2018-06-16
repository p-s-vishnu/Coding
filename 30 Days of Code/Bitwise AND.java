import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Set<Integer> set = new HashSet<Integer>();
        Scanner scan = new Scanner(System.in);
        int T = scan.nextInt();
        while(T-- >0){
          int k=  scan.nextInt();
          int n = scan.nextInt();
          int a = k - 1;
          int b = (~a) & -(~a);

          if( (a | b) > n )
        	 System.out.println(a - 1);
          else
        	 System.out.println(a);
        }
       }
    }
