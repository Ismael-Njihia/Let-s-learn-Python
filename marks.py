s1 = int(input("Enter the marks for science: "))
if(s1>99):
    print("impossible")
else:
    s2 = int(input("Enter the marks for mathematics: "))
    if (s2 > 99):
        print("impossible")
    else:
        s3 = int(input("Enter the marks for social studies: "))
        if (s3 > 90):
            print("impossible")
        else:
            s4 = int(input("Enter the marks for CRE: "))
            if (s4 > 30):
                print("impossible")
            else:
                s5 = int(input("Enter the marks for English: "))
                if (s5 > 50):
                    print("impossible")
                else:
                    s6 = int(input("Enter the marks for composition: "))
                    if (s6 > 50):
                        print("impossible")
                    else:
                        s7 = int(input("Enter the marks for kiswahili: "))
                        if (s7 > 50):
                            print("impossible")
                        else:
                         s8 = int(input("Enter the marks for Insha: "))
                         if (s8 > 50):
                             print("impossible")
                         else:
                             Geng = ((s6 / 40) * 50) + s5
                             Gkis = ((s8 / 40) * 50) + s7
                             Gsoc = ((s3 + s4) / 90) * 100
                             total = s1 + s2 + Gsoc + Geng + Gkis

                             if (total > 500):
                                 print("Nullified")
                             else:
                                 print(total)
                                 print(Geng)
                                 print(Gkis)


