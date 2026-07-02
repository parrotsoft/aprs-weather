import logging
logging.basicConfig(level=logging.DEBUG)
import os
import aprslib
from dotenv import load_dotenv

load_dotenv()

CALLSIGN = os.getenv("CALLSIGN")
PASSCODE = os.getenv("PASSCODE")
LATITUDE = os.getenv("LATITUDE")
LONGITUDE = os.getenv("LONGITUDE")

comment = "Barranquilla 31°C"

def main():
    ais = aprslib.IS(
        CALLSIGN,
        passwd=PASSCODE, # type: ignore
        host="rotate.aprs2.net",
        port=14580
    )

    ais.connect()

    packet = f"{CALLSIGN}>APRS:={LATITUDE}/{LONGITUDE}>{comment}"

    ais.sendall(packet)

    print("Paquete enviado...")


if __name__ == "__main__":
    main()
