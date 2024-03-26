/*1Escreva um algoritmo que atribua valores a variáveis num1, num2 e num3, calcule sua média na variável media e exiba para o usuário o resultado.*/
import java.util.Scanner;


public class Exercicio1 {
    public static void main(String[] args) {
        try (Scanner entrada = new Scanner (System.in)) {
            System.out.println("Digite um número inteiro");
            int num1 = entrada.nextInt();
            
            System.out.println("Digite +1 número: ");
            int num2 = entrada.nextInt();

            System.out.println("Digite outro número");
            int num3 = entrada.nextInt();

            int media = (num1 + num2 + num3) / 3;

            System.out.println("Média Geral dos valores informados: " + media);
        }

    }
}
