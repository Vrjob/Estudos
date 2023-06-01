
public class TestaConversao {

    public static void main(String[] args) {

        double salario = 1270.50;
        int valor = (int) salario;
        System.out.println(valor);

        //long numeroGrande = 77787878787878l;
        //short valorPequeno = 2121;
        //byte b = 123;

        double valor1 = 0.2;
        float valor2 = 0.1f;
        double total = valor1 + valor2;
        System.out.println(total);
    }
}