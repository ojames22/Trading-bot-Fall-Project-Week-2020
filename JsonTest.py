message = {"stream":"AM.TSLA","data":{"ev":"AM","T":"TSLA","v":1430,"av":1126793,"op":624.35,"vw":630.396,"o":630.43,"c":630.15,"h":630.51,"l":630.15,"a":628.0756,"s":1607449440000,"e":1607449500000}}

#print(message["data"]["vw"])

price = message["data"]["vw"]

#print(price)

if float(price) > 630:
	print("High")
if float(price) < 630:
	print("Low")