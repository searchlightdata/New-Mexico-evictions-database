#Libraries we need
import sys, os

from requests_html import HTML, HTMLSession
from bs4 import BeautifulSoup as bs

data = {
#This is where you change UserName and Password to your SOPA login credentials
  'UserName': #your_user_name,
  'Password': #your_password,
  'ValidateUser': '1',
  'dbKeyAuth': 'JusticeAuth',
  'SignOn': 'Sign On'
}
LOGIN_URL = "https://securecourtcaseaccess.nmcourts.gov/login.aspx"
TARGET_URL = "https://securecourtcaseaccess.nmcourts.gov/Search.aspx?ID=100"


headersArea = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'https://securecourtcaseaccess.nmcourts.gov',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://securecourtcaseaccess.nmcourts.gov/default.aspx',
    'Accept-Language': 'en-US,en;q=0.9',
}

paramsArea = (
    ('ID', '100'),
)

dataArea = {
  'NodeID': '29111',
  'NodeDesc': 'Bernalillo Metropolitan'
}


DataAreaAll =  {
  'NodeID': '210,220,2210,2220,99,900,1000,1101,1055,1040,1070,1150,1175,1250,1275,1340,1355,1370,2020,3070,3101,3125,3150,4120,4240,4340,5030,5060,6080,6190,6230,7210,7229,7250,7280,8090,8180,8200,9050,9110,25601,150,500,610,700,900,100,1101,1201,1301,1400,1470,1480,1500,1600,1700,1800,1900,1910,1920,2000,2101,2201,2301,2400,2500,2600,2700,2800,2900,3000,3200,3300,3400,3500,3600,3700,3800,4000,4100,4300,4400,4500,4600,4700,4800,4900,5100,5200,5300,5400,5600,5800,5900,6001,29111',
  'NodeDesc': 'All Courts'
}


headersSearch = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'https://securecourtcaseaccess.nmcourts.gov',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://securecourtcaseaccess.nmcourts.gov/default.aspx',
    'Accept-Language': 'en-US,en;q=0.9',
}

paramsSearch = (
    ('ID', '100'),
)


dataSearch = {
  '__EVENTTARGET': '',
  '__EVENTARGUMENT': '',
  '__VIEWSTATE': '/wEPDwULLTEwOTk1NTcyNzAPZBYCZg9kFgICAQ8WAh4HVmlzaWJsZWgWAgIDDw9kFgIeB29ua2V5dXAFJnRoaXMudmFsdWUgPSB0aGlzLnZhbHVlLnRvTG93ZXJDYXNlKCk7ZGR8gO5bSe+IJNYv7tDJa3aakOK3VQ==',
  '__VIEWSTATEGENERATOR': 'BBBC20B8',
  '__EVENTVALIDATION': '/wEWAgKcp5bHDwKYxoa5COCqIZ6YKaR767+VZ1TuhCYYLd5W',
  'NodeID': '210,220,2210,2220,99,900,1000,1101,1055,1040,1070,1150,1175,1250,1275,1340,1355,1370,2020,3070,3101,3125,3150,4120,4240,4340,5030,5060,6080,6190,6230,7210,7229,7250,7280,8090,8180,8200,9050,9110,25601,150,500,610,700,900,100,1101,1201,1301,1400,1470,1480,1500,1600,1700,1800,1900,1910,1920,2000,2101,2201,2301,2400,2500,2600,2700,2800,2900,3000,3200,3300,3400,3500,3600,3700,3800,4000,4100,4300,4400,4500,4600,4700,4800,4900,5100,5200,5300,5400,5600,5800,5900,6001,29111',
  'NodeDesc': 'All Courts',
  'SearchBy': '0',
  'CaseSearchMode': 'CaseNumber',
  'CaseSearchValue': '',
  'CitationSearchValue': '',
  'CourtCaseSearchValue': '',
  'PartySearchMode': 'Name',
  'AttorneySearchMode': 'Name',
  'LastName': '',
  'FirstName': '',
  'cboState': 'AA',
  'MiddleName': '',
  'DateOfBirth': '',
  'DriverLicNum': '',
  'CaseStatusType': '0',
  'DateFiledOnAfter': '',
  'DateFiledOnBefore': '',
  'chkCriminal': 'on',
  'chkFamily': 'on',
  'chkCivil': 'on',
  'chkProbate': 'on',
  'chkDtRangeCriminal': 'on',
  'chkDtRangeFamily': 'on',
  'chkDtRangeCivil': 'on',
  'chkDtRangeProbate': 'on',
  'chkCriminalMagist': 'on',
  'chkFamilyMagist': 'on',
  'chkCivilMagist': 'on',
  'chkProbateMagist': 'on',
  'DateSettingOnAfter': '',
  'DateSettingOnBefore': '',
  'SortBy': 'fileddate',
  'SearchSubmit': 'Search',
  'SearchType': 'CASE',
  'SearchMode': 'CASENUMBER',
  'NameTypeKy': '',
  'BaseConnKy': '',
  'StatusType': 'true',
  'ShowInactive': '',
  'AllStatusTypes': 'true',
  'CaseCategories': '',
  'RequireFirstName': '',
  'CaseTypeIDs': '',
  'HearingTypeIDs': ''
}

