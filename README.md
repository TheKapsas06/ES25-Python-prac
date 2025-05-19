Pythoni skripti ideed:
* Algarvu tuvastaja, kirjuta funktsioon `is_prime_number(number: int) -> bool`, mis võtab sisendiks täisarvu ja tagastab:
  * True, kui tegemist on algarvuga;
  * False, kui see ei ole algarv.

* Minimaalne müntide leidja. Funktsioon, mis leiab mitu münti on vaja ette antud summa moodustamiseks
  * Küsib täisarvulise summa, mida soov müntidega maksta
  * Arvutab, mitu münti on vaja selle moodustamiseks (5, 10, 20, 50)
  * Alati kastutatakse võimalikult vähe münte

* API endpoint, mis tagastab aadressilt `/uptime` serveri uptime.
* API endpoint, mis tagastab ketta kasutuse aadressilt `/disk-usage`. JSON põhi, mis peab tulema väljundist.
```
{
  "filesystem": "/dev/sdb1",
  "size": "100G",
  "used": "65G",
  "available": "35G",
  "use_percent": "65%",
  "mounted_on": "/"
}
```