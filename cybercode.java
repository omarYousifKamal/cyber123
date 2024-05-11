import java.util.Scanner;

public class VulnerableCLI {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Welcome to the Vulnerable CLI!");
        System.out.println("Please enter your name:");
        
        String name = scanner.nextLine();
        
        // Vulnerability 1: Command Injection
        System.out.println("Hello, " + name + "! Please enter a command:");
        String command = scanner.nextLine();
        try {
            // This vulnerability allows arbitrary commands to be executed
            Runtime.getRuntime().exec(command);
        } catch (Exception e) {
            System.out.println("Error executing command: " + e.getMessage());
        }
        
        // Vulnerability 2: SQL Injection
        System.out.println("Please enter your username:");
        String username = scanner.nextLine();
        // This vulnerability allows malicious SQL queries to be injected
        String sqlQuery = "SELECT * FROM users WHERE username = '" + username + "'";
        System.out.println("Executing SQL query: " + sqlQuery);
        
        // Vulnerability 3: Integer Overflow
        System.out.println("Please enter a number:");
        int num1 = scanner.nextInt();
        System.out.println("Please enter another number:");
        int num2 = scanner.nextInt();
        // This vulnerability may lead to unexpected behavior or security flaws
        int result = num1 + num2;
        System.out.println("Result of addition: " + result);
        
        // Close the scanner
        scanner.close();
    }
}
