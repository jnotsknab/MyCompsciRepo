class File_processor:
    '''A class that processes a file and returns a list of words in the file'''

    def __init__(self, file_name):
        '''Initializes the file name'''
        self.file_name = file_name
        self.text = {}


    def clean_word(self, word):
        cleaned_word = ''
        for char in word:
            if char.isalnum():
                cleaned_word += char
        return cleaned_word.lower()

    
    def build_count(self):
        with open(self.file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                words = line.split()
                for word in words:
                    cleaned_word = self.clean_word(word)
                    if cleaned_word in self.text:
                        self.text[cleaned_word] += 1
                    else:
                        self.text[cleaned_word] = 1
            return self.text


    def unique_words(self):
        special_words = []
        for word in self.text:
            if self.text[word] == 1:
                special_words.append(word)
        return special_words
    
    def save_word_data(self):
        with open('word_data.txt', 'w') as file:
            for word, count in self.text.items():
                file.write(f'{word}: {count}\n')

    def save_unique_words(self):
        with open('unique_words.txt', 'w') as file:
            unique_word_list = self.unique_words()
            for word in unique_word_list:
                file.write(f'{word}\n')
    

    def main(self):
        welcome_message = 'Welcome Whoever Grades This, I died making this.'
        print(welcome_message.center(60, '='))
        user_file = input('Enter a filename to proceed: ')
        self.file_name = user_file
        self.build_count()
        self.save_word_data()
        self.save_unique_words()
        print('Done!')

if __name__ == '__main__':
    file_processor = File_processor('')
    file_processor.main()

    


        






    



        
                

