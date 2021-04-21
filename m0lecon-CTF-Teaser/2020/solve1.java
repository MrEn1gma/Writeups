import java.io.*;
import java.util.*;

public class solve1{
    public static void main(String[] args) {
        int i = 0;
        String str = "EASYPEASY";
        String upperCase = "NUKRPFUFALOXYLJUDYRDJMXHMWQW".toUpperCase();
        String str2 = "";
        for (int i2 = 0; i2 < upperCase.length(); i2++) {
            str2 = str2 + ((char) ((((upperCase.charAt(i2) - str.charAt(i)) + 26) % 26) + 65));
            i = (i + 1) % str.length();
        }
        System.out.print("flag: ptm{" + str2 + "}");
    }
}