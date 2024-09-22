import java.io.*;

import java.util.*; 

public class Main {
    public static void main(String[] args) throws IOException { 

        Scanner scanner = new Scanner(System.in); 

        String a = scanner.next(); 

        if(a.equals("You")){
            System.out.println("Me");
        }else{
            System.out.println("No");
        }
    }
}