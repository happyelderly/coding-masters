/* A ȸ�� �ѹ��μ��� �����մϴ�. �߿��� ������ ��� ����ִ� ��ǻ���� ��й�ȣ�� ��Ծ��� �����Դϴ�.
������ å�󿡴� �����ڰ� ���� ��Ʈ�� ��� ������ �����ֽ��ϴ�. ������ ������ �̷��մϴ�.
'��й�ȣ�� �������� ���ϸ�, ��ǻ�� ȭ�鿡�� �� �� �Ϸ��� ���ڵ��� �־����ϴ�. �� ��ǻ�� ȭ�鿡�� ���ĺ� c������ ���ĺ� ���ڿ��� ��й�ȣ�Դϴ�.'
�Ӹ��� ���� ��븮�� �ٷ� ���ظ� �ϰ� ��ȣ�� Ǯ�����ϴ�. �̶� ��븮�� ����� ����� ���α׷����� �ۼ��ϼ���. */


import java.io.*;
import java.util.*; 

public class Main {
    public static void main(String[] args) throws IOException { 
        
        Scanner scanner = new Scanner(System.in); 

        // ���� ��� ���� ���ٷ� �Է¹޾Ƽ� ���ڿ��� ����
        String a = scanner.nextLine();
        
        // ���� �������� ���ڿ� ������
        String[] b = a.split(" ");
        
        // �迭 ���� ���ϰ� �ϱ� ���� StringBuilder �ҷ�����
        StringBuilder result = new StringBuilder();
        
        // c�� �߰ߵǱ� ������ stringbuilder�� ���� �߰�
        for(int i=0 ; i<b.length ; ++i){
            result.append(b[i]).append(" ");
            if(b[i].equals("c")){
                break;
            }
        }
        
        // �������� ���� ���� ���� �� ���
        System.out.println(result.toString().trim());

    }
}