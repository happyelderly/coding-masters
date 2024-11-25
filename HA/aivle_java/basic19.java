import java.io.*;

import java.util.*; 

public class Main {
    public static void main(String[] args) throws IOException { 

        Scanner scanner = new Scanner(System.in); 

        int n = scanner.nextInt(); 

        int m = scanner.nextInt();
        
        int a=0;
        
        for(int i=1 ; i<n+1 ; ++i){
            if((n%i==0)&&(m%i==0)){
                a = i;
            }
        }
        
        System.out.println(a); 

    }
}