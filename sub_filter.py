import re, getpass

filename = input('Move file to desktop and enter file name.\n')
#open and read unfiltered txt
path = '/Users/{}/desktop/'.format(getpass.getuser())
subtitles = open(path + filename + '.txt')
subtitles_unfiltered = subtitles.read()

#open new txt file for filered text
subtitles_filtered = open(path + filename + '_filtered.txt', 'w')


#find all time stamps
regEx = re.findall(r'\d{1,3}\n\d{2}.\d{2}.\d{2}.\d{3}\s...\s\d{2}.\d{2}.\d{2}.\d{3}\n', subtitles_unfiltered)

#remove time stamps and write filtered text to new file
raw_subtitles = subtitles_unfiltered
for x in regEx:
    raw_subtitles = raw_subtitles.replace(x,'')
subtitles_filtered.write(raw_subtitles)

#close all files
subtitles.close()
subtitles_filtered.close()


print('\n\n{} has been filtered.'.format(filename))