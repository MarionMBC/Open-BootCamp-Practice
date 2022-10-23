package EJERCICIO_TEMA9;

public class Trabajador extends Persona{
    double salario;

    public Trabajador (int edad, String nombre, String telefono, double salario) {
        super (edad, nombre, telefono);
        this.salario = salario;
    }

    public void setSalario (double salario) {
        this.salario = salario;
    }

    public double getSalario () {
        return salario;
    }

    @Override
    public String toString() {
        return super.toString() +
                "\nSalario: " + salario;
    }
}
