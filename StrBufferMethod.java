class StringBufferDemo {

    public static void main(String[] args) {
        StringBuffer sb = new StringBuffer("Java");

        sb.append("Programming");
        System.out.println(sb);

        sb.insert("Language ");
        System.out.println(sb);

        sb.reverse ();
        System.out.println(sb);
    }
}
