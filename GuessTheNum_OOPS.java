package Salil;

import java.util.Random;
import java.util.Scanner;


abstract class Player {
    protected String name;

    public Player(String name) {
        this.name = name;
    }

    
    public abstract int makeGuess();
}


class HumanPlayer extends Player {
    public HumanPlayer(String name) {
        super(name);
    }

   
    public int makeGuess() {
        Scanner scanner = new Scanner(System.in);
        System.out.print(name + ", enter your guess: ");
        return scanner.nextInt();
    }
}


class ComputerPlayer extends Player {
    public ComputerPlayer(String name) {
        super(name);
    }

    
    public int makeGuess() {
        
        Random random = new Random();
        return random.nextInt(100) + 1;
    }
}


class Game {
    private Player player;
    private int targetNumber;

    public Game(Player player) {
        this.player = player;
        
        Random random = new Random();
        this.targetNumber = random.nextInt(100) + 1;
    }

    
    public void play() {
        System.out.println("Welcome to the Number Guessing Game!");
        System.out.println("Try to guess the number between 1 and 100.");
        System.out.println("A project By Saaalil");

        int guess;
        boolean isCorrect = false;

        do {
            guess = player.makeGuess();
            System.out.println(player.name + " guesses: " + guess);

            if (guess == targetNumber) {
                System.out.println("Congratulations, " + player.name + "! You guessed the correct number.");
                isCorrect = true;
            } else if (guess < targetNumber) {
                System.out.println("Too low! Try again.");
            } else {
                System.out.println("Too high! Try again.");
            }
        } while (!isCorrect);
    }
}

public class SalilOOps {
    public static void main(String[] args) {
        
        HumanPlayer humanPlayer = new HumanPlayer("Player 1");
        ComputerPlayer computerPlayer = new ComputerPlayer("Computer");

        
        Game humanGame = new Game(humanPlayer);
        Game computerGame = new Game(computerPlayer);

        
        humanGame.play();
        computerGame.play();
    }
}
