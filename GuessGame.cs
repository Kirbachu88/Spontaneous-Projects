using System;

namespace NumberGuess
{
    class GuessGame
    {
        static void Main(string[] args)
        {
            // Initialization
            int secret;
            int guess = 0;
            int chance = 10;

            // Game introduction
            Console.WriteLine("Guess the Number Game!");

            Console.Write("Enter maximum number to guess: ");
            int max = Convert.ToInt32(Console.ReadLine());

            // Generating secret number
            secret = Generate(max);

            // Optional: Print secret number for testing purposes
            // Console.WriteLine(secret);

            // Guessing game with decreasing chances
            do
            {
                Console.WriteLine($"{chance} guesses remaining");
                Console.Write("Enter Guess: ");
                guess = Convert.ToInt32(Console.ReadLine());
                // Converting it so many times must be a terrible way to do this

                // Hints for each guess
                if (guess < secret && chance > 1)
                {
                    Console.WriteLine("Higher!\n");
                }
                else if (guess > secret && chance > 1)
                {
                    Console.WriteLine("Lower!\n");
                }

                // Decreasing number of chances for each guess
                chance--;

            } while (guess != secret && chance > 0);

            // Game result
            if (guess == secret)
            {
                Console.WriteLine($"The secret number was {secret}! You win!");
            }
            else
            {
                Console.WriteLine($"The secret number was {secret}! You lose...");
            }

            Console.ReadLine();
        }

        static int Generate(int max)
        {
            int secret;
            System.Random random = new Random();
            secret = random.Next(0, max);
            return secret;
        }

    }
}
