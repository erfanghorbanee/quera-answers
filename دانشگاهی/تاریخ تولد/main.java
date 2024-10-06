import java.util.Scanner;
public class main {
	public static void main(String args[]) {
		
		Scanner sc = new Scanner(System.in);
		String tarikh=sc.nextLine();
		System.out.println("saal:"+tarikh.charAt(0)+ tarikh.charAt(1));
		System.out.println("maah:"+tarikh.charAt(2)+ tarikh.charAt(3));
		
	}

}
