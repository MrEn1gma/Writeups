package p000;

/* renamed from: Inner */
public class Inner {
    public static String decrypt(String str) {
        int i = 0;
        String upperCase = "NUKRPFUFALOXYLJUDYRDJMXHMWQW".toUpperCase();
        String str2 = "";
        for (int i2 = 0; i2 < upperCase.length(); i2++) {
            str2 = str2 + ((char) ((((upperCase.charAt(i2) - str.charAt(i)) + 26) % 26) + 65));
            i = (i + 1) % str.length();
        }
        return str2;
    }

    public static String encrypt(String str, String str2) {
        int i = 0;
        String upperCase = str.toUpperCase();
        String str3 = "";
        for (int i2 = 0; i2 < upperCase.length(); i2++) {
            str3 = str3 + ((char) ((((upperCase.charAt(i2) - 'A') + (str2.charAt(i) - 'A')) % 26) + 65));
            i = (i + 1) % str2.length();
        }
        return str3;
    }

    public void keep() {
    }
}