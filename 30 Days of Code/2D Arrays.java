import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

   public static class CroppedArray
   {
        int[][] b = new int [3][3];
       CroppedArray(int[][] arr , int I , int J )
       {
              for(int i=I,k=0 ; i< I+3 ; i++,k++){
                  for(int j=J,l=0; j< J+3; j++,l++){
                      b[k][l] = arr[i][j];
                  }
              }
       }
       public int maximum()
           {
           int sum=0;
           b[1][0]=b[1][2]=0;

           for(int i =0 ; i<3 ; i++)
               for(int j=0;j<3;j++ )
                sum+=b[i][j];

           return sum;
       }
   }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int[][] arr = new int[6][6];
        int max=-64;
        for(int i=0; i < 6; i++){
            for(int j=0; j < 6; j++){
                arr[i][j] = in.nextInt();
            }
        }

        for(int i=0; i < 4; i++){
            for(int j=0; j < 4; j++){
               int value = new CroppedArray(arr,i,j).maximum();
               max = (max < value )? value : max; ;
             }
        }
        System.out.println(max);
    }
}
