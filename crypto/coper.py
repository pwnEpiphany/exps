from struct import pack,unpack
import zlib
import gmpy
 
def my_parse_number(number):
    string = "%x" % number
    erg = []
    while string != '':
        erg = erg + [chr(int(string[:2], 16))]
        string = string[2:]
    return ''.join(erg)
def extended_gcd(a, b):
    x,y = 0, 1
    lastx, lasty = 1, 0
    while b:
        a, (q, b) = b, divmod(a,b)
        x, lastx = lastx-q*x, x
        y, lasty = lasty-q*y, y
    return (lastx, lasty, a)
def chinese_remainder_theorem(items):
  N = 1
  for a, n in items:
    N *= n
  result = 0
  for a, n in items:
    m = N//n
    r, s, d = extended_gcd(n, m)
    if d != 1:
      N=N/n
      continue
    result += a*s*m
  return result % N, N

sessions=[{"c": 0xB1E7F916884F9D17DFFCB8EF1A93D61E3DA73E066CE8B71F09BB8EF61C833300CB472854FF642F540DB232DED17095F4FDDCA6CCCC27628EA781F546863FA431B9057FA7DC1AA41C127FB22B113E512B14926CA0C361DD6DAAEBC3F2E9CE51D012F40173CF88F07752CAAABA06AE53C4DBD559F50EED636A0A2E65D6BD835BD0, "e": 3, "n":0xDD1B58FF0DE86CD28DFFB60CC1EE0EFA3250D58264B3DA9CEAA5B5C17C728741F728C462C347DCB707BA7EE8672295F5A750C19D48AE23A32FC21E76F3188B85008E4EC1A66371BBB0825E558E876D80FA59E7099AF25B0B298131277E634772F24EE0ED1BACD3BA6F8D8E443D5AE16FAF6AA7DBAA59F91F763E4EAFD7D7F5CD},
{"c":0x9FEDDC9C122AA836E9A04FE9358A118B358C7BC6F3ABDE4E035E2BCB15B52950DB1D23449EA62F83406FB591ED39564FD0E2DAD0954156037BB32C9C23C49DA83E2E85BC09A9B6FD75E2F55129044FA0F996895E8BF5E53D88938E4A3366649E97961BE5B7B4095476D013D2E9F6FE75DC21295747BF371AE346355A5ADBD93F , "e": 3, "n":0x9A597210DA69760A66B063FA125DC17DC2038EC720CAE6D0B1599EC25B9A19F328BC55882EE9ED05FC9BD90276B0F7F1D227946FFD77081DF6E08976EBF57A3BB21AC13FE25A742A0C137E007BD8787A42683D81ADC28450051B44617C2081D5ACA3141DC2C848F1401CEA94DA7D11142BB2406306B299953D1C28259521EA11 },
{"c":0xD2611805B6839FD983F2C574BDAD1C50A4FB9FAB35F3BB643F90A9FBB0B84AF1D042E35E821564FCA783F1A2AF41349BB3E1C159B20EA6A0DB9E70597CB5C0780EF6CD78481AEAC0DF65A8DE35A8B5021FCE55332C5B2ADAEDCF80963BD6FFF773CAB55D73637C9BD667148FB1359782D38C41CBB43FA5FD56F424F842D8683D , "e": 3, "n":0x4A6972B03F96CC30DE3F60DA66C71842E600320964A69EC818047B219506A12F3E4D522B40B10EB3F630A068C908186F29BF782360E35262A4CECCAD554F57D1721DB61B260AC6C5FBCB020AC326562048B0FC9270AFE51C63F5F27A9A3CFD78B5971D5CBF7FBF20E23CA7B429121BD0BB9AE0552D6907C659E2B450B01675D7 }]
data = []
for session in sessions:
    e=session['e']
    n=session['n']
    msg=session['c']
    data = data + [(msg, n)]
print ("Please wait, performing CRT")
x, n = chinese_remainder_theorem(data)
e=session['e']
realnum = gmpy.mpz(x).root(e)[0].digits()
print (my_parse_number(int(realnum)).encode("UTF-8").hex())
