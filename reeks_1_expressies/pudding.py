bought = int(input())
price = float(input())
barcodes = int(input())
miles = int(input())

print(f"Phillips spendeerde ${round(bought * price, 1)} voor {bought // barcodes * miles} frequent flyer mijlen.")