import java.io.*;

import java.util.*; 

public class Main {
    public static void main(String[] args) throws IOException { 

        Scanner scanner = new Scanner(System.in); 

        int a = scanner.nextInt(); 

        int b = scanner.nextInt(); 
        
        int n = scanner.nextInt();

        System.out.println(a + b*(n-1)); 

    }
}