import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
public class Operators {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        double mealCost = scan.nextDouble(); // original meal price
        int tipPercent = scan.nextInt(); // tip percentage
        int taxPercent = scan.nextInt(); // tax percentage
        scan.close();

        double round =0.0;
        round = mealCost *(1+ 0.01 * tipPercent + (double)taxPercent * 0.01) ;
        int totalCost = (int) Math.round(round);

        System.out.println("The total meal cost is "+ totalCost + " dollars.");
    }
}
