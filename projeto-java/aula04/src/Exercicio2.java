/*2Crie um algoritmo que mostre o resultado exato de uma divisão entre números inteiros, a parte inteira da divisão e o resto da divisão. */
import java.util.Scanner;

public class Exercicio2 {
    public static void main(String[] args) throws Exception {
        Scanner entrada = new Scanner(System.in);  
        
        System.out.println("Digite o primeiro valor: ");
        int num1 = entrada.nextInt();

        System.out.println("Digite o segundo valor: ");
        int num2 = entrada.nextInt();

        double divisão = num1 / num2;
        int resto = num1 % num2;

        System.out.println("Resultado Divisão: " + divisão);
        System.out.println("Resultado Resto da Divisão: " + resto);


    }
}
