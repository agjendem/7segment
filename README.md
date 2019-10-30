Hardware:
7-segment:
    * Guide: https://learn.sparkfun.com/tutorials/large-digit-driver-hookup-guide/all
    * Kan testes med ./7segmentdisplay.py
    * Må ha ekstern 12v strømforsyning på GRØNN inngang. Vær nøye med hvor jord kobles.
    * Utgang er 6 pins nær grønn inngang. Fra ytterst på krettskort:
        * 12v (rød, for å drive LED-lysene i segmentene)
        * 5v (rød, for å drive shift-register-brikke på displayene)
        * SER (orange, GPIO: 14/TXD)
        * CLK (grønn, GPIO: 11/CLK)
        * LATch (hvit, GPIO: 13, brukes for å signalisere når vi skal bytte til neste tall)
        * jord (blå)
    
Led-strip:
    * Bibliotek: https://github.com/jgarff/rpi_ws281x
    * Guide: https://dordnung.de/raspberrypi-ledstrip/ws2812
    * Må ha 5v strømforsyning på BLÅ inngang. Vær nøye med hvor jord kobles.
    * Utgang er 3 pins nær blå inngang. Fra ytterst på kretskort:
        * jord
        * signal (GPIO/PWM: 18)
        * 5v (for å drive led-lysene på stripen(e))
    * Bibliotek er installert eksplisitt med "sudo pip3", for å finnes når den kjøres med sudo igjen. Det må til pga. tilgang til minne som brukes til stripene.
    ```
    sudo pip3 install rpi-ws281x
    sudo ./strandtest.py
    ```
