#!/usr/bin/python
'''
[>]                WELCOME TO SpyPorte SOURCE CODE                 [<]
[-]----------------------------------------------------------------[-]
[>] Script: SpyPorte                                               [<]
[>] Job: Scan Ports And Find Open Ports In Servers Devices.etc...  [<]
[#] CodedBy: Oseid Aldary                                          [<]
[--------------------------------------------------------------------]
'''

## IMPOER LIB ##
#==============#
import optparse
import socket,datetime
from time import sleep
from sys import platform as useros
try:
   import json
except:
	print("[!] Error [ Json ] Is Not Exist !!!\n[*] Please Install It Using This Command: pip install simplejson")
	exit(1)
try:
   import urllib2
except:
	print("[!] Error [ Urllib2 ] Is Not Exist !!!\n[*] Please  reinstall your python, because it comes with python")
	exit(1)

#==============#

## COLORS ##
if useros == "linux" or useros == "linux2":
 rd = "\033[1;31m"
 gr = "\033[1;32m"
 yl = "\033[1;33m"
 bl = "\033[1;34m"
 pu = "\033[1;35m"
 cy = "\033[1;36m"
 wi = "\033[1;37m"
else:
 rd = ""
 gr = ""
 yl = ""
 bl = ""
 pu = ""
 cy = ""
 wi = ""
##########################

############# show time #############
                                    #
mytime = datetime.datetime.now()    #
hour = mytime.hour                  #
min = mytime.minute                 #
sec = mytime.second                 #######
timenow = "{}:{}:{}".format(hour,min,sec) #
###########################################


## CHECK INTERNET CONNECTION............

server = "www.google.com"

def check():
  try:
     host = socket.gethostbyname(server)
     conn = socket.create_connection((host, 80), 2)
     return True
  except:
	pass
  return False
checknet1 = check()
checknet2 = checknet1
checknet3 = checknet2

################ DONE!  ##########################

## Error Connect ##

def msgerror():
	print(rd + "\n[!]:Ops:"+yl+"You Not Connected To ["+rd+" INTERNET"+yl+" ]"+bl+"\n[*]"+gr+":"+wi+"Please Connect To [ "+rd+"INTERNET"+wi+" ] And Try Again "+rd+":)")
	exit()
###################

##########################################=>> MAKE TOOL OPTIONS <<=###########################################

parse = optparse.OptionParser("""
USAGE: python ./SpyPorte.py -S <serverIP OR website> [OPTIONS...]

OPTIONS:

	 -O <PORT>            ::> THIS OPTION FOR SCAN [SINGLE] PORT
	 -M <Many Port>       ::> THIS OPTION FOR SCAN [MANY] PORTS
	 -R <Range Port>      ::> THIS OPTION FOR SCAN [RANGE] PORTS
	 -T <Timeout>         ::> IF You Want Set Timeout For Connection close | Default=5s

EXAMPLES:

	./SpyPorte.py -S www.google.com -O 80
	./SpyPorte.py -S 192.168.1.1 -M 80,443,21,22,23,25,53
	./SpyPorte.py -S www.fb.com -R 1-1000
        ./SpyPorte.py -s 192.168.1.3 -O 80 -t 10

""",version='SpyPorte Version: 2.5')
################################### DONE! ###########################################

###################### MAKE MAIN AND FUNCTION #######################################

