#[int(i) for i in input().split(' ')]
razmer = [int(i) for i in input().split(' ')]
A = [["" for i in range(razmer[1])] for j in range(razmer[0])]
temp_massive = [razmer[1]]
for i in range(razmer[0]):
	temp_massive = [i for i in input()]
	for j in range(razmer[1]):
		A[i][j] = temp_massive[j]

kolvo_ingridient = int(input())
ingridient = [[0 for i in range (3)] for j in range(kolvo_ingridient)]
for i in range(kolvo_ingridient):
	temp_massive = [i for i in input().split(' ')]
	for j in range(3):
		ingridient[i][j] = temp_massive[j]

count = 0
kolvo_count = 0
for i in range(razmer[0] - 2, -1, -1):
	for j in range(razmer[1] - 1, -1, -1):
		if A[i][j] == ' ':
			if kolvo_count != int(ingridient[count][1]):
				A[i][j] = ingridient[count][2]
				print(count)
	kolvo_count += 1
	if kolvo_count == int(ingridient[count][1]):
		if count == kolvo_ingridient - 1:
			break
		count += 1
		kolvo_count = 0

for i in range(razmer[0]):
	for j in range(razmer[1]):
		print(A[i][j], end = "")
	print("")