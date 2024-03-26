// 5.Faça uma função recursiva que permita somar os elementos de um vetor de inteiros.

public class Exercicio5 {
   
   
    public static void main(String[] args) {
        int[] vetor = {1, 2, 3, 4, 5};
        int soma = somaVetor(vetor, 0); // Chama a função recursiva
        System.out.println("A soma dos elementos do vetor é: " + soma);
    }

    public static int somaVetor(int[] vetor, int indice) {
        // Caso base: quando o índice ultrapassa o tamanho do vetor
        if (indice >= vetor.length) {
            return 0; // Retorna 0, pois não há mais elementos para somar
        } else {
            // Chamada recursiva: soma o elemento atual com a soma dos restantes
            int somaRestante = somaVetor(vetor, indice + 1);
            int somaAtual = vetor[indice];
            // Imprime o elemento atual para fins de demonstração
            System.out.println("Elemento atual: " + somaAtual);
            // Retorna a soma do elemento atual com a soma dos restantes
            return somaAtual + somaRestante;
        }
    }

    
}