def main():
  parse.add_option("-S","-s","--server",dest="TARGET",type="string")
  parse.add_option("-O","-o","--one-port",dest="Oport",type="string")
  parse.add_option("-M","-m","--many-port",dest="Mport",type="string")
  parse.add_option("-R","-r","--range-port",dest="Rport",type="string")
  parse.add_option("-T","-t","--timeout",dest="timeout",type="string")
  parse.add_option("-V","-v",action="store_true",dest="version",default=False)
  (options,args) = parse.parse_args()
  if options.version:
	print("SpyPorte Version: 2.5")
  elif options.TARGET !=None and options.Oport !=None:
	target = options.TARGET
	port = options.Oport
	def servername():
	  try:
	     ser = socket.getservbyport(int(port))
	     return ser
	  except OSError:
	     return "TCP"
	  except socket.error:
             return "TCP"
	servername = servername()
	global checknet1
	if target =="127.0.0.1":
		checknet1 = True

	if checknet1 == True:
	 def checkser():
	   if target !="127.0.0.1":
            try:
	       ip = socket.gethostbyname(target)
	       return True
	    except:
		 pass
	    return False
	   else:
		return True
 	 if checkser() !=True:
		print(yl+"\n[!]:"+rd+"Error:["+yl+"404"+rd+"]"+wi+" SERVER Not Found"+rd+"!!")
		exit(1)
	 try:
	  ip = socket.gethostbyname(target)
          print(wi+"\n[*]:method: SINGLE-PORT=> [ {} ]".format(port))
          sleep(1.8)
	  print(wi+"[>]:ServerIP: {}".format(ip))
          try:
	   url = "http://ip-api.com/json/"
           reponse = urllib2.urlopen(url + str(ip) )
           name = reponse.read()
           labs = json.loads(name)
	   test = labs['regionName']
           print(rd+"INFO"+gr+":["+wi+str(ip)+gr+"]===:")
	   sleep(0.10)
           print(gr + "\t\t IP: " +wi+ labs['query'])
	   sleep(0.10)
           print(gr+ "\t\t Status: " +wi+ labs['status'])
           sleep(0.10)
           print(gr+ "\t\t Region: " +wi+ test)
           sleep(0.10)
           print(gr + "\t\t Country: " +wi+ labs['country'])
           sleep(0.10)
           print(gr + "\t\t City: " +wi+ labs['city'])
           sleep(0.10)
           print(gr + "\t\t ISP: "+wi + labs['isp'])
           sleep(0.10)
           print(gr + "\t\t Lat,Lon: "+wi + str(labs['lat']) + "," + str(labs['lon']))
           sleep(0.10)
           print(gr + "\t\t ZIPCODE: "+wi + labs['zip'])
           sleep(0.10)
           print(gr + "\t\t TimeZone: " +wi+ labs['timezone'])
           sleep(0.10)
           print(gr + "\t\t AS: " +wi+ labs['as'])
           sleep(0.10)
           print(pu+"===============================\n"+wi)
	  except:
		pass
	  sleep(0.60)
	  print(wi+"[$]:Start At: {}".format(timenow))
	  sleep(0.60)
          print(wi+"[#]:Checking.......")
          sleep(1.5)
	  con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	  if options.timeout !=None:
			timeout = options.timeout
			con.settimeout(int(timeout))
	  else:
		 	con.settimeout(5)
	  con.connect((ip,int(port)))
          print(bl + "\n[+]"+gr+":"+wi+"PORT["+gr+str(port)+wi+"/"+cy+servername+wi+"] <="+gr+"OPEN"+wi+"=>")
	 except KeyboardInterrupt:
			print(rd+"[CTRL+C]:"+yl+"Exiting"+rd+".....")
			sleep(2.5)
			exit()
         except socket.error:
               print(rd+"\n[-]"+wi+":PORT["+rd+str(port)+wi+"/"+yl+servername+wi+"] <="+rd+"CLOSE!"+wi+"=>")
         except:
               print(rd+"\n[!]"+yl+"[ERROR] Something Went Wrong..."+gr+"Try Again :)")
	       exit(1)
	 print(gr+"---------------------------------\n[$]"+wi+" Shutdown At: {}".format(timenow))
	else:
		msgerror()

  elif options.TARGET !=None and options.Mport !=None:
	target = options.TARGET
	port = options.Mport
	if "," in port:
	  ports = port.split(",")
	else:
		print(rd+"\n[!]"+yl+"[ERROR] Please Use"+gr+" ["+yl+" , "+gr+"]"+yl+" For Distinguish Ports"+gr+" Ex: "+yl+"22,80,23,25,135,445,21")
		exit(1)
	global checknet2
	if target =="127.0.0.1":
		checknet2 = True

	if checknet2 == True:
 	 def checkser():
	   if target !="127.0.0.1":
            try:
	       ip = socket.gethostbyname(target)
	       return True
	    except:
		 pass
	    return False
	   else:
		return True
 	 if checkser() !=True:
                print(yl+"\n[!]:"+rd+"Error:["+yl+"404"+rd+"]"+wi+" SERVER Not Found"+rd+"!!")
		exit(1)


	 ip = socket.gethostbyname(target)
	 print(wi+"\n[*]:method: MANY-PORT=> [ {} ]".format(port))
         sleep(1.8)
         print(wi+"[>]:ServerIP: {}".format(ip))
         try:
	   url = "http://ip-api.com/json/"
           reponse = urllib2.urlopen(url + str(ip) )
           name = reponse.read()
           labs = json.loads(name)
	   test = labs['regionName']
           print(rd+"INFO"+gr+":["+wi+str(ip)+gr+"]===:")
	   sleep(0.10)
           print(gr + "\t\t IP: " +wi+ labs['query'])
	   sleep(0.10)
           print(gr+ "\t\t Status: " +wi+ labs['status'])
           sleep(0.10)
           print(gr+ "\t\t Region: " +wi+ test)
           sleep(0.10)
           print(gr + "\t\t Country: " +wi+ labs['country'])
           sleep(0.10)
           print(gr + "\t\t City: " +wi+ labs['city'])
           sleep(0.10)
           print(gr + "\t\t ISP: "+wi + labs['isp'])
           sleep(0.10)
           print(gr + "\t\t Lat,Lon: "+wi + str(labs['lat']) + "," + str(labs['lon']))
           sleep(0.10)
           print(gr + "\t\t ZIPCODE: "+wi + labs['zip'])
           sleep(0.10)
           print(gr + "\t\t TimeZone: " +wi+ labs['timezone'])
           sleep(0.10)
           print(gr + "\t\t AS: " +wi+ labs['as'])
           sleep(0.10)
           print(pu+"===============================\n"+wi)
	 except:
		pass
	 sleep(0.60)
	 print(wi+"[$]:Start At: {}".format(timenow))
	 sleep(0.60)
         print(wi+"[#]:Checking.......")
         sleep(1.5)
	 for p in ports:
		        try:
			   servername = socket.getservbyport(int(p))
                        except socket.error:
			   servername = "TCP"
			except OSError:
			   servername = "TCP"
			try:
			   con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                           if options.timeout !=None:
                              timeout = options.timeout
                              con.settimeout(int(timeout))
                           else:
                                  con.settimeout(5)
			   con.connect((ip,int(p)))
                           print(bl + "\n[+]"+gr+":"+wi+"PORT["+gr+str(p)+wi+"/"+cy+servername+wi+"]"+wi+" <="+gr+"OPEN"+wi+"=>")
			except KeyboardInterrupt:
				print(rd+"[CTRL+C]:"+yl+"Exiting"+rd+".....")
				sleep(2.5)
				break
                        except socket.error:
                              print(rd+"\n[-]"+wi+":PORT["+rd+str(p)+wi+"/"+yl+servername+wi+"] <="+rd+"CLOSE!"+wi+"=>")
                        except:
                             print(rd+"\n[!]"+yl+"[ERROR] Something Went Wrong\033[1;31m !!!")
	 print(gr+"---------------------------------\n[$]"+wi+" Shutdown At: {}".format(timenow))

	else:
		msgerror()

  elif options.TARGET !=None and options.Rport !=None:
        target = options.TARGET
        port = options.Rport
        if "-" in port:
          ports = port.split("-")
	  if int(ports[0]) > int(ports[1]):
		print(rd+"\n[!] "+yl+"Wrong,The First Range Port"+gr+"["+rd+str(ports[0])+gr+"]"+yl+" Is Bigger Than Last Range Port"+gr+"["+rd+str(ports[1])+gr+"]"+rd+" !!!")
		exit(1)
        else:
                print(rd+"\n[!]"+yl+"[ERROR] Please Use"+gr+" ["+yl+" - "+gr+"]"+yl+" For Distinguish First Range to Last Range Ports "+gr+"Ex: "+yl+"1-50")
                exit(1)
	global checknet3
	if target =="127.0.0.1":
		checknet3 = True

        if checknet3 == True:
	 def checkser():
	   if target !="127.0.0.1":
            try:
	       ip = socket.gethostbyname(target)
	       return True
	    except:
		 pass
	    return False
	   else:
		return True
 	 if checkser() !=True:
		print(yl+"\n[!]:"+rd+"Error:["+yl+"404"+rd+"]"+wi+" SERVER Not Found"+rd+"!!")
		exit(1)
         ip = socket.gethostbyname(target)
         print(wi+"\n[*]:method: RANGE-PORT=> [ {} ]".format(port))
         sleep(1.8)
         print(wi+"[>]:ServerIP: {}".format(ip))
         try:
	   url = "http://ip-api.com/json/"
           reponse = urllib2.urlopen(url + str(ip) )
           name = reponse.read()
           labs = json.loads(name)
	   test = labs['regionName']
           print(rd+"INFO"+gr+":["+wi+str(ip)+gr+"]===:")
	   sleep(0.10)
           print(gr + "\t\t IP: " +wi+ labs['query'])
	   sleep(0.10)
           print(gr+ "\t\t Status: " +wi+ labs['status'])
           sleep(0.10)
           print(gr+ "\t\t Region: " +wi+ test)
           sleep(0.10)
           print(gr + "\t\t Country: " +wi+ labs['country'])
           sleep(0.10)
           print(gr + "\t\t City: " +wi+ labs['city'])
           sleep(0.10)
           print(gr + "\t\t ISP: "+wi + labs['isp'])
           sleep(0.10)
           print(gr + "\t\t Lat,Lon: "+wi + str(labs['lat']) + "," + str(labs['lon']))
           sleep(0.10)
           print(gr + "\t\t ZIPCODE: "+wi + labs['zip'])
           sleep(0.10)
           print(gr + "\t\t TimeZone: " +wi+ labs['timezone'])
           sleep(0.10)
           print(gr + "\t\t AS: " +wi+ labs['as'])
           sleep(0.10)
           print(pu+"===============================\n"+wi)
	 except:
		pass
         sleep(0.60)
	 print(wi+"[$]:Start At: {}".format(timenow))
	 sleep(0.60)
         print(wi+"[#]:Checking.......")
         sleep(1.5)
	 found = []
         for p in range( int(ports[0]) , int(ports[1])+1):
                        try:
                           servername = socket.getservbyport(int(p))
                        except socket.error:
                           servername = "TCP"
                        except OSError:
                           servername = "TCP"
                        try:
                           con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                           if options.timeout !=None:
                              timeout = options.timeout
                              con.settimeout(int(timeout))
                           else:
                                  con.settimeout(5)

                           con.connect((ip,int(p)))
                           print(bl + "\n[+]"+gr+":"+wi+"PORT["+gr+str(p)+wi+"/"+cy+servername+wi+"] <="+gr+"OPEN"+wi+"=>")
			   found.append(p)
			except KeyboardInterrupt:
				print(rd+"[CTRL+C]:"+yl+"Exiting"+rd+".....")
				sleep(2.5)
				exit(1)
                        except socket.error:
                              print(rd+"\n[-]"+wi+":PORT["+rd+str(p)+wi+"/"+yl+servername+wi+"] <="+rd+"CLOSE!"+wi+"=>")

                        except:
                              print(rd+"\n[!]"+yl+"[ERROR] Something Went Wrong \033[1;31m!!!")

	 if len(found) > 0:
	        print(rd+"---------------------------------\n[#]"+gr+" Result"+rd+" [#]\n")
	        print(gr+"[*] "+wi+"TARGET:"+bl+" {}\n".format(target)+gr+"[*]"+wi+" OPEN-PORT(S) Found:"+gr+" {}".format(found))
		print(gr+"[$]"+wi+" Shutdown At: {}".format(timenow))
	 else:
		print(gr+"---------------------------------\n[#]"+rd+" Result"+gr+" [#]\n")
                print(gr+"[*] "+wi+"TARGET: {}\n".format(target)+gr+"[*]"+wi+" OPEN-PORT(S):"+rd+" No Open Port(s) Found !! :(")
		print(gr+"[$]"+wi+" Shutdown At: {}".format(timenow))
                exit(1)
        else:
                msgerror()
  else:
	print(parse.usage)
	exit(1)


if __name__=="__main__":
	main()
##############################################################
##################### 		     #########################
#####################   END OF TOOL  #########################
#####################                #########################
##############################################################
#This Tool by Oseid Aldary
#Have a nice day :)
#GoodBye
