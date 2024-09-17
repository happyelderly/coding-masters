import java.io.*;

import java.util.*; 

public class Main {
    public static void main(String[] args) throws IOException { 

        Scanner scanner = new Scanner(System.in); 

        int a = scanner.nextInt(); 
        
        int count = 0;
        
        count += a/50000;
        a %= 50000;
        
        count += a/10000;
        a %= 10000;
        
        count += a/5000;
        a %= 5000;
        
        count += a/1000;
        a %= 1000;
        
        count += a/500;
        a %= 500;
        
        count += a/100;
        a %= 100;
        
        count += a/50;
        a %= 50;
        
        count += a/10;
        

        System.out.println(count); 

    }
}