import sys
import bs4
from bs4 import BeautifulSoup
import requests
import urllib.parse as urlparse
from urllib.parse import parse_qs
import datetime
import os
import PySimpleGUI as sg


listOfstr = []

def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

def bongkarTag(tag):

	if(tag.name == 'link'):
		#print("Link")
		return
	elif(tag.name == 'meta'):
		#print("Meta")
		return
	elif(tag.name == 'script'):
		#print("Script")
		return
	elif(tag.name == 'noscript'):
		#print("Noscript")
		return
	elif(tag.name == 'style'):
		return
	
	if isinstance(tag,bs4.element.NavigableString):
		if (isinstance(tag,bs4.element.Comment)):
			return
		#print(type(tag))
		if(tag.string.strip() != ''):
			#print(tag.string)

			listOfstr.append(str(tag.parent.name)+"無"+str(tag.string))
		else:
			return
		 	
	#print(type(tag))


	

	if tag.name is not None:
		#print(tag.name)
		None



	try:
		for x in tag.attrs:
			try:
				#print(str(x) +" : "+ str(tag.attrs[x]))
				None
			except Exception as e:
				#print(str(x))
				None
	except Exception as e:
		None
	'''
	if tag.string is not None:
		print(tag.string)
	'''

	try:
		for x in tag.contents:			
			bongkarTag(x)
	except Exception as e:
		None
	if tag.name is not None:
		#print("End of "+str(tag.name))
		#print()
		None

GUImode = True
while GUImode:
	goOn = True
	while goOn:
		try:
			
			url = input("URL : ")
			#url = "https://muhammadcank.wordpress.com/2012/05/26/kromatografi-fingerprint-dan-standardisasi-obat-herbal/"
			if url == 'q':
				sys.exit(0)

			if "https://" not in url and "http://" not in url:
				url = "https://"+str(url)

			actualPayload = bytearray()
			response = requests.get(url)
			goOn = False
			listOfstr = []
		except Exception as e:
			print(e)

	
	actualPayload = response.text
	#print(actualPayload)

	os.system("clear")
	soup = BeautifulSoup(actualPayload,'lxml')
	for i in soup.contents:
		#print(type(i))
		if isinstance(i,bs4.element.Doctype):
			print("Doctype : "+str(i))
			#print()
		elif isinstance(i,bs4.element.Tag):
			bongkarTag(i)
			#print()

	os.system("clear")


	layout = []
	layout = [[sg.MLine(size=(None,500),font=('Noto',13),key='-ML1-')]]
	window = sg.Window("rb ["+str(sizeof_fmt(len(actualPayload)))+"]",layout,resizable=True).Finalize()

	ultimateString = ""

	pastEM = False
	isFirst = True
	for i in listOfstr:
		#print(i.strip())
		#disline = []

		disline = i.strip()
		if "em無" in disline:
			disline = disline.replace("em無",'')
			disline += " "
			pastEM = True
		elif pastEM:
			disline += " "
			pastEM = False
			if "p無" in disline:
				disline = disline.replace("p無",'')	

		elif "p無" in disline:
			disline = disline.replace("p無",'')
			disline = "\n\n" + disline
		elif isFirst:
			isFirst = False
		else:
			disline = "\n\n" + disline


		ultimateString += disline
		#disline.append(sg.Text(i.strip()))
		#layout.append(disline)


	window['-ML1-'].update(ultimateString)




	#print(str(sizeof_fmt(len(actualPayload))))

	#layout = [[sg.Text('Some text on Row 1')],[sg.Text('Enter something on Row 2')]]



	
		