import java.util.Scanner;
public class maxmin {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter Size of the Array:");
        int s = sc.nextInt();
        int[] num  = new int[s];
        for(int i=0; i<s ;i++){
            System.out.println("Enter Element no.-  "+(i+1));
            num[i]=sc.nextInt();}
        int smallest= num[0];
        int largest = num[0];
        for(int i=0;i<s;i++){
            if(num[i]>largest){largest=num[i];}
            if(num[i]<smallest){smallest=num[i];}}
        System.out.println("Largest number: "+largest);
        System.out.println("Smallest number: "+smallest);}}

