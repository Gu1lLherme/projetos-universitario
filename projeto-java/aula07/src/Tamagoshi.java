/* Crie uma classe que modele um Tamagoshi (Bichinho Eletrônico): 

a. Atributos: Nome, Fome, Saúde e Idade 
b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade e imprimir (deve apresentar os valores de todos os atributos). 

Após a criação da classe, instancie dois Tamagoshis, altere seus atributos e depois os imprima.*/

public class Tamagoshi{

    // Atributos
    String nome;
    int fome;
    int saude;
    int idade;

    // Contrutor
    public Tamagoshi(String nome, int fome, int saude, int idade){
        this.nome = nome;
        this.fome = fome;
        this.saude = saude;
        this.idade = idade; 
    }
    // Métodos para alterar o estado do meu objeto

    public void alterarNome(String novoNome){
        this.nome = novoNome;
    }

    public void alterarFome(int novaFome){
        this.fome = novaFome;
    }

    public void alterarSaude(int novaSaude){
        this.saude = novaSaude;
    }
    
    public void alterarIdade(int novaIdade){
        this.idade = novaIdade;
    }

    // Metodo para imprimir os valores recebidos do construtor "Tamagoshi"
    public void imprimir(){
        System.out.println("Nome: " + this.nome);
        System.out.println("Fome: " + this.fome);
        System.out.println("Saude: "+ this.saude);
        System.out.println("Idade: "+ this.idade);
    }

    // Programa Principal
    public static void main(String[] args) throws Exception {
        // Declaração dos 2 objetos 
        Tamagoshi MeuPrimeiroTamagoshi = new Tamagoshi("Leandro", 4, 8, 2) ;
        Tamagoshi MeuSegundoTamagoshi = new Tamagoshi("Guilherme", 6, 4, 1);
        
        // Divisor 
        System.out.println("--------------------------------------------------------");
        //Imprimindo os atributos dos Tamagoshis  - Primeiro Tamagoshi 
        System.out.println("    Dados dos Tamagoshis sem Alteração dos atributos");
        // Divisor 
        System.out.println("--------------------------------------------------------");
        System.out.println("Primeiro Tamagoshi:" );
        MeuPrimeiroTamagoshi.imprimir();
        // Divisor 
        System.out.println("----------------------");
        // Segundo Tamagoshi
        System.out.println("Segundo Tamagoshi: ");
        MeuSegundoTamagoshi.imprimir();


        // Alteração de Atributos - Primeiro Tamagoshi
        MeuPrimeiroTamagoshi.alterarNome("Carlos");
        MeuPrimeiroTamagoshi.alterarFome(2);
        MeuPrimeiroTamagoshi.alterarSaude(10);
        MeuPrimeiroTamagoshi.alterarIdade(5);

        //Segundo Tamagoshi
        MeuSegundoTamagoshi.alterarNome("Débora");
        MeuSegundoTamagoshi.alterarFome(1);
        MeuSegundoTamagoshi.alterarSaude(9);
        MeuSegundoTamagoshi.alterarIdade(3);
        
        // Divisor 
        System.out.println("--------------------------------------------------------");
        //Imprimindo os Tamagoshis com Alteração de atributos - Primeiro Tamagoshi 
        System.out.println("    Dados dos Tamagoshis com Alteração dos atributos");
        // Divisor 
        System.out.println("--------------------------------------------------------");
        System.out.println("Primeiro Tamagoshi:" );
        MeuPrimeiroTamagoshi.imprimir();
        // Divisor 
        System.out.println("----------------------");
        // Segundo Tamagoshi
        System.out.println("Segundo Tamagoshi: ");
        MeuSegundoTamagoshi.imprimir();
        // Divisor 
        System.out.println("--------------------------------------------------------");

    }
}
