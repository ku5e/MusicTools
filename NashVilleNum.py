#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 01/28/2022
#Purpose: Work out scales and nashville numbers

#scale of C 
# major 		C, 	D, 	E, 	F, 	G, 	A, 	B
# int   		R  		3  		5 		7
# Major scale 	x 	x+2	x+4	x+5 x+7	x+9 	x+11
# Chords 		M	m	m	M	M	m	dim/2
# Triad			x	
#				x+4
#				x+7

# minor			C, 	D, 	E♭, 	F, 	G, 	A♭, 	B♭
# int   		R    	3 		5 		7 
# minor Scale	x	x+2	x+3	x+5	x+7	x+8	x+10
# Chords		m	dim	M	m	m	M	M
# Triad			x	
#				x+4
#				x+7	

fancyNotes = ['c', 'c♯|d♭', 'd', 'd♯|e♭', 'e', 'f', 'f♯|g♭', 'g', 'g♯|a♭', 'a', 'a♯|b♭', 'b']
notes = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b']
numNotes = len(notes)
majorIntervals = [0, 2, 4, 5, 7, 9, 11]
minorIntervals = [0, 2, 3, 5, 7, 8, 10]
majorTonality = [' ', 'm', 'm', ' ', ' ', 'm', '°']
minorTonality = ['m', '°m', ' ', 'm', 'm', ' ', ' ']
triad = [0, 4, 7]
topLine = ''
bottomLine = ''

key = input('What key are we working with? (# only) ').lower()
tonality = input('[M]ajor or [m]inor? ')

root = notes.index(key)
nash = list()
for i in range(7):
	if tonality == 'm':
		nash.append(fancyNotes[(root + minorIntervals[i]) % numNotes])
	else:
		nash.append(fancyNotes[(root + majorIntervals[i]) % numNotes])
		
for i in range(7):
	if tonality == 'm':
		topLine += '  ' + str(i + 1) + '-' + nash[i].upper() + minorTonality[i] + '\t'
	else:
		topLine += '  ' + str(i + 1) + '-' + nash[i].upper() + majorTonality[i] + '\t'
		if i == 6:
			topLine = topLine[:-1]
			topLine += '/' + nash[1].upper()

print()
print('The chords in the number system are:')
print(topLine)


