import java.io.*;

import java.util.*; 

public class Main {
    public static void main(String[] args) throws IOException { 

        Scanner scanner = new Scanner(System.in); 

        int a = scanner.nextInt(); 

        StringBuilder b = new StringBuilder();
        StringBuilder c = new StringBuilder();
        
        int temp = a;
        
        while(a != 0){
            b.insert(0, a%8);
            a /= 8;
        }
        
        a = temp;
        
        while(a != 0){
            int d = a%16;
            if(d == 10){
                c.insert(0, 'A');
            }else if(d == 11){
                c.insert(0, 'B');
            }else if(d == 12){
                c.insert(0, 'C');
            }else if(d == 13){
                c.insert(0, 'D');
            }else if(d == 14){
                c.insert(0, 'E');
            }else if(d == 15){
                c.insert(0, 'F');
            }else{
                c.insert(0, d);
            }
            a /= 16;
        }
        

        System.out.println(b.toString() + " " + c.toString());

    }
}