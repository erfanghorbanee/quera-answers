import java.util.Scanner;
public class moraba {
	public static void main(String args[]) {
		
		Scanner sc= new Scanner(System.in);
		int n= sc.nextInt();
		int i=0;
		int j=0;
		int h=0;
		int g=0;
		for(i=0;i<n;i++) {
			System.out.print("*");
	}
		System.out.println();
		
		for(j=0;j<n-2;j++) {
			System.out.print("*");
		for(h=0;h<n-2;h++) {
			System.out.print(" ");
		}
		System.out.println("*");
		}
		
		for(g=0;g<n;g++) {
			System.out.print("*");
	}

}
}
