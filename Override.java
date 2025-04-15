class A {

    void show() {
        System.out.println("Parent");
    }
}

class B extends A {

    void show() {
        System.out.println("Child");
    }
}

class OverrideDemo {

    public static void main(String[] args) {
        A obj = new B();

        obj.show();
    }
}