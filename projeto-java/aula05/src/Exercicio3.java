// Escreva um programa para ler 3 valores inteiros (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.


public class Exercicio3{
    public static void main(String[] args) {
        int num1, num2, num3, menor_num, maior_num, meio;

        num1 = 9;
        num2 = 9;
        num3 = 8;

        maior_num = Math.max(Math.max(num1, num2), num3);
        menor_num = Math.min(Math.min(num1, num2), num3);
        meio = num1 + num2 + num3 - menor_num - maior_num;

        System.out.println("Valores em ordem crescente:");
        System.out.println(menor_num + ", " + meio + ", " + maior_num);

    }
}