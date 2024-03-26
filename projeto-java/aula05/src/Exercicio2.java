// Escrever Tabuada do 1 ao 10. Escreva os dez primeiros elementos (começo em 1) da tabuada de multiplicação, dos números 1 ao 10. 

public class Exercicio2 {
    public static void main(String[] args) {
        int resultado_multiplicação;
        
        for(int i=1; i <= 10; i++){
            System.out.println("===== TABUADA de " + i + " =====");
            for (int j=1; j<=10; j++){
                    resultado_multiplicação = i*j ;
                    System.out.println(i + " x " + j + "=" + resultado_multiplicação);
            }
            
            
        }

    }
}
