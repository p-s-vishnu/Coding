import java.io.*;
import java.util.*;

public class Solution {
    public static int count=0;

    public int[] sort(int[] arr ){
        int n = arr.length;
        for(int i=0 ; i<n ; i++){

            for(int j=0 ; j<n-i-1 ; j++){
                 if(arr[j] > arr[j+1]){
                     int temp  = arr[j];
                     arr[j] =arr[j+1] ;
                     arr[j+1] = temp;

                     count++;
                 }
            }
            if(count==0) break;
        }
        return arr;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n;
        int[] arr = new int[n=scan.nextInt()];
        for(int i=0 ; i<n;i++){
            arr[i]=scan.nextInt();
        }

        arr=(new Solution()).sort(arr);
        System.out.println("Array is sorted in "+ count + " swaps.");
        System.out.println("First Element: "+ arr[0]);
        System.out.println("Last Element: "+ arr[n-1]);
    }
}
