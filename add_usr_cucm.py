import requests ##the requests module allows you to send HTTP requests using Python
import csv ##implements classes to read and write tabular data in CSV format
## The following 3 lines suppresses/ignores the insecure request warnings for unverified https requests
import warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore', InsecureRequestWarning)

keys=['UserID', 'Fname', 'Lname'] ## Create list of headers in Users.csv file
r=open('Users.csv') ## Reading the CSV file
read=csv.DictReader(r)
for DevName in read: ## iterate through each row in the file
    values=list(map(DevName.get, keys)) ## Building the List of the values for each header for a particular row. For first user it will look like values=[User1, User1, LUser1]
## Below is the SOAP request that we will send to CUCM to add users with given details "firstName, lastName, userid"

soaprequest="""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns="http://www.cisco.com/AXL/API/11.5">
<soapenv:Header/>
<soapenv:Body>
<ns:addUser>
<user>
<firstName>""" +values[1]+ """</firstName>
<lastName>""" +values[2]+ """</lastName>
<userid>""" +values[0]+ """</userid>
</user>
</ns:addUser>
</soapenv:Body>
</soapenv:Envelope>"""
r=requests.post("https://cucmip/axl/", verify=False, auth=('username','password'), data=soaprequest)
print(r.status_code) ##print the response code of the request sent [200] in case of successful transaction.
