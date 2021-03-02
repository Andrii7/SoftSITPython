def parallel_lines(line1, line2):
  return line1[0]/line1[1] == line2[0]/line2[1]

print(parallel_lines([1,2,3], [1,2,4]))

print(parallel_lines([2,4,1], [4,2,1]))

print(parallel_lines([0,1,5], [0,1,5]))