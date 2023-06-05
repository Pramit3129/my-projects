import java.util.Scanner;
public class checking_if_no_is_power_of_n {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n= sc.nextInt();
        int k=0;
        for(int i=1;i<=n;i*=2){
            if(i==n){
                k=1;
                break;
            }
        }
        if(k==1){
            System.out.println("Yes");
        }
        else{
            System.out.println("No");
        }
    }
}
