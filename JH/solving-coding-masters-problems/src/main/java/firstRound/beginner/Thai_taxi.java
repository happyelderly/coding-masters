package firstRound.beginner;
import java.util.*;
public class Thai_taxi {

    static List<List<Integer>> graph;
    static boolean[] visited;

    public static void main(String[] args) {
        Thai_taxi main = new Thai_taxi();
        Scanner scanner = new Scanner(System.in);

        // 입력 받기
        int N = scanner.nextInt(); // 마을의 수
        int M = scanner.nextInt(); // 택시의 수

        graph = new ArrayList<>();
        for (int i = 0; i <= N; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < M; i++) {
            int u = scanner.nextInt(); // 마을 u
            int v = scanner.nextInt(); // 마을 v
            graph.get(u).add(v);
            graph.get(v).add(u); // 무향 그래프
        }

        visited = new boolean[N + 1];
        int taxiCount = 0;

        // 모든 마을을 방문하기 위해 DFS 수행
        for (int i = 1; i <= N; i++) {
            if (!visited[i]) {
                main.dfs(i);
                taxiCount++; // 새로운 연결 요소 발견 시 택시 수 증가
            }
        }

        System.out.println(taxiCount);
        scanner.close();
    }

    // DFS 메서드
    public void dfs(int node) {
        visited[node] = true;
        for (int neighbor : graph.get(node)) {
            if (!visited[neighbor]) {
                dfs(neighbor);
            }
        }
    }
}
