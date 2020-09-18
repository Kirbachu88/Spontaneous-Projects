import java.util.Scanner;

public class Coins {
	public static void main(String args[]) {
    String[] coinNames  = new String[] {"Toonie", "Loonie", "Quarter", "Dime", "Nickel", "Penny"};
    int[] coinCount = new int[] {0, 0,   0,  0,   0,   0};
    int[] centValue  = new int[] {200, 100, 25, 10, 5, 1};

    int dollars = inputAmount();
    findChange(dollars, coinCount, centValue);
    printChange(coinNames, coinCount);
    }

  public static int inputAmount() {
    Scanner console = new Scanner(System.in);
		System.out.println("This program converts a dollar amount into change.");
		System.out.println("Please type the amount of money you want converted into change.");
		System.out.print("$");
		double inputAmount = console.nextDouble();
    int dollars = (int)(inputAmount*100);
    // Converting to int because 11 cents would result in 1 dime otherwise
    return dollars;
  }

  public static void findChange(int dollarAmount, int[] numberOfCoins, int[] centValue){
    int coinTally = 0;

    for (int i = 0; i < numberOfCoins.length; i++){
      while(dollarAmount >= centValue[i]) {
        dollarAmount -= centValue[i];
        numberOfCoins[i] = ++coinTally;
      }
      coinTally = 0;
    }
  }

  public static void printChange(String[] coinNames, int[] numberOfCoins) {
    for (int i = 0; i < numberOfCoins.length; i++){
    System.out.println(numberOfCoins[i] + " " + coinNames[i]);
    }
  }
}