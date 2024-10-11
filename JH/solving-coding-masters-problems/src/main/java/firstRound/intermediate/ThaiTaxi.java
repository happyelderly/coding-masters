package firstRound.intermediate;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

class Edge implements Comparable<Edge> {
    int from, to, cost;

    public Edge(int from, int to, int cost) {
        this.from = from;
        this.to = to;
        this.cost = cost;
    }

    @Override
    public int compareTo(Edge other) {
        return this.cost - other.cost;
    }
}
public class ThaiTaxi {
    // Union-Find 자료구조를 위한 배열
    static int[] parent;
    static int[] rank;

    // 부모 노드를 찾는 함수 (경로 압축)
    public int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    // 두 집합을 합치는 함수 (Union by Rank)
    public void union(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);

        if (rootX != rootY) {
            if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
        }
    }

    // 최소 비용 계산 함수
    public int minimumCostToConnectVillages(int N, int M, List<Edge> taxiInfo) {
        // 초기화
        parent = new int[N + 1];
        rank = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            parent[i] = i;
            rank[i] = 0;
        }

        // 간선을 비용 기준으로 오름차순 정렬
        Collections.sort(taxiInfo);

        int totalCost = 0;
        int edgesUsed = 0;

        // 크루스칼 알고리즘
        for (Edge edge : taxiInfo) {
            if (find(edge.from) != find(edge.to)) {
                union(edge.from, edge.to);
                totalCost += edge.cost;
                edgesUsed++;
                // 모든 마을이 연결된 경우
                if (edgesUsed == N - 1) {
                    break;
                }
            }
        }

        return totalCost;
    }

    public static void main(String[] args) {
        ThaiTaxi main = new ThaiTaxi();
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int M = scanner.nextInt();

        List<Edge> taxiInfo = new ArrayList<>();

        for (int i = 0; i < M; i++) {
            int a = scanner.nextInt();
            int b = scanner.nextInt();
            int c = scanner.nextInt();

            taxiInfo.add(new Edge(a, b, c));
        }

        // 결과 출력
        int minimumCost = main.minimumCostToConnectVillages(N, M, taxiInfo);
        System.out.println(minimumCost);
    }

}
