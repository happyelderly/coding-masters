import java.io.*;

import java.util.*; 

public class Main {
    public static void main(String[] args) throws IOException { 

        Scanner scanner = new Scanner(System.in); 

        int n = scanner.nextInt(); 
        String[] names = new String[n];
        int[] iqs = new int[n];
        int i;
        for(i=0 ; i<n ; ++i){
            names[i] = scanner.next();
            iqs[i] = scanner.nextInt();
        }
        
        List<int[]> students = new ArrayList<>();
        for(i=0 ; i<n ; ++i){
            students.add(new int[]{iqs[i], i});
        }
        
        students.sort((a,b) -> b[0] - a[0]);
        
        for(i=0 ; i<3 ; ++i){
            System.out.println(names[students.get(i)[1]]);
        }

    }
}