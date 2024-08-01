import webbrowser

# BIO
def bio_kg():
	print("\nName\t\t:\tKASHYAP RAVAL\nMo. Number\t:\t9106385616\nDOB\t\t:\t26 - OCT - 2002")

# EDUCATIONAL QUALIFICATION
def edu_info_kg():

	print('\nSECONDRY SCHOOLING : SHREE SHASTRISWAMI NARAYANSEVADASJI VIDYALAYA, SURENDRANAGAR')
	print('\t\t\t\t\t\t\tfor more press --> 1\n\t\t\t\t\t\t\telse press any key\n')

	print('HIGHER SECONDRY SCHOOLING : INDIAN PUBLIC SCHOOL, SURENDRANAGAR')
	print('\t\t\t\t\t\t\tfor more press --> 2\n\t\t\t\t\t\t\telse press any key\n')

	print('BACHLOR STUDIES : L J INSTITUTE OF ENGINEERING AND TECHNOLOGY\neffiliciated to - GUJARAT TECHNOLIGICAL UNIVERSITY')
	print('\t\t\t\t\t\t\tfor more press --> 3\n\t\t\t\t\t\t\telse press any key\n')
	l = input()


	while int(l) <= 3:
		print('hi')
		# break
	else:
		pass

# SKILLS
def skills_kg():
	pass

# =========================================================================================================================================================

# CONTACT
def contact_kg():
	try:
		choice_contact = int(input('\n1 : GIT HUB\n2 : LINKED IN ACCOUNT\n3 : TO DO MAIL\n4 : SKYPE PROFILE\n5 : INSTAGRAM PROFILE\n6 : GO BACK...\nTo go on my profiles please select any of them : '))
		# choice_contact = print('To go on my profiles please select any of them ....\n1 : GIT HUB\n2 : LINKED IN ACCOUNT\n3 : TO DO MAIL\n4 : SKYPE PROFILE\n5 : INSTAGRAM PROFILE\n6 : GO BACK...')

		while choice_contact <= 6:
			match choice_contact:
				case 1:
					print("\nYou are redirecting to my 'GIT HUB' profile ...")
					git_hub = 'https://github.com/kgraval02'
					webbrowser.open(git_hub)
					contact_kg()
					break

				case 2:
					print("\nYou are redirecting to my 'LINKED IN PROFILE' profile ...")
					linked_in = 'https://www.linkedin.com/in/kg-raval'
					webbrowser.open(linked_in)
					contact_kg()
					break

				case 3:
					print("\nYou are redirecting to my 'MAIL COMPOSE' ...")
					mail = 'mailto:kashyapg262002@gmail.com'
					webbrowser.open(mail)
					contact_kg()
					break
					
				case 4:
					print("\nYou are redirecting to my 'SKYPE PROFILE' profile ...")
					skype = 'https://join.skype.com/invite/wvvDfXAp0Qiu'
					webbrowser.open(skype)
					contact_kg()
					break

				case 5:
					print("\nYou are redirecting to my 'INSTA PROFILE' profile ...")
					insta = 'https://www.instagram.com/k.g.raval/'
					webbrowser.open(insta)
					contact_kg()
					break
					
				case 6:
					print('\nBack...')

					break
		else:
			print('\nYou did not entered your choice from given options.\nPlease enter choice as per given options....\n')
			contact_kg()
	except:
		print('Error in your input please enter valid input here ...')
		contact_kg()

# visiter's main choce
def	main_choice():
	try:
		choice_info = int(input('\n1. BIO\n2. EDUCATIONAL QUALIFICATION\n3. SKILLS\n4. CONTACT\n5. To EXIT\nEnter your choice please : '))
		while choice_info <= 5:
			match choice_info:
				# BIO
				case 1:
					bio_kg()
					main_choice()
					break
				
				# EDUCATIONAL QUALIFICATION
				case 2:
					edu_info_kg()
					main_choice()
					break

				# SKILLS
				case 3:
					skills_kg()
					main_choice()
					break
				
				# CONTACT
				case 4:
					contact_kg()
					main_choice()
					break
				
				# exit
				case 5:
					print('\nEXIT...')
					# break
					break
		else:
			print('\nYou did not entered your choice from given options.\nPlease enter choice as per given options....\n')
			main_choice()
	except:
		print('Please enter valid input ...')
		main_choice()

# welcome script
def wel_come():
	nm_visitor = input('Enter your name here please ... ')
	print(f"\n\t\t\tWelcome, {nm_visitor}! 🎉\n\tSuper excited you’re here to look into my Portfolio!\n\t\tFeeling glade to have your visit here.\n\t****************************************************\n")
	print('To redirect over the profiles please enter perticular inputs from the given options please ....')

	main_choice()

wel_come()