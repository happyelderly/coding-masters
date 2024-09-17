import java.io.*;

import java.util.*; 

public class Main {
    public static void main(String[] args) throws IOException { 

        Scanner scanner = new Scanner(System.in); 

        int a = scanner.nextInt(); 
        
        char b;

        if(a >= 200){
            b = 'A';
        }else if(a >= 180){
            b = 'B';
        }else if(a >= 150){
            b = 'C';
        }else{
            b = 'D';
        }

        System.out.println(b); 

    }
}