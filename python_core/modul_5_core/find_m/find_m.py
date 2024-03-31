files = ['video.avi', 'audio.mp3', 'document.doc', 'folder', 'back.tar.gz']

#for file in files:
    #indx = file.find('.')
    #if indx != -1:
        #suffix = file[indx + 1:]
        #print(f'File: {file}, Index: {indx}, Suffix: {suffix}')
    #else:
        #print(f'File: {file}, Suffix: not found')

for file in files:
    try:
        #indx = file.index('.')
        indx = file.rindex('.')
        suffix = file[indx + 1:]
        print(f'File: {file}, Index: {indx}, Suffix: {suffix}')

    except ValueError:
        print(f'File: {file}, Suffix: not found')