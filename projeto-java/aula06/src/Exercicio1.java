// 1.Faça um algoritmo em JAVA que exiba data e hora atual.

// importação da biblioteca java.util. na função Date
import java.util.Date;

public class Exercicio1 {
    public static void main(String[] args) throws Exception {
        // Variavel dataHoje recebe o valor retornado do metodo Date()
        Date dataHoje = new Date();
        // Exibe a data atual no terminal
        
        System.out.println("Data atual: " + dataHoje );


    }
}
