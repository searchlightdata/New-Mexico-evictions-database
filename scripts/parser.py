import csv
import re
import sys, os
import unicodedata 

from bs4 import BeautifulSoup as bs

#set names for all the fields that we'd like to fill with information from the case docket. 
AllData=[]
field_names=["caseNumber", "filename", "caseType", "dateFiled", "location", "judicialOfficer", "plaintiff1", "plaintiff1Address", "plaintiff1Attorney", "plaintiff2", "plaintiff2Address", "plaintiff2Attorney", "plaintiff3", "plaintiff3Address", "plaintiff3Attorney", "plaintiff4", "plaintiff4Address", "plaintiff4Attorney", "plaintiff5", "plaintiff5Address", "plaintiff5Attorney"]

#open the files from the directory where the html files of each docket were saved to
for filename in os.listdir(os.getcwd()):
    if bool(re.match("^[0-9]+$", filename)):
        with open(os.path.join(os.getcwd(), filename), 'r', encoding="utf-8") as f: 
            
            #create empty strings for all of our fields 
            caseType = ""
            dateFiled = ""
            location = ""
            judicialOfficer = ""
            plaintiff1 = ""
            plaintiff1Address = ""
            plaintiff1Attorney = ""
            plaintiff2 = ""
            plaintiff2Address = ""
            plaintiff2Attorney = ""
            plaintiff3 = ""
            plaintiff3Address = ""
            plaintiff3Attorney = ""
            plaintiff4 = ""
            plaintiff4Address = ""
            plaintiff4Attorney = ""
            plaintiff5 = ""
            plaintiff5Address = ""
            plaintiff5Attorney = ""
            
            #Turn our docket into beautiful soup and find these first few pieces of information            
            contents = f.read()
            soup = bs (contents,'html.parser')
            table4 = soup.find_all('table')[4]
            dataB = table4.find_all('b')
            numIndex = soup.find_all('div')[1].text.index("No.")
            caseNumber = soup.find_all('div')[1].text[numIndex+4:]
            caseType = dataB[1].text
            dateFiled = dataB[2].text
            location = dataB[3].text
            judicialOfficer = dataB[4].text #Comment out the judicial officer variable if parsing cases from the years 2011 and 2012
            
              #Find the table in the docket where the parties' names and addresses are listed
            partiesTable = soup.find_all('table')[7]
            if 'Defendant' not in str(partiesTable.text):
                partiesTable = soup.find_all('table')[8]
            partiesTableHeaders = partiesTable.find_all('th')
            
            #Loop through the data in the table to account for all defedants and plaintiffs
            numPlaintiffs=0
            for data in partiesTableHeaders: 
                dataText=data.text
                if 'plaintiff' in data.text.lower():
                    numPlaintiffs=numPlaintiffs+1
            
            #Make a list of defendant and plaintiff names 
            plaintiffNameList=[""]*(numPlaintiffs)
                
            currentPlaintiffNumber=0
            thLen=len(partiesTable.find_all('th'))
            for i in range(0,thLen): 
                data= partiesTableHeaders[i].text
                if 'plaintiff' in data.lower():
                    plaintiffNameList[currentPlaintiffNumber]=partiesTableHeaders[i+1].text
                    currentPlaintiffNumber=currentPlaintiffNumber+1
            
            #Make a list of the coressponding addresses for each defendant and plaintiff 
            plaintiffAddrList=[""]*(numPlaintiffs)
            currentPlaintiffNumber=0 
            for data in partiesTable.find_all('td'):
                if (re.findall(r"\D(\d{5})", data.text)):
                    if (currentPlaintiffNumber<numPlaintiffs):
                        plaintiffAddrList[currentPlaintiffNumber]=unicodedata.normalize("NFKD", data.text)
                        currentPlaintiffNumber=currentPlaintiffNumber+1
                        
                        #Create a list for attorneys 
            plaintiffAttorneyList=[]
            currentPlaintiffNumber=0 
            for data in partiesTable.find_all('b'):
                if (currentPlaintiffNumber<numPlaintiffs):
                    plaintiffAttorneyList.append(unicodedata.normalize("NFKD", data.text))
                    currentPlaintiffNumber=currentPlaintiffNumber+1
            
            #Use our defendant and plaintiff list to loop through and find an attorney for each party
           
            
            currentPlainName=0
            plainNameListLen=len(plaintiffNameList)
            for i in range(0,plainNameListLen): 
                if i==0:
                    plaintiff1=plaintiffNameList[0]
                    plaintiff1Address=plaintiffAddrList[0]
                    if len(plaintiffAttorneyList)>i:
                        plaintiff1Attorney=plaintiffAttorneyList[0]
                        
                if i==1:
                   plaintiff2=plaintiffNameList[1]
                   plaintiff2Address=plaintiffAddrList[1]
                   if len(plaintiffAttorneyList)>i:
                        plaintiff2Attorney=plaintiffAttorneyList[1]
            
                if i==2:
                   plaintiff3=plaintiffNameList[2]
                   plaintiff3Address=plaintiffAddrList[2]
                   if len(plaintiffAttorneyList)>i:
                        plaintiff3Attorney=plaintiffAttorneyList[2]
            
                if i==3:
                   plaintiff4=plaintiffNameList[3]
                   plaintiff4Address=plaintiffAddrList[3]
                   if len(plaintiffAttorneyList)>i:
                        plaintiff4Attorney=plaintiffAttorneyList[3]
                        
                if i==4:
                   plaintiff5=plaintiffNameList[4]
                   plaintiff5Address=plaintiffAddrList[4]
                   if len(plaintiffAttorneyList)>i:
                        plaintiff5Attorney=plaintiffAttorneyList[4]
            
             #Take all the information above and save it to its corresponding case in the loop
            caseData= [caseNumber, filename, caseType, dateFiled, location, judicialOfficer,plaintiff1, plaintiff1Address, plaintiff1Attorney, plaintiff2, plaintiff2Address, plaintiff2Attorney, plaintiff3, plaintiff3Address, plaintiff3Attorney, plaintiff4, plaintiff4Address, plaintiff4Attorney, plaintiff5, plaintiff5Address, plaintiff5Attorney]
            AllData.append(caseData)

            
#Write the information for each case into a CSV
with open('Results.csv', 'w', encoding='utf-8', newline='') as csvfile: 
    #writer = csv.DictWriter(csvfile, fieldnames = field_names) 
    #writer.writeheader() 
   
    csvWriter = csv.writer(csvfile,delimiter=',')
    field_names2=[field_names]
    csvWriter.writerows(field_names2) 
    csvWriter.writerows(AllData)