package EJERCICIO_TEMA9;

public class Cliente extends Persona{
    private double credito;

    public Cliente (int edad, String nombre, String telefono, double credito) {
    super (edad, nombre, telefono);
    this.credito = credito;
    }


    public void setCredito (double credito) {
        this.credito = credito;
    }
    public double getCredito () {
        return credito;
    }


    @Override
    public String toString() {
        return super.toString() +
                "\nCredito: " + credito;
    }
}
