import re

print("exchange_order_id\tclient_order_id\torder_gross_fill_notional\tpnl_per_fill_ntl_bps\tspread_captured\ttrade_notional")

with open("pikachu.previous.log", "r") as file:
    for line in file:
        match = re.search(r'FILL: exchange_order_id (\S+), client_order_id (\S+), order_ gross_fill_notional: ([\d.]+), pnl_per_fill_ntl_bps: ([\d.]+), spread_captured: ([\d.-]+)', line)
        if match:
            print("{'FILL': 'exchange_order_id %s', 'gross_fill_notional': '%s', 'pnl_per_fill_ntl_bps': '%s', 'spread_captured': '%s'}" % (match.group(1), match.group(3), match.group(4), match.group(5)))
