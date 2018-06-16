import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. */

        Scanner scan = new Scanner(System.in);
        int t = Integer.parseInt(scan.nextLine());
        while(t-- >0){
            int num = Integer.parseInt(scan.nextLine());
            boolean isPrime = (num == 1? false : true);
            for(int i=2;i<=Math.sqrt(num);i++){
                if(num % i == 0){
                   isPrime = false;
                   break;
                }
            }
            System.out.println(isPrime == false ? "Not prime": "Prime");
        }
        scan.close();
    }
}
