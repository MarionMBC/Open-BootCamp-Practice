package EJERCICIO_TEMA9;

public class Main {
    public static void main(String[] args) {
        Cliente client1 = new Cliente(21, "Fredy Banegas", "8484848", 93423423.43);
        System.out.println(client1.toString());
        System.out.println("------------------------");
        Trabajador trabajador1 = new Trabajador(33, "Pedro Lopez", "56464656456", 65464564.33);
        System.out.println(trabajador1.toString());
    }
}
