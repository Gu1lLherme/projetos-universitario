// 3.Faça um programa em que cria uma matriz de 3 x 3 elementos inteiros, depois
// multiplica cada elemento por 5 e imprime o resultado.
public class Exercicio3 {
    public static void main(String[] args) {
        
        //int[][] matriz = new int[3][3];
        int[][] myNumbers = { {1, 2, 3}, {5, 6, 7}, {8, 9, 10}};
        
        for(int i=0; i<3; i++){
            for(int j=0; j<3; j++){
                System.out.println(myNumbers[i][j] * 5);
            }
        }
    }
}
