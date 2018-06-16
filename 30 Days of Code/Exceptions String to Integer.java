import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int msg=0;
        try{
            msg = Integer.parseInt(scanner.nextLine());
             System.out.println(msg);
        }catch(NumberFormatException e)
        {
             System.out.println("Bad String");
        }


    }
}
