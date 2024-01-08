while True:
    grade = float(input('Enter the grade in decimal system: '))
    if 0 <= grade <= 10:
        break
    else:
        print('Invalid grade')
if grade >= 8.5 and grade <= 10.0:
    print('Alphabet grade: A\n4th grade: 4')
elif grade >= 7.0 and grade < 8.5:
    print('Alphabet grade: B\n4th grade: 3')
elif grade >= 5.5 and grade < 7.0:
    print('Alphabet grade: C\n4th grade: 2')
elif grade >= 4.0 and grade < 5.5:
    print('Alphabet grade: D\n4th grade: 1')
else:
    print('Alphabet grade: F\n4th grade: 0')