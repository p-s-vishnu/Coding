import java.io.*;
import java.util.*;

public class Solution {

    public int factorial(int n){
        if(n==1){
            return 1;
        }else{
            return n*factorial(n-1);
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int fact = sc.nextInt();
        Solution a = new Solution();
        System.out.println( ""+ a.factorial(fact) );
    }
}
