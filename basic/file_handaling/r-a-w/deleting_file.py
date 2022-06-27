import os
if os.path.exists('new_file.txt'):
 os.remove('new_file.txt')
 print("file has deleted successfully!")
else:
 print('file does not exists,')
