from rates_parser import RatesParser

rp = RatesParser("exchange.json")

print(f"{rp.date}: {rp.base_rate} to GBP - {rp.gbp}")

