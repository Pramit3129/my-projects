import java.util.Scanner;
public class count_the_no_of_1s {
    public static int power(int a){ //this function to check up to which position the no. is having bit value
        int n = 1;
        int k = 1;
        while(k<=a){
            k*=2;
            n++;
        }
        return n;
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); //number in which we need to check
        int cnt = 0; //counter
        int c= power(n);
        for(int p=0;p<=c;p++){
            int bitmask=1<<p; //making bitmask everytime while checking every position
            if ((bitmask & n)!=0){
                cnt+=1;

            }
        }
        System.out.println("Total no. of ones: "+cnt);
    }
}
