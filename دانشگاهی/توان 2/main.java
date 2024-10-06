import java.math.*;
import java.util.Scanner;
public class power {
	public static void h () {
		Scanner sc = new Scanner(System.in);
		int n=sc.nextInt();
		int i=0;
		while(true) {
			int tavan= (int) Math.pow(2, i);
			if(tavan>n) {
				System.out.println(tavan);
				break;
			}
			else i++;
			
			
		}
		return;
	}

}

