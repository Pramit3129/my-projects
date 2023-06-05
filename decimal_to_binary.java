import java.util.Scanner;
public class decimal_to_binary {
    public static int pow(int a , int b){
        int n =1;
        for(int i = 0; i<b;i++){
            n*=a;
        }
        return n;
    }
    public static int power(int a){ //this function to check up to which position the no. is having bit value
        int n = 1;
        int k = 1;
        while(k<=a){
            k*=2;
            n++;
        }
        return n;}
    public static void Decimal_To_Binary(){
        Scanner sc = new Scanner(System.in);
        int n=sc.nextInt();
        int k=power(n);
        for(int i = k;i>=0;i--){
            int bitmask = 1<<i;
            if((n & bitmask)!=0){
                System.out.print('1');}
            else{
                System.out.print('0');
            }
        }
    }
    public static void Binary_to_decimal(){
        Scanner sc= new Scanner(System.in);
        String n = new String(sc.next());
        int b=0;
        for(int i=0;i<n.length();i++){
           int k=Character.getNumericValue(n.charAt(n.length()-1-i));
            b += k * pow(2, i);
        }
        System.out.println("The decimal number is: "+b);
    }
public static void main(String[] args){
    System.out.println("Press 1 to Convert Binary to Decimal");
    System.out.println("Press 2 to convert Decimal to Binary");
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    if(n==1){
        Binary_to_decimal();}
    else{
        Decimal_To_Binary();
    }
}
}
