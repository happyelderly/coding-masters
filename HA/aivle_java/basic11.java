import java.io.*;

import java.util.*; 

public class Main {
    public static void main(String[] args) throws IOException { 

        Scanner scanner = new Scanner(System.in); 

        int a = scanner.nextInt(); 

        int[] n = new int[a];
        
        int i;
        
        for(i=0 ; i<a ; ++i){
            n[i] = scanner.nextInt();
        }
        
        int t=0;
        for(i=0 ; i<a ; ++i){
            if(n[i]<=160){
                t = 1;
                System.out.println(\"I \"+ n[i]);
                break;
            }
        }
        if(t == 0){
            System.out.println(\"P\");
        }
    }
}