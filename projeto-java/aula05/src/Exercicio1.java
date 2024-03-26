// Crie um algoritmo que verifique se um número é positivo, negativo ou igual a zero. 

import java.util.Scanner;

public class Exercicio1 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        String saida = " ";
        
        System.out.println("Digite um número inteiro: ");
        int num = entrada.nextInt();
        
        
        
        if(num > 0){
            saida = "POSITIVO";
        }else if(num < 0){
            saida = "NEGATIVO";
        }else{
            saida = "IGUAL A ZERO";
        }

        System.out.println("O número " + num + " é " + saida);
        entrada.close();
    }
}
