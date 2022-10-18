import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        int numeroIf = 0;
        System.out.println("----------------------------------------------");
        System.out.println("Número positivo o negativo");
        Scanner sc1 = new Scanner(System.in);
        System.out.println("Ingrese un número: ");
        numeroIf = sc1.nextInt();
        if (numeroIf<0) {
            System.out.println("El número es negativo");
        }  else  {
            System.out.println("El número es positivo");
        }

        System.out.println("----------------------------------------------");
        System.out.println("Ciclo While");
        int numeroWhile = 0;
        while (numeroWhile<3) {
            System.out.println(numeroWhile);
            numeroWhile++;
        }

        System.out.println("----------------------------------------------");
        System.out.println("Ciclo Do While");
        numeroWhile = 0;
        do {
            System.out.println(numeroWhile);
            numeroWhile++;
        } while (numeroWhile<0);


        System.out.println("----------------------------------------------");
        System.out.println("Ciclo For");
        for (int numeroFor=0; numeroFor<=3; numeroFor++){
            System.out.println(numeroFor);
        }

        System.out.println("----------------------------------------------");
        System.out.println("Switch Case");
        String estacion = "";
        Scanner sc2 = new Scanner(System.in);
        System.out.println("Ingrese la estación del año: ");
        estacion = sc2.nextLine();

        switch (estacion){
            case "Primavera":
                System.out.println("Estación:" + estacion);
            break;
            case "Verano":
                System.out.println("Estación:" + estacion);
                break;
            case "Invierno":
                System.out.println("Estación:" + estacion);
                break;
            case "Otoño":
                System.out.println("Estación:" + estacion);
                break;
            default:
                System.out.println("Estación incorrecta, debe iniciar con mayúscula.");
        }

    }
}