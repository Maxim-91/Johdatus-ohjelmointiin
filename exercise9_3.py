import functions as f

# Tee funktio nimeltä magazine_serial_check(serial),
# joka vastaanottaa parametrina vain ISSN-sarjanumeron (tekstinä),
# ja tarkistaa onko se oikeassa muodossa.

serial = input("Anna ISSN-sarjanumero:\n")
if f.magazine_serial_check(serial):
    # Jos sarjanumero on oikeassa muodossa, tulosta "Oikea ISSN"
    print("Oikea ISSN.")
else:
    # Jos sarjanumero ei ole oikeassa muodossa, tulosta "Väärä ISSN"
    print("Väärä ISSN.")
