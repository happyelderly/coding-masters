import java.io.*;
import java.util.*; 

public class Main {
    public static void main(String[] args) throws IOException { 

        Scanner scanner = new Scanner(System.in); 

        int a = scanner.nextInt(); 

        int f = a%5;
        
        int s = a%7;
        
        int max;
        
        if(f>s){
            max = f;
        }else{
            max = s;
        }

        System.out.println(max); 

    }
}