package T3;

public class MainTema8 {
    public static void main(String[] args) {
        Persona p1 = new Persona();
        p1.setEdad(21);
        p1.setNombre("Marion Bustamante");
        p1.setTelefono("98x8xx9x");
        System.out.println("Su nombre es: " + p1.getNombre());
        System.out.println("Su teléfono es: " + p1.getTelefono());
        System.out.println("Su edad es: "+ p1.getEdad());
    }
}
