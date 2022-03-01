import regex

obfuscated_script = open("chall.bat", "r").readlines() # Your obfuscated file here

with open("oldschool_deobfuscated.bat", "w") as f:
    # First, I scan all function, if match line like: %TdapAUb%g%dhVMYqNn%%uPKf%o%kMZB%%ZMSLo%t%QnP%%ych%o%mOxct% :PPbpns
    # It will skipped the inside, Else if it match line like: :PPbpns
    # It will keep the next line
    # Because of RegEx does not match the first line so i add them.
    join_org_script = str("".join(obfuscated_script))
    f.write("@shift /0\n")
    fixed_code1 = []
    fixed_code2 = []
    """
    ^%.*:[A-Za-z]+ mean: match all lines that conatain % in the first line and the last line contain like :abcxyz
    ^:[A-Za-z]+[\n|\r|\r\n].+ mean: match all lines that contain like :abcxyz and match the next line
    """
    match_func = regex.findall(r"(^%.*:[A-Za-z]+|^:[A-Za-z]+[\n|\r|\r\n].+)", join_org_script, regex.MULTILINE)
    fc = [str(idx_func).split("\n") for idx_func in match_func]
    fixed_code1 = [str(out) + "\n" for i in fc for out in i]
    #print(fixed_code1)
    """
    I filtered some special function so that it can be removed correctly.
    scan_uc => scan unused code
    """
    join_script = str("".join(fixed_code1))
    for idx_fixed_code1 in fixed_code1:
        scan_uc = regex.findall(r"(:[A-Za-z]+)", idx_fixed_code1, regex.MULTILINE)
        for idx_scan_uc in scan_uc:
            sc = str(idx_scan_uc)
            if((":ll" in sc) or (":good" in sc) or (":bad" in sc)):
                continue
            
            scan_uc_all = regex.findall(sc, join_script, regex.MULTILINE)
            count = len(scan_uc_all)
            if(count == 2):
                idx_fixed_code1 = ""
        fixed_code2.append(idx_fixed_code1)
        
    """
    The next step I'll remove unused variables like %owhgwhg%
    """
    join_script1 = str("".join(fixed_code2))
    for idx_fixed_code2 in fixed_code2:
        scan_uc1 = regex.findall(r"(%[A-Za-z]+%)", idx_fixed_code2, regex.MULTILINE)
        for idx_scan_uc1 in scan_uc1:
            sc1 = str(idx_scan_uc1)
            # These variables are important so I keep them.
            if(("%length%" in sc1) or ("%out%" in sc1) or ("%pass%" in sc1) or ("%result%" in sc1) or ("%n%" in sc1) or 
               ("%t%" in sc1) or ("%A%" in sc1) or ("%B%" in sc1) or ("%C%" in sc1) or ("%D%" in sc1) or 
               ("%E%" in sc1) or ("%F%" in sc1) or ("%G%" in sc1) or ("%H%" in sc1) or ("%I%" in sc1) or 
               ("%J%" in sc1) or ("%K%" in sc1) or ("%L%" in sc1) or ("%M%" in sc1) or ("%N%" in sc1) or 
               ("%Z%" in sc1) or ("%P%" in sc1) or ("%Q%" in sc1) or ("%R%" in sc1) or ("%S%" in sc1) or 
               ("%T%" in sc1) or ("%U%" in sc1) or ("%V%" in sc1) or ("%W%" in sc1) or ("%X%" in sc1) or 
               ("%AA%" in sc1) or ("%BB%" in sc1) or ("%CC%" in sc1) or ("%DD%" in sc1) or ("%EE%" in sc1) or 
               ("%FF%" in sc1) or ("%GG%" in sc1) or ("%HH%" in sc1) or ("%II%" in sc1) or ("%JJ%" in sc1) or 
               ("%KK%" in sc1) or ("%LL%" in sc1) or ("%MM%" in sc1) or ("%NN%" in sc1) or ("%ZZ%" in sc1) or 
               ("%PP%" in sc1) or ("%dd%" in sc1)):
                continue
            scan_ucvar_all = regex.findall(sc1, join_script1, regex.MULTILINE)
            count1 = len(scan_ucvar_all)
            # if this variable has length = 1, That's an unused variable
            if(count1 == 1):
                idx_fixed_code2 = str(idx_fixed_code2).replace(sc1, "")
        f.write(idx_fixed_code2)