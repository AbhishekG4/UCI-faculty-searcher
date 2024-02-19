import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

def FacultySearcher(interest, subinterest):    #Takes in interest and subinterest as regex
    fh=urllib.request.urlopen('http://catalogue.uci.edu/faculty/#faculty')
    #fh=open(input('Enter file name'))
    #uni=input('Enter University')
    print()
    ho=BeautifulSoup(fh.read(),'html.parser')           #ho is handle object
    fl=ho('div')                                        #fl is faculty list and ft is faculty tag
    ct1=0
    ct2=0
    l=[]
    for ft in fl:
        tok=None
        al=ft.attrs
        if not 'class' in al: continue
        a=ft.get('class',None)
        if not a[0]=='faculty': continue
        sl=ft('span')
        for st in sl:                                   #st is span tag and sl is span list
            if not 'research'==st.get('class',None)[0]: continue
            #if re.search('[aA]merican [iI]ndia', st.contents[0]):continue
            if re.search(interest,st.contents[0]):
                ct1=ct1+1
                print('sl.no.',ct1)
                for i in sl:
                    a=i.get('class',None)
                    if 'name'==a[0]: print('Name:',i.contents[0])
                    if 'degree'==a[0]: print('Deg.:',i.contents[0])
                    if 'department'==a[0]:
                        el=i('em')
                        print('Dept.:',el[0].contents[0])
                    if 'research'==a[0]:
                        print('Research: ',i.contents[0])
                        if re.search(subinterest,i.contents[0]):
                            ct2=ct2+1
                            l.append(ct1)
                print()
    print('=======================================================')
    print('count is: ',ct1)
    print('no. with subinterest: ',ct2)
    print('sl.no. of subinterest=',l)

print()
interest = input('Enter research interest to be searched as regex: ')
subin = input('Enter subinterest to be tracked as regex: ')
FacultySearcher(interest,subin)
