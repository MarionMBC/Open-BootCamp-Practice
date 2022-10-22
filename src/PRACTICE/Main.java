package PRACTICE;

public class Main {
    public static void main(String[] args) {
        Casa casa1 = new Casa(2,3,4);

        Vehiculo v1 = new Vehiculo();
        v1.setTipo("Carrera");
        System.out.println(v1.getTipo());
    }
}



class Casa {
    int puertas;
    int baños;
    int cuartos;

//    Constructor sin parámetros
    public Casa () {
        System.out.println("Hola");
    }

//    Constructor con parámetros
    public Casa (int puertas, int baños, int cuartos) {
        this.puertas = puertas;
        this.baños = baños;
        this.cuartos = cuartos;
        System.out.println(this.puertas);
    }
}

//Privacidad, Abstracción y encapsulación

//Propiedades privadas y públicas
//Una propiedad privada solo se puede usar dentro de la clase
//Una pública se puede instanciar desde fuera de la clase


//Encapsulación
class Vehiculo {
    private String tipo;
    private int vMaxima;
    private int vMinima;

    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

    public int getvMaxima() {
        return vMaxima;
    }

    public void setvMaxima(int vMaxima) {
        this.vMaxima = vMaxima;
    }

    public int getvMinima() {
        return vMinima;
    }

    public void setvMinima(int vMinima) {
        this.vMinima = vMinima;
    }

    public Vehiculo (){
    }


}



// Atributos con Boolean

class Computadora {
    boolean i5;

    public boolean isI5() {
        return i5;
    }

    public void setI5(boolean i5) {
        this.i5 = i5;
    }
}


//Abstracción

abstract class ClaseAbstracta {
    private String nombre;

    ClaseAbstracta (String nombre) {
        this.nombre = nombre;
    }

    public String getNombre() {
         return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }


//    Las clases abstractas no pueden instanciarse ni pueden tener cuerpo en
//    sus métodos

    abstract public void generarToken();
    abstract public String obtenerToken();
}


class ClaseHija extends ClaseAbstracta {
    String mensaje;

    ClaseHija (String mensaje, String nombre) {
        super(nombre);
        this.mensaje = mensaje;
    }


    @Override
    public void generarToken() {

    }

    @Override
    public String obtenerToken() {
        return null;
    }
}
