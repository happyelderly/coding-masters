package firstRound.basic;

import java.io.*;
import java.util.Scanner;

public class MakingGameId {

    private String solution(String input) {
        if (input.length() > 20 ) {
            return "I";
        } else {
            return "P";
        }
    }

    public static void main(String[] args) throws IOException {
        MakingGameId main = new MakingGameId();
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        BufferedWriter bf = new BufferedWriter(new OutputStreamWriter(System.out));
//        String answer = main.solution(br.readLine());
//        bf.write(answer);
//        bf.close();

        Scanner scanner = new Scanner(System.in);

        String input = scanner.nextLine();

        String answer = main.solution(input);

        System.out.println(answer);
    }
}
