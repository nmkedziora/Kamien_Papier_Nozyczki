def win_loss_sequence(lista, winning_letter):
	previous_element = lista[0]
	max_sequence = 0
	if previous_element == winning_letter:
		sequence = 1
	else:
		sequence = 0
	if len(lista) == 1:
		return sequence
	for element in lista[1:]:
		if previous_element == element and previous_element == winning_letter:
			sequence+=1
			if max_sequence < sequence:
				max_sequence = sequence
		else:
			if element == winning_letter:
				sequence = 1
			else:
				if max_sequence < sequence:
					max_sequence = sequence
					sequence = 0

		previous_element = element
	return max_sequence


# win_loss_sequence(data, 'W')
# win_loss_sequence(data, 'W')
# win_loss_sequence(data, 'W')
# win_loss_sequence(data, 'P')
# win_loss_sequence(data1, 'W')
# win_loss_sequence(data1, 'P')


# import collections
# result = collections.Counter(data)
# print(result['W'])
