import java.util.Scanner;
public class main {
	public static void main(String args[]) {
		Scanner s1=new Scanner(System.in);
		
		int i,temp = 0;
		int n=s1.nextInt();
		for(i=0;i<n;i++) {
		
			int m= s1.nextInt();
			if(m>temp || m==temp) {
				temp=m;
			}
		}
		
		System.out.println(temp);
		
	}

}
