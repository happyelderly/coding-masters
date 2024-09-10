//////////////////////////////////// Java ////////////////////////////////////
//기초-3.8진수와 16진수

import java.io.*;
import java.util.*; 

public class Main {
    public static void main(String[] args) throws IOException { 

        Scanner scanner = new Scanner(System.in); 
        int a = scanner.nextInt(); 

        String o = Integer.toHexString(a).toUpperCase();
        String x = Integer.toOctalString(a);

        System.out.println(x + ' ' + o); 
    }
}
//str.toUpperCase()
//str.toLowerCase()
//str.isEmpty()
//str.charAt(int index):특정 인덱스에 있는 문자 반환
//str.length(): 길이 반환
//str.substring(int beginIndex)
//str.substring(int beginIndex, int endIndex)
//str1.equalsIgnoreCase(String str1): 대소문자 무시 같은지 확인
//str.contains(CharSequence s): 특정 문자열을 포함 여부
//str.indexOf(String str1): 특정 문자 위치 찾ㄱ지
//str.lastIndexOf(String str1): 특정문자의 마지막 위치 찾기
//str.replace(String target, String replacement) 특정 문자열 교체
//str.replaceAll(String regex, String replacement) 정규 표현식에 맞는 문자열 모두 대체
//str.trim(): 양측 공백 제거
//str.split(String regex): 특정 구분자로 배열 반환
//str.matches(String regex): 정규표현식이 일치하는지 확인 여부
//str.startsWith(String prefix): 특정 문자열로 시작하는지 확인
//str.endsWith(String suffix): 특정 문자열로 끝나는지 확인
//str.isBlank(): 공백또는 비어있는지
//str.isEmpty(): 비어있는지
//String.join(CharSequence delimiter, CharSequence... elements) 특정 구분자로 여러 문자열 하나로 합침



//기초-4.아스키 코드
import java.io.*;
import java.util.*; 
public class Main {
    public static void main(String[] args) throws IOException { 
        Scanner scanner = new Scanner(System.in); 
        int a = scanner.nextInt(); 
        System.out.println((char)a); 
    }
}