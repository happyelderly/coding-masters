//////////////////////////////////// Java ////////////////////////////////////
//기초-1.비밀번호 찾기
import java.util.Scanner; //Sanner 사용을 위해
public class Main {
    //pubic:
    //Main:
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();  // 사용자 입력 받기

        // 'c' 문자의 위치를 찾고, 그 위치까지의 문자열을 출력
        int index = input.indexOf('c');
        if (index != -1) {
            System.out.println(input.substring(0, index + 1));
        } else {
            System.out.println(input);  // 'c'가 없을 경우 전체 문자열 출력
        }
        
        scanner.close();
    }
}

//기초-2.등차수열
