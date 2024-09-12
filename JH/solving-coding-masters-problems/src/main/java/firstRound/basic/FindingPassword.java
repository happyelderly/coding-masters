package firstRound.basic;

/*
A 회사 총무부서가 분주합니다. 중요한 파일이 모두 들어있는 컴퓨터의 비밀번호를 까먹었기 때문입니다.
다행히 책상에는 전임자가 놓고간 힌트가 담긴 쪽지가 놓여있습니다. 쪽지의 내용은 이러합니다.
'비밀번호는 쉴새없이 변하며, 컴퓨터 화면에는 매 번 일련의 문자들이 주어집니다.
 단 컴퓨터 화면에서 알파벳 c까지의 알파벳 문자열이 비밀번호입니다.'
 머리가 좋은 김대리는 바로 이해를 하고 암호를 풀었습니다. 이때 김대리가 사용한 방법을 프로그램으로 작성하세요.
 */

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class FindingPassword {

    public char[] solution(String[] input) {
        char[] chars = new char[input.length];
        char[] password;
        int count = 0;
        for (int i = 0; i < input.length; i++) {
            char c = input[i].charAt(0);
            chars[i] = c;
            count++;
            if (c == 'c') {
                break;
            }
        }
        password = new char[count];
        for (int i = 0; i < count; i++) {
            password[i] = chars[i];
        }
        return password;
    }

    public static void main(String[] args) throws IOException {
        FindingPassword findingPassword = new FindingPassword();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bf = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] input = br.readLine().split(" ");
        char[] password = findingPassword.solution(input);
        for (int i = 0; i < password.length; i++) {
            bf.write(password[i] + " ");
        }
        bf.flush();
    }
}
