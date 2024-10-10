//////////////////////////////////// Java ////////////////////////////////////
//기초-1.비밀번호 찾기
import java.util.Scanner; 
//Sanner 사용을 위해
public class Main {
    //pubic: 접근 제어자
    //class: java는 클래스 기반 언어
    //Main: java의 시작점(클래스 이름은 파일 이름과 동일???)
    public static void main(String[] args) { //이것도 시작점??
        //static:객체를 생성하지 않고도 이 메서드를 호출할 수 있음????? -> 메모리 로드 시 바로 실행
        //void: 반환 x
        //main: 명령줄에서 인수를 받을 때 사용. arg는 문자열
        //String[] args:
        Scanner scanner = new Scanner(System.in);
        //new: 새로운 객체 생성?
        //Scanner: java에서 입력 받는데 사용
        //System.in: 표준 입력 스트림
        //Scanner scanner: 객체??????
        String input = scanner.nextLine(); 
        //nextLine(): 입력한 한줄의 문자영을 읽어옴
        //String input
        int index = input.indexOf('c');
        //input.indexOf: c위치 찾아서 인덱스 반환
        //int index
        if (index != -1) {
            System.out.println(input.substring(0, index + 1));
            //input.substring:문자열 n~m까지 반환
            //System.out.println: 출력
        } else {
            System.out.println(input);  // 'c'가 없을 경우 전체 문자열 출력
        }
        
        scanner.close();
        //scanner.close: 자원 해제를 위한 것.
    }
}

//기초-2.등차수열

// don't place package name. 

import java.io.*;

import java.util.*; 

// don't change 'Main' class name and  'public' accessor. 

public class Main {
    public static void main(String[] args) throws IOException { 

        Scanner scanner = new Scanner(System.in); 

        String input = scanner.nextLine(); 

        String[] parts = input.split(" ");

        int A = Integer.parseInt(parts[0]);  
        int B = Integer.parseInt(parts[1]);  
        int N = Integer.parseInt(parts[2]); 

        //Integer.parseInt(String s): 문자열을 int타입으로
        //Integer.toString(int i): 정수를 문자열로
        //Integer.valueOf(String s): 문자열은 정수 객체로
        //Integer.valueOf(int i): int를 Integer로 (int:기본형 데이터 타입,객체x, Integer: 래퍼 클래스, int를 객체로 감쌈)?????????????
        //Integer.MAX_VALUE
        //Integer.MIN_VALUE
        //Integer.compare(int x, int y): 왼크 1 같 0 오크 -1
        //Integer.bitCount(int i): 2진수 변환후 1의 개수 반환
        //Integer.toBinaryString(int i): 2진수 문자열로 반환
        //Integer.toHexString(int i): 16진수 문자열로 반환
        //Integer.toOctalString(int i): 8진수 문자열로 반환

        //Double.parseDouble(String s)
        //Float.parseFloat(String s)
        //Boolean.parseBoolean(String s)

        int result = A + (N - 1) * B;

        System.out.println(result);
        
        scanner.close();
    }
}