import java.util.Scanner;
public class Positionofelement {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int s=sc.nextInt();
        int[] numbers=new int[s];
        for(int i=0;i<numbers.length;i++){
            numbers[i] = sc.nextInt();}
        int x= sc.nextInt();
        for(int i=0;i<s;i++){
            if (numbers[i]==x){
                System.out.println("Number found at position: "+i);}}
            }
        }

