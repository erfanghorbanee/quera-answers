import java.util.*;

public class khar {
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		int l = sc.nextInt();
		int sum = 0;
		for (int i = 0; i < l; i++) {
			if (i % 2 == 0) {
				sum += a;
			} else
				sum += b;
		}
		System.out.print(sum);
	}

}
