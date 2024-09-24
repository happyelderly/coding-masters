import java.io.*;

import java.util.*; 

public class Main {
    public static void main(String[] args) throws IOException { 

        Scanner scanner = new Scanner(System.in); 

        int a = scanner.nextInt();
        
        int count = 0;
        int t = 0;
        
        for(int i=2 ; i<a+1 ; ++i){
            for(int j=2 ; j<i ; ++j){
                if(i%j==0){
                    t = 1;
                    break;
                }
            }
            if(t==0){
                ++count;
            }
            t=0;
        }

        System.out.println(count); 

    }
}