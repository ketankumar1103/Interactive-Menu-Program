import os

while True:
	print("Chat with me your requirements:", end = ' ')
	p = input()
	if(("run" in p) or ("execute" in p) or ("open" in p)):
		if(("chrome" in p) or ("internet" in p) or ("browser" in p)):
			os.system("chrome")
		elif(("notepad" in p) or ("editor" in p) or ("text" in p)):
			os.system("notepad")
		elif(("media" in p) or ("player" in p) or ("song" in p) or ("mp3" in p) or ("music" in p)):
			os.system("wmplayer")
		elif(("ms excel" in p) or ("excel" in p) or ("spreadsheet" in p)):
			os.system("excel")
		elif(("ms word" in p) or ("word" in p) or ("word document" in p)):
			os.system("Start word.exe")
		elif(("ms powerpoint" in p) or ("powerpoint" in p) or ("ppt" in p) or ("powerpoint presentation" in p) or ("presentation" in p)):
			os.system("Start powerpnt")
		elif(("Action Center" in p)):
			os.system("Start ms-actioncenter:")	
		elif(("Clock" in p)):
			os.system("start ms-clock:")
		elif(("Calculator" in p) or ("Calculate" in p) or ("Calc" in p)):
			os.system("calc")
		elif(("Calendar" in p) or ("Cal" in p)):
			os.system("start outlookcal:")
		elif(("camera" in p) or ("cam" in p) or ("capture" in p)):
			os.system("start microsoft.windows.camera:")
		elif(("candy crush" in p)):
			os.system("Start candycrushsodasaga:")
		elif(("mail" in p) or ("email" in p)):
			os.system("start outlookmail:")
		elif(("Microsoft Edge" in p) or ("edge" in p) or ("explorer" in p)):
			os.system("start microsoftedge")
		
		else:
			print("Enter a valid program requirement")
	elif "exit" in p:
			print("bye bye")
			break	

			
	if(("dont run" in p) or ("dont execute" in p) or ("dont open" in p)):
			print("does not support")
