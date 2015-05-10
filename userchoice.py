def user_input (question, choice_options):
	user_choice = input(question)
	while user_choice.upper() not in choice_options:
		user_choice = input ('Blad. Wybierz:' + str(choice_options) + '\n')
	return (user_choice.upper())



