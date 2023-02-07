def arithmetic_arranger(problems, solve=False):
  if len(problems) > 5:
    return 'Error: Too many problems.'
  numb1 = []
  numb2 = []
  border = []
  results = []
  operator = []
  for number in problems:
    # find space
    space = number.find(' ')

    # find and check numb1, numb2
    if (number[:space].isdigit() != True
        or number[space + 3:len(number)].isdigit() != True):
      return 'Error: Numbers must only contain digits.'
    if (len(number[:space]) > 4 or len(number[space + 3:len(number)]) > 4):
      return 'Error: Numbers cannot be more than four digits.'
    numb1.append(number[:space])
    numb2.append(number[space + 3:len(number)])

    # generate border
    if len(number[:space]) > len(number[space + 3:len(number)]):
      border.append('-' * ((len(number[:space])) + 2))
    else:
      border.append('-' * (len(number[space + 3:len(number)]) + 2))

    # generate result, find and check + or -
    if number[space + 1] == '+':
      results.append(int(number[:space]) + int(number[space + 3:len(number)]))
    elif number[space + 1] == '-':
      results.append(int(number[:space]) - int(number[space + 3:len(number)]))
    else:
      return "Error: Operator must be '+' or '-'."
    operator.append(number[space + 1])
  # variable string which is for output
  ln1 = ''
  ln2 = ''
  ln3 = ''
  ln4 = ''
  # print output
  for line in range(4):
    for each in range(len(numb1)):
      if line == 0:
        ln1 += (numb1[each].rjust(len(border[each])) + (' ' * 4))
      elif line == 1:
        ln2 += ((operator[each] + numb2[each].rjust(len(border[each]) - 1)) +
                (' ' * 4))
      elif line == 2:
        ln3 += (border[each] + (' ' * 4))
      else:
        if solve == True:
          ln4 += (str(results[each]).rjust(len(border[each])) + (' ' * 4))
  if solve == True:
    arranged_problems = ln1.rstrip() + '\n' + ln2.rstrip() + '\n' + ln3.rstrip() + '\n' + ln4.rstrip()
  else:
    arranged_problems = ln1.rstrip() + '\n' + ln2.rstrip() + '\n' + ln3.rstrip()
  return arranged_problems
