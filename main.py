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


def _build_comment(w: dict) -> str:
    codes = []

    if w["wind_deg"] is not None and w["wind_speed"] is not None:
        knots = int(round(w["wind_speed"] / 0.514444))
        codes.append(f"{w['wind_deg']:03d}/{knots:03d}")
    if w.get("gust"):
        knots = int(round(w["gust"] / 0.514444))
        codes.append(f"g{knots:03d}")

    temp_f = w["temp_c"] * 9.0 / 5.0 + 32.0
    codes.append(f"t{int(round(temp_f)):03d}")

    codes.append("r000p000")

    if w["humidity"] is not None:
        codes.append(f"h{w['humidity']:02d}")
    if w["pressure"] is not None:
        codes.append(f"b{int(round(w['pressure'] * 10)):05d}")

    weather_codes = "".join(codes)
    return f"{weather_codes}Estacion meteorologica APRS - {w['city']}"


def main():
    owm = OpenWeatherMap(OWM_API_KEY, CITY, COUNTRY) # type: ignore
    w = owm.get_all()
    comment = _build_comment(w)

    ais = aprslib.IS(
        CALLSIGN,
        passwd=PASSCODE, # type: ignore
        host="rotate.aprs2.net",
        port=14580
    )

    ais.connect()

    packet = f"{CALLSIGN}>APRS:={LATITUDE}/{LONGITUDE}_{comment}"
    ais.sendall(packet)
    print("Paquete de posicion enviado")

    status = f"{CALLSIGN}>APRS:>Estacion meteorologica APRS - {CITY}"
    ais.sendall(status)
    print("Paquete de estado enviado")


if __name__ == "__main__":
    main()
