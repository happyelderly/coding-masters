package firstRound.middle;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
import java.util.Set;

public class FindingNumber {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 입력받기
        int N = sc.nextInt(); // 목표 숫자
        int K = sc.nextInt(); // 시작 숫자

        // 결과 출력
        System.out.println(bfs(N, K));

        sc.close();
    }

    public static int bfs(int N, int K) {
        Queue<int[]> queue = new LinkedList<>(); // 큐 생성 (현재 숫자, 이동 횟수)
        Set<Integer> visited = new HashSet<>(); // 방문한 숫자를 저장할 Set

        queue.add(new int[] {K, 0}); // 시작 숫자와 이동 횟수 (0회) 추가
        visited.add(K); // 시작 숫자 방문 처리

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int number = current[0];
            int count = current[1];

            // 목표 숫자에 도달하면 횟수 반환
            if (number == N) {
                return count;
            }

            // 세 가지 연산을 통해 새로운 숫자 탐색
            int[] nextNumbers = {number + 1, number - 1, number * 2};
            for (int next : nextNumbers) {
                if (next >= 0 && next <= 100000 && !visited.contains(next)) {
                    visited.add(next);
                    queue.add(new int[] {next, count + 1});
                }
            }
        }

        return -1; // 도달할 수 없을 경우 (이론상 도달 불가능한 경우는 없음)
    }
}
