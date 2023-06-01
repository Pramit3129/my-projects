public class sortedornot {
    public static void main(String[] args){
        int[] num= {3,4,8,60,10};
        boolean b = true;
        for(int i=0;i<num.length-1;i++){       // note: here length -1 is used
            if(num[i]<num[i+1]){b=true;}
            else{b=false;
            break;}}
        if(b==true){
            System.out.println("sorted");}
        else{
            System.out.println("Not Sorted");}
        }
    }

