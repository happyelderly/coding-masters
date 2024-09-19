import java.io.*;

import java.util.*; 

public class Main {
    public static void main(String[] args) throws IOException { 

        Scanner scanner = new Scanner(System.in); 

        int a = scanner.nextInt(); 

        int b = scanner.nextInt(); 
        
        int c = scanner.nextInt();
        
        if((a+b+c==180) && (a>0) && (b>0) && (c>0)){
            System.out.println("P"); 
        }else{
            System.out.println("F"); 
        }


    }
}