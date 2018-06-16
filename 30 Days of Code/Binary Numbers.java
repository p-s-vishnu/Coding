import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int max=0,count=0;
        String b = new String( Integer.toBinaryString( scan.nextInt() ) );
        char[] bin= b.toCharArray();
        for(int i=0 ; i < b.length(); i++){

            count = (bin[i] == '1') ? ++count : 0;
            //System.out.println(i +":"+  count);
            max = (max<count) ? count : max;

        }
        System.out.println(max);
    }
}
