from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap  = 10,
)


text = """
My name is Amna Afzal. I am 22 year old.    
Code,Symbol,Name
BGN,лв.,Bulgarian lev
BHD,.د.ب,Bahraini dinar
BIF,Fr,Burundian franc
BMD,$,Bermudian dollar
BND,$,Brunei dollar
BOB,Bs.,Bolivian boliviano

BRL,R$,Brazilian real
BSD,$,Bahamian dollar
BTC,฿,Bitcoin
BTN,Nu.,Bhutanese ngultrum
BWP,P,Botswana pula
BYR,Br,Belarusian ruble (old)'
BYN,Br,Belarusian ruble
BZD,$,Belize dollar
CAD,$,Canadian dollar
CDF,Fr,Congolese franc
CHF,CHF,Swiss franc
CLP,$,Chilean peso
CNY,¥,Chinese yuan
COP,$,Colombian peso
CRC,₡,Costa Rican colón
CUC,$,Cuban convertible peso')
CUP,$,Cuban peso
CVE,$,Cape Verdean escudo
CZK,Kč,Czech koruna
DJF,Fr,Djiboutian franc
DKK,DKK,Danish krone
DOP,RD$,Dominican peso
DZD,د.ج,Algerian dinar
EGP,EGP,Egyptian pound

ERN,Nfk,Eritrean nakfa
ETB,Br,Ethiopian birr
EUR,€,Euro

FJD,$,Fijian dollar
FKP,£,Falkland Islands pound')
GBP,£,Pound sterling
GEL,₾,Georgian lari
GGP,£,Guernsey pound
GHS,₵,Ghana cedi
GIP,£,Gibraltar pound
GMD,D,Gambian dalasi
IRR,﷼,Iranian rial
IRT,تومان,Iranian toman
ISK,kr.,Icelandic króna
JEP,£,Jersey pound
MGA,Ar,Malagasy ariary
MKD,ден,Macedonian denar
MMK,Ks,Burmese kyat
MNT,₮,Mongolian tögrög
MOP,P,Macanese pataca
MRU,UM,Mauritanian ouguiya
MUR,₨,Mauritian rupee
MVR,.ރ,Maldivian rufiyaa
MWK,MK,Malawian kwacha
MXN,$,Mexican peso
MYR,RM,Malaysian ringgit
MZN,MT,Mozambican metical
NAD,N$,Namibian dollar
NGN,₦,Nigerian naira
NIO,C$,Nicaraguan córdoba
NOK,kr,Norwegian krone
SBD,$,Solomon Islands dollar')
SCR,₨,Seychellois rupee
SDG,ج.س.,Sudanese pound
SEK,kr,Swedish krona
UZS,UZS,Uzbekistani som
VEF,Bs F,Venezuelan bolívar
VES,Bs.S,Bolívar soberano
VND,₫,Vietnamese đồng
VUV,Vt,Vanuatu vatu
WST,T,Samoan tālā
XAF,CFA,Central African CFA fr
XCD,$,East Caribbean dollar
XOF,CFA,West African CFA franc
XPF,Fr,CFP franc
YER,﷼,Yemeni rial
ZAR,R,South African rand
ZMW,ZK,Zambian kwacha
"""

chunks = splitter.split_text(text)

print("\nChunks:")

print(chunks[0])

print("\nChunks 1:")

print(chunks[1])