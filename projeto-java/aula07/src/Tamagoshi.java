/*Crie uma classe que modele um Tamagoshi (Bichinho Eletrônico): 

a. Atributos: Nome, Fome, Saúde e Idade 
b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade e imprimir (deve apresentar os valores de todos os atributos). 

Após a criação da classe, instancie dois Tamagoshis, altere seus atributos e depois os imprima. */
public class Tamagoshi {
    
    String nome;
    int fome ;
    int saude ;
    int idade ;

    


    static void saida() {
        Tamagoshi MeuTamagoshi = new Tamagoshi();
        System.out.println("Nome: " + MeuTamagoshi.nome);
        System.out.println("Fome: " + MeuTamagoshi.fome);
        System.out.println("Saude: " + MeuTamagoshi.saude);
        System.out.println("Idade: " + MeuTamagoshi.idade);
    }




    public static void main(String[] args) {
        saida();
    }


}
