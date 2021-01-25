#taxi_id;  indulas;              idotartam;  tavolsag;  viteldij;   borravalo;    fizetes_modja
#5240   ;  2016-12-15 23:45:00;  900;        2,5;          10,75;   2,45;          bankkártya

f = open("Fuvar.csv")
f.readline()

fuvar = [sor.strip().split(';') for sor in f]

print(f"3. Feladat: {len(fuvar)}")