import java.io.*;
import java.util.*; 

public class Main {
    public static void main(String[] args) throws IOException { 

        Scanner scanner = new Scanner(System.in); 

        String a = scanner.nextLine(); 

        if(a.length()>20){
            System.out.println("I");
        }else{
            System.out.println("P");
        }
    }
}