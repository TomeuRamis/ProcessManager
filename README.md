# ProcessManager
Python process manager

El programa principal comprova si hi ha fitxers a la carpeta Requests (processos pendents a executar) i
a la carpeta InProgress (processos en execució). En el cas que no hi hagi cap document a cap de les dues carpetes:
  -Genera 10 arxius amb una request cada un a la carpeta Requests
  -Llegeix tots els fitxers i llança un procés per a cada Request del tipus especificat (Ara mateix només llança processos tipus "fib")
  -Per a cada procés llançat enmagetzema el procés a un arxiu a la carpeta InProgress i elimina l'arxiu orginial de Requests
  -Comprova per tots els fitxers de InProgress l'estat en que es troben: 
    -Si el pid del procés no exsisteix (significa que el procés ha finatlizat), transporta l'arxiu de InProgress a Finished
    -Si es troba el pid (no ha acabat), no fa res
    
Si hi ha arxius a Requests o a InProgress no genera arxius, genera el processos de Requests (si n'hi ha) i
comprova l'estat dels de InProgress.
