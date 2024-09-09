package jop.posting;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

// 10배 문제
public class Example {
    public int solution(int input) {
        return input * 10;
    }

    public static void main(String[] args) throws IOException {
        Example main = new Example();
        var br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bf = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        int answer = main.solution(n);
        bf.write(String.valueOf(answer));
        bf.flush();
    }
}
