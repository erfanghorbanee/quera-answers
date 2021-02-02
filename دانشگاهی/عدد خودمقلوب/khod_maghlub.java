import java.util.*;

public class khod_maghlub {
	public static void main(String args[]) {

		Scanner a = new Scanner(System.in);
		int n = a.nextInt(), tul = 0;
		int m = n;

		while (0 < n) {
			n = n / 10;
			tul = tul + 1;
		}

		int[] Array = new int[tul];
		for (int i = m; i > 0; i = i / 10) {
			int g = 0;
			Array[tul - 1] = i % 10;
			tul--;
		}
		int j = Array.length - 1,h=0;
		for (int i = 0; i < Array.length; i++) {
			if (Array[i] != Array[j]) {
				System.out.print("NO");
				h=1;
				break;
			} else
				j--;

		}
		if (h==0) {
			System.out.print("YES");
			
		}

	}

}
