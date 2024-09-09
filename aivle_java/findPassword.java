import java.io.*;
import java.util.*; 

public class Main {
    public static void main(String[] args) throws IOException { 
        
        Scanner scanner = new Scanner(System.in); 

        String a = scanner.nextLine();
        
        String[] b = a.split(" ");
        
        StringBuilder result = new StringBuilder();
        
        for(int i=0 ; i<b.length ; ++i){
            result.append(b[i]).append(" ");
            if(b[i].equals("c")){
                break;
            }
        }
        
        System.out.println(result.toString().trim());

    }
}