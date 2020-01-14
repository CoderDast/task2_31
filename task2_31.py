def read_text(myfile):
    text_read = open(myfile)
    number_lines = 0
    number_words = 0
    number_letters = 0
    for lines in text_read:
        number_lines +=1
        number_words += len(lines.split())
        number_letters += len(lines)
    text_read.close()
    return print (number_lines),print (number_words), print (number_letters-number_lines)
    
read_text('text31.txt')