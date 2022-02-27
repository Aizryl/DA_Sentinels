import requests
class GSC():
 def SC(self):
  url = "http://192.168.84.128/zipper/"
  rq = requests.get(url)
  SC = rq.status_code
  print("************************************")
  print('Status Code:')
  print("\t*",SC)
  if (SC == 200 ):
    print(" Status Code 200 = OK ")
class Header():
 def Head(self):
  url = "http://192.168.84.128/zipper/"
  h = requests.head(url)
  print("Website Header")
  print("************************************")
  for a in h.headers:
    print("\t",a,":",h.headers[a])
  print("************************************")
class Mobile():
 def Mob(self):
  UAM = {
  'User-Agent' : 'Mobile'
  }
  url2 = 'http://httpbin.org/headers'
  RMA = requests.get(url2,headers=UAM)
  print(RMA.text)
  print("************************************")

if __name__ == "__main__":
 GSC.SC(self=GSC)
 Header.Head(self=Header)
 Mobile.Mob(self=Mobile)