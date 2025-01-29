import java.util.Scanner;
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Random rand = new Random();

        System.out.println("Por favor, digite o número da Agência !");
        String Agencia = sc.nextLine();
        System.out.println("Por favor, digite o nome");
        String NomeCliente = sc.nextLine();
        System.out.println("Por favor, digite o número da conta !");
        Integer NumeroConta = sc.nextInt();
        double Saldo = 100 * (1000000 - 100) * rand.nextDouble();

        System.out.printf("Olá %s, obrigado por criar uma conta em nosso banco, sua agência é %s, conta %d e seu saldo %.2f já está disponível para saque.", NomeCliente, Agencia, NumeroConta, Saldo);

        sc.close();
    }
}