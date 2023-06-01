
public class TesteCondiciona {

    public static void main(String[] args) {
    System.out.println("Testando Condicionais");        
    int idade = 20;
    int quantidadePessoas = 3;
    if(idade >= 18) {
        System.out.println("Voce é maior de idade");
        System.out.println("Seja bem vindo!");
    } else {
        if(quantidadePessoas>=2){
        System.out.println("Voce é novo mas ta acompanhado");
    } else {
        System.out.println("Voce nao entra!");
    }
    }
    
    //if(idade <= 18) 
      //  System.out.println("Voce é de menor!");

    }
}