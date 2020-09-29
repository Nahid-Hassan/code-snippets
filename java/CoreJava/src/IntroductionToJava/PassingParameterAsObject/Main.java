package IntroductionToJava.PassingParameterAsObject;

public class Main {
    public static void main(String[] args) {
        Human girl = new Human();
        girl.skinTone = "Pale";

        Human boy = new Human();
        boy.skinTone = "Light";

        Human baby = girl.produce(boy);
        System.out.println(baby.skinTone);
    }
}

class Human {
    String skinTone;
    Human anotherHuman;

    public Human produce(Human anotherHuman) {
        Human newBie = new Human();
        newBie.skinTone = this.skinTone + anotherHuman.skinTone;

        return newBie;
    }
}