headers = {
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://securecourtcaseaccess.nmcourts.gov/Search.aspx?ID=100',
    'Accept-Language': 'en-US,en;q=0.9',
}

#Start our HTML session by logging into SOPA
with  HTMLSession() as s:
    postResult = s.post(LOGIN_URL, data=data)

    #Create list of search terms used for wildcard search by magistrate court and year 
    magistrateCourtSearchByYear = ['T-4-CV-2021','M-5-CV-2021-', 'M-7-CV-2021-',	'M-9-CV-2021-',	'M-10-CV-2021-',	'M-12-CV-2021-',	'M-13-CV-2021-',	'M-14-CV-2021-',	'M-15-CV-2021-',	'M-16-CV-2021-',	'M-17-CV-2021-',	'M-18-CV-2021-',	'M-19-CV-2021-',	'M-20-CV-2021-',	'M-21-CV-2021-',	'M-23-CV-2021-',	'M-24-CV-2021-',	'M-25-CV-2021-',	'M-26-CV-2021-',	'M-27-CV-2021-',	'M-28-CV-2021-',	'M-29-CV-2021-',	'M-30-CV-2021-',	'M-32-CV-2021-',	'M-33-CV-2021-',	'M-34-CV-2021-',	'M-35-CV-2021-',	'M-36-CV-2021-',	'M-37-CV-2021-',	'M-38-CV-2021-',	'M-40-CV-2021-',	'M-41-CV-2021-',	'M-43-CV-2021-',	'M-44-CV-2021-',	'M-45-CV-2021-',	'M-46-CV-2021-',	'M-47-CV-2021-',	'M-48-CV-2021-',	'M-49-CV-2021-',	'M-51-CV-2021-',	'M-52-CV-2021-',	'M-53-CV-2021-',	'M-54-CV-2021-',	'M-56-CV-2021-',	'M-58-CV-2021-',	'M-59-CV-2021-',	'M-60-CV-2021-',	'M-61-CV-2021-',	'M-117-CV-2021-',	'M-147-CV-2021-',	'M-148-CV-2021-',	'M-150-CV-2021-',	'M-191-CV-2021-',	'M-192-CV-2021-']


    #Loop through the list of magistrate courts while also looping through the number of possible civil cases in that magistrate court 
    for courtSearch in magistrateCourtSearchByYear:
        for i in range(0,350): 
            
            print("Selection range: "+str(i))
            
            if (len(str(i)) ==1): 
                searchTerm = courtSearch + '000' + str(i) + '*'
            elif (len(str(i)) == 2):
                searchTerm = courtSearch + '00' + str(i) + '*'
            elif (len(str(i)) == 3):
                searchTerm = courtSearch + '0' + str(i) + '*'
            
            #Bernalillo Metropolitan Court from 2010 to 2014 does not use the above numeration system. Instead, just loop through a simple range of 0 to 14,000 
        
            print(searchTerm)
            
            dataSearch['CaseSearchValue'] = searchTerm
            CGRSearch= s.post('https://securecourtcaseaccess.nmcourts.gov/Search.aspx', headers=headersSearch, params=paramsSearch,  data=dataSearch)
            
            if ('Login' in CGRSearch.url):
                print("Error in "+str(CGRSearch.url))
                sys.exit()
            
            #Get the Case IDs for the cases that are results of our search AND contain the words case types for Landlord Tenant, Forcible Entry, Mobile Home Park, and Interpleader cases 
            caseIDs=[]
            p = bs(CGRSearch.text, 'lxml')
            table = p.find_all('table')
            courtData=table[5].find_all('tr')
            for i in range(3,len(courtData)):
                if 'Landlord' in str(courtData[i]):
                    tempString=bs(str(courtData[i]), 'lxml')
                    caseIDs.append(str(tempString.find_all('a')[0])[32:39])
                elif 'Forcible' in str(courtData[i]):
                     tempString=bs(str(courtData[i]), 'lxml')
                     caseIDs.append(str(tempString.find_all('a')[0])[32:39])
                elif 'Mobile Home' in str(courtData[i]):
                     tempString=bs(str(courtData[i]), 'lxml')
                     caseIDs.append(str(tempString.find_all('a')[0])[32:39])
                elif 'Interpleader' in str(courtData[i]):
                     tempString=bs(str(courtData[i]), 'lxml')
                     caseIDs.append(str(tempString.find_all('a')[0])[32:39])
                print(caseIDs)
                
            #Loop through the Case IDs and retrieve the webpage for that case 
            for i in caseIDs:
                 paramsCase = (('CaseID', str(i)),)
                 caseGetResults = s.get('https://securecourtcaseaccess.nmcourts.gov/CaseDetail.aspx', headers=headers, params=paramsCase)
                
                 if ('error' in caseGetResults.url):
                     print(str(i) + ": "+str(caseGetResults.url))
                     sys.exit()
                
                 #Save to the directory that this scraper is in 
                 f = open(str(i), 'wb')
                 f.write(caseGetResults.content)
                 f.close()