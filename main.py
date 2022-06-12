with open('5-letter-words.txt') as word_file:
    contents = word_file.read()
    word_list = contents.split('\n')


'''---------- Finding cumulative frequency for each occurrence of each letter in each position ----------'''
cumulative_frequencies = {
    'a': [0, 0, 0, 0, 0],
    'b': [0, 0, 0, 0, 0],
    'c': [0, 0, 0, 0, 0],
    'd': [0, 0, 0, 0, 0],
    'e': [0, 0, 0, 0, 0],
    'f': [0, 0, 0, 0, 0],
    'g': [0, 0, 0, 0, 0],
    'h': [0, 0, 0, 0, 0],
    'i': [0, 0, 0, 0, 0],
    'j': [0, 0, 0, 0, 0],
    'k': [0, 0, 0, 0, 0],
    'l': [0, 0, 0, 0, 0],
    'm': [0, 0, 0, 0, 0],
    'n': [0, 0, 0, 0, 0],
    'o': [0, 0, 0, 0, 0],
    'p': [0, 0, 0, 0, 0],
    'q': [0, 0, 0, 0, 0],
    'r': [0, 0, 0, 0, 0],
    's': [0, 0, 0, 0, 0],
    't': [0, 0, 0, 0, 0],
    'u': [0, 0, 0, 0, 0],
    'v': [0, 0, 0, 0, 0],
    'w': [0, 0, 0, 0, 0],
    'x': [0, 0, 0, 0, 0],
    'y': [0, 0, 0, 0, 0],
    'z': [0, 0, 0, 0, 0],

}


def find_cumulative_frequencies(current_list_of_words):
    for word in current_list_of_words:
        for k in range(5):
            if word[k] == 'a':
                cumulative_frequencies['a'][k] += 1
            elif word[k] == 'b':
                cumulative_frequencies['b'][k] += 1
            elif word[k] == 'c':
                cumulative_frequencies['c'][k] += 1
            elif word[k] == 'd':
                cumulative_frequencies['d'][k] += 1
            elif word[k] == 'e':
                cumulative_frequencies['e'][k] += 1
            elif word[k] == 'f':
                cumulative_frequencies['f'][k] += 1
            elif word[k] == 'g':
                cumulative_frequencies['g'][k] += 1
            elif word[k] == 'h':
                cumulative_frequencies['h'][k] += 1
            elif word[k] == 'i':
                cumulative_frequencies['i'][k] += 1
            elif word[k] == 'j':
                cumulative_frequencies['j'][k] += 1
            elif word[k] == 'k':
                cumulative_frequencies['k'][k] += 1
            elif word[k] == 'l':
                cumulative_frequencies['l'][k] += 1
            elif word[k] == 'm':
                cumulative_frequencies['m'][k] += 1
            elif word[k] == 'n':
                cumulative_frequencies['n'][k] += 1
            elif word[k] == 'o':
                cumulative_frequencies['o'][k] += 1
            elif word[k] == 'p':
                cumulative_frequencies['p'][k] += 1
            elif word[k] == 'q':
                cumulative_frequencies['q'][k] += 1
            elif word[k] == 'r':
                cumulative_frequencies['r'][k] += 1
            elif word[k] == 's':
                cumulative_frequencies['s'][k] += 1
            elif word[k] == 't':
                cumulative_frequencies['t'][k] += 1
            elif word[k] == 'u':
                cumulative_frequencies['u'][k] += 1
            elif word[k] == 'v':
                cumulative_frequencies['v'][k] += 1
            elif word[k] == 'w':
                cumulative_frequencies['w'][k] += 1
            elif word[k] == 'x':
                cumulative_frequencies['x'][k] += 1
            elif word[k] == 'y':
                cumulative_frequencies['y'][k] += 1
            elif word[k] == 'z':
                cumulative_frequencies['z'][k] += 1
    return cumulative_frequencies


word_scores = {}

cumulative_frequencies = find_cumulative_frequencies(word_list)
for word in word_list:
    score = 0
    for index in range(len(word)):
        score += cumulative_frequencies[word[index]][index]
    print(f'total score for word --- {word} --- = {score}')
    word_scores[word] = score

print('\n')
print(f'{len(word_list)} possible answers')
print(f'Suggested guess: {max(word_scores, key=word_scores.get)}')
print(f'Suggested guess score: {word_scores[max(word_scores, key=word_scores.get)]}')

'''---------- Logic for solver ----------'''

program_is_running = True
while program_is_running:

    for round_number in range(6):

        guess = input('Please input your guess: ')
        while guess not in word_list:
            guess = input('Invalid input. Please try again: ')

        code_allowed_characters = ['g', 'y', '-']
        code = list(
            input('Please input the code for your first guess (- = wrong letter, y = yellow letter, g = green letter): '))
        for letter_index in range(5):
            while len(code) != 5:
                code = input('Invalid input. Please try again: ')
            while code[letter_index] not in code_allowed_characters:
                code = input('Invalid input. Please try again: ')

        wrong_words = []
        for word in word_list:
            for i in range(5):
                if code[i] == '-' and guess[i] in word:
                    wrong_words.append(word)
                    break
                elif code[i] == 'y' and guess[i] == word[i]:
                    wrong_words.append(word)
                    break
                elif code[i] == 'y' and guess[i] not in word:
                    wrong_words.append(word)
                    break
                elif code[i] == 'g' and guess[i] != word[i]:
                    wrong_words.append(word)
                    break

        removed_counter = 0
        for wrong_word in wrong_words:
            if wrong_word in word_list:
                word_list.remove(wrong_word)
                del word_scores[wrong_word]
                removed_counter += 1
        print('\n')
        if removed_counter == 1:
            print(f'You have eliminated {removed_counter} possible answer')
        elif removed_counter == 0:
            pass
        else:
            print(f'You have eliminated {removed_counter} possible answers')

        wrong_words.clear()

        if code == list('ggggg'):
            if round_number == 0:
                print(f'Congrats! You solved today'f's Wordle in {round_number + 1} guess!')
                program_is_running = False
                break

            elif round_number != 0:
                print(f'Congrats! You solved today'f's Wordle in {round_number + 1} guesses!')
                program_is_running = False
                break

        if len(word_list) == 1:
            print(f'There is {len(word_list)} possible answer')
        else:
            print(f'There are {len(word_list)} possible answers')

        print(f'The suggested guess is: {max(word_scores, key=word_scores.get)}')
        print(f'{max(word_scores, key=word_scores.get).title()} has a cumulative frequency score of: {word_scores[max(word_scores, key=word_scores.get)]}')
