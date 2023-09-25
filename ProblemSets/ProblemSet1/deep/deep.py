answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

if answer.strip().isdigit() and int(answer.strip()) == 42:
    print('Yes')
elif answer.strip().lower() == 'forty-two' or answer.strip().lower() == 'forty two':
    print('Yes')
else:
    print('No')