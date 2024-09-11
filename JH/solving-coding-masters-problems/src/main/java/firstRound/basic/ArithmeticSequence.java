package firstRound.basic;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.io.*;

import java.util.*;

public class ArithmeticSequence {

    /*
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bf = new BufferedWriter(new OutputStreamWriter(System.out));
        int[] input = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        // 0 : 3 시작점
        // 1 : 5 더할값
        // 2 : 7 몇번째인지 -> 시작점이 첫번째였으니, 6번을 더해주면 7번째 항이 된다.
        int count = 0;
        int answer = input[0];
        while (!(count > input[2] - 2)) {
            count++;
            answer += input[1];
        }
        bf.write(answer + "\n");
        bf.flush();
    }

     */

    // Scanner version
    public static void main(String[] args) throws IOException {

        Scanner scanner = new Scanner(System.in);

        int a = scanner.nextInt();
        int b = scanner.nextInt();
        int n = scanner.nextInt();

        int count = 0;
        while (!(count > n - 2)) {
            count++;
            a += b;
        }
        System.out.println(a);
    }
}
