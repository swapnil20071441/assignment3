#bubble sort
salaries=[65000,120000,23000,45000,80000,55000,115000,75000]
n=len(salaries)

for i in range(n):
    for j in range(0,n-i-1):
        if salaries[j]>salaries[j+1]:
            salaries[j],salaries[j+1]=salaries[j+1],salaries[j]
print("bubble sort",salaries)

top_5 = salaries[-5:][::-1] 
print("Top 5 highest salaries:") 
print(top_5)

#selection sort
for i in range(n):
    min_index = i

    for j in range(i + 1, n):
        if salaries[j] < salaries[min_index]:
            min_index = j

    salaries[i], salaries[min_index] = salaries[min_index], salaries[i]

print("Selection Sort:", salaries)

print("Top 5 highest salaries:") 
print(salaries[-5:][::-1])