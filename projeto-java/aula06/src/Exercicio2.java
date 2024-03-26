//2.Faça um algoritmo em JAVA que calcule a raiz quadrada de um número.

import java.util.Scanner;;
public class Exercicio2 {
    public static void main(String[] args) {

        System.out.println("Digite um número: ");

        Scanner entrada = new Scanner(System.in);
        int raiz = entrada.nextInt();
        double resultado = Math.sqrt(raiz); 

        System.out.println("Raiz Quadrada de: " + resultado);
        
        entrada.close();
    }
}
