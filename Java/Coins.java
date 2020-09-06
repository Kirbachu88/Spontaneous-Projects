import java.util.Scanner;
public class Coins {
	public static void main(String args[]) {
		Scanner console = new Scanner(System.in);
		System.out.println("This program converts cents into change.");
		System.out.println("Please type the number of cents you want converted into change.");
		System.out.println("Your number must be between 1 and 99.");
		int cents = console.nextInt();
		int numberOfQuarters = 0;
		int numberOfDimes = 0;
		int numberOfNickels = 0;
		int numberOfPennies = 0;

		do {
			if(cents >= 25) {
				numberOfQuarters++;
				cents = cents - 25;
			}
			else if(cents >= 10) {
				numberOfDimes++;
				cents = cents - 10;
			}
			else if(cents >= 5) {
				numberOfNickels++;
				cents = cents - 5;
			}
			else {
				numberOfPennies++;
				cents = cents -1;
			}
		} while(cents > 0);

		do {
			if(numberOfQuarters >= 1) {
				System.out.println("Quarter");
				numberOfQuarters--;
			}
			else if(numberOfDimes >= 1) {
				System.out.println("Dime");
				numberOfDimes--;
			}
			else if(numberOfNickels >= 1) {
				System.out.println("Nickel");
				numberOfNickels--;
			}
			else if(numberOfPennies >= 1) {
				System.out.println("Penny");
				numberOfPennies--;
			}
		} while(numberOfQuarters > 0 || numberOfDimes > 0 || numberOfNickels > 0 || numberOfPennies > 0);
	}
}
