
import java.util.Scanner;

public class prime {
	public static void prime(int n) {
		int i, f = 0;

		if (n == 0 || n == 1) {

		} else {
			for (i = 2; i < n; i++) {

				if (n % i == 0) {

					f = 1;
					break;
				}
			}
			if (f == 0) {
				System.out.println(n);

			}
		}
	}

	public static void main(String args[]) {

		Scanner a = new Scanner(System.in);
		int n1 = a.nextInt();
		int n2 = a.nextInt();
		for (int n = n1; n <= n2; n++) {
			prime(n);

		}
	}
}// 2 adad gerfte va adad haie avale beineshan ra chap mikonad.