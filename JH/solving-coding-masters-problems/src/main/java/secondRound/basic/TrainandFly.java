package secondRound.basic;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class TrainandFly {

    public int solution(int[] input) {
        int x = input[0];
        int y = input[1];
        int z = input[2];
//
//         충돌 조건
//         거리가 같아져야 함( - 방향으로?)
//         속력 = 거리 / 시간
//         x 킬로미터
//         x 킬로미터의 반이 되는 순간 충돌 -> 그래서 그 "시간" 이? 로 접근해야 함
//         기차의 속력 : 시속 y킬로미터
//         거리 = 속력 * 시간
//        시간 = 거리 / 속력
//        충돌시간 = x / 2y
//         파리는 시속 z킬로미터
//        파리의 이동거리 = 시간 * 속력
//        * z
//         같은 시간이 흐를동안 기차는 y만큼 파리는 z만큼 움직이는 건데
//        기차가 충돌하기까지 걸리는 시간은 x / 2y 혹은 (x / 2) / y
//        (x / 2y) * z = 파리의 이동거리

        int tmp1 = 2 * y;
        int tmp2 = x / tmp1;
        int answer = tmp2 * z;
//        return ((x / 2 * y) * z);
//        return ((x / 2) * y) * z;
        return  answer;

        // 200 / 100 = 2
        // 2 * 75 = 150
    }

    public static void main(String[] args) throws IOException {
        TrainandFly main = new TrainandFly();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int[] input = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int answer = main.solution(input);
        bw.write(String.valueOf(answer));
        bw.flush();
    }
}
