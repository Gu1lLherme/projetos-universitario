// 4.Escreva uma função que receba 3 números inteiros e retorne o menor número.

public class Exercicio4 {
    static int menorNumero(int num1, int num2, int num3){
        return Math.min(Math.min(num1, num2), num3);
    }


    public static void main(String[] args) {
        int resultado = menorNumero(5, 1, 6);
        System.out.println("Menor número " + resultado);
    }
}

    

