import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        while(T>0){
            String front="", back="";
            String s = scanner.next();
            char ch[] = s.toCharArray();
            for(int i=0; i<ch.length ; i++){
                if((i & 1) == 1){
                    back+=ch[i];
                }else{
                    front+=ch[i];
                }
            }
            System.out.println(front + " " + back);
            T--;
        }

    }
}
