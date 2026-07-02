import logging
logging.basicConfig(level=logging.DEBUG)
import os
import aprslib
from dotenv import load_dotenv
from weather import OpenWeatherMap

load_dotenv()

CALLSIGN = os.getenv("CALLSIGN")
PASSCODE = os.getenv("PASSCODE")
LATITUDE = os.getenv("LATITUDE")
LONGITUDE = os.getenv("LONGITUDE")
CITY = os.getenv("CITY")
COUNTRY = os.getenv("COUNTRY")
OWM_API_KEY = os.getenv("OWM_API_KEY")


def main():
    owm = OpenWeatherMap(OWM_API_KEY, CITY, COUNTRY) # type: ignore
    temp = owm.get_temperature_celsius()
    comment = f"{CITY} {temp:.0f}°C"

    ais = aprslib.IS(
        CALLSIGN,
        passwd=PASSCODE, # type: ignore
        host="rotate.aprs2.net",
        port=14580
    )

    ais.connect()

    packet = f"{CALLSIGN}>APRS:={LATITUDE}/{LONGITUDE}_{comment}"

    ais.sendall(packet)

    print("Paquete enviado...")


if __name__ == "__main__":
    main()
