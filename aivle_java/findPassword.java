/* A 회사 총무부서가 분주합니다. 중요한 파일이 모두 들어있는 컴퓨터의 비밀번호를 까먹었기 때문입니다.
다행히 책상에는 전임자가 놓고간 힌트가 담긴 쪽지가 놓여있습니다. 쪽지의 내용은 이러합니다.
'비밀번호는 쉴새없이 변하며, 컴퓨터 화면에는 매 번 일련의 문자들이 주어집니다. 단 컴퓨터 화면에서 알파벳 c까지의 알파벳 문자열이 비밀번호입니다.'
머리가 좋은 김대리는 바로 이해를 하고 암호를 풀었습니다. 이때 김대리가 사용한 방법을 프로그램으로 작성하세요. */


import java.io.*;
import java.util.*; 

public class Main {
    public static void main(String[] args) throws IOException { 
        
        Scanner scanner = new Scanner(System.in); 

        // 공백 상관 없이 한줄로 입력받아서 문자열에 저장
        String a = scanner.nextLine();
        
        // 공백 기준으로 문자열 나누기
        String[] b = a.split(" ");
        
        // 배열 편집 편하게 하기 위해 StringBuilder 불러오기
        StringBuilder result = new StringBuilder();
        
        // c가 발견되기 전까지 stringbuilder에 문자 추가
        for(int i=0 ; i<b.length ; ++i){
            result.append(b[i]).append(" ");
            if(b[i].equals("c")){
                break;
            }
        }
        
        // 마지막에 오는 공백 제거 후 출력
        System.out.println(result.toString().trim());

    }
}