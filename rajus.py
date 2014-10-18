numCourses, numConstraints = input().split()
numCourses = int(numCourses)
numConstraints = int(numConstraints)

parentsOf = {str(i+1): [] for i in range(numCourses)}
for line in range(numConstraints):
    parent, course = input().split()
    parentsOf[course].append(parent)

update = True
while update:
    update = False
    for course in range(numCourses):
        parents = parentsOf[str(course+1)]
        for parent in parents:
            ancestors = parentsOf[parent]
            for ancestor in ancestors:
                if ancestor not in parents:
                    parents.append(ancestor)
                    update = True

proposed = input().split()
valid = True
if len(parentsOf[proposed[0]]) > 0:
    valid = False
i = 1
while valid and i < (len(proposed)):
    if proposed[i] in parentsOf[proposed[i-1]]:
        valid = False
    i += 1

print('YES' if valid else 'NO')
