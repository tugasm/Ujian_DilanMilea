import requests

prov = requests.get(
    'https://raw.githubusercontent.com/LintangWisesa/Ujian_Fundamental_JCDS08/master/data/provinsi.json')
kodepos = requests.get(
    'https://raw.githubusercontent.com/LintangWisesa/Ujian_Fundamental_JCDS08/master/data/kodepos.json')
pv = prov.json()
kp = kodepos.json()


listkey = list(pv.keys())
listvalue = list(pv.values())
listkey2 = list(kp.keys())
listvalue2 = list(kp.values())

dilan = listkey[listvalue.index('BANTEN')]
milea = listkey[listvalue.index('JAWA BARAT')]

for i in range(len(listvalue2[listkey2.index(dilan)])):
    if listvalue2[listkey2.index(dilan)][i]['urban'] == 'SAMPORA':
        kodeposdilan = (listvalue2[listkey2.index(dilan)][i]['postal_code'])


for i in range(len(listvalue2[listkey2.index(milea)])):
    if listvalue2[listkey2.index(milea)][i]['urban'] == 'CITARUM':
        kodeposmilea = (listvalue2[listkey2.index(milea)][i]['postal_code'])


apikey = 'RA6dfOvYnLSNQdk0W0FwyWEvGjNRSIKSTlZqNRlq5UO8m3lSqcFO83VH4OLWJDtw'
urlpostcode = 'http://www.zipcodeapi.com/rest/'
datapostcode = requests.get(
    urlpostcode+apikey+'/distance.json/'+kodeposdilan+'/'+kodeposmilea+'/km')
hasilpostcode = datapostcode.json()
z = hasilpostcode['distance']

print(f'Kode Pos lokasi Dilan adalah {kodeposdilan} ')
print(f'Kode Pos lokasi Milea adalah {kodeposmilea}')
print(f'Jarak Dilan & Milea adalah {z} km')
