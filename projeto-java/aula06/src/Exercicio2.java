//2.Faça um algoritmo em JAVA que calcule a raiz quadrada de um número.




4.Escreva uma função que receba 3 números inteiros e retorne o menor número.


5.Faça uma função recursiva que permita somar os elementos de um vetor de inteiros.*/

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
