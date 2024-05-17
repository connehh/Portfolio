# FiveM Cache Deleter

import os, shutil
username = os.getlogin()
total_size = 0
files = ["cache", "server-cache-priv", "server-cache"]


# both of the following functions cover checking the size of your cache folders
# I couldn't figure out how to make one function go through a list, so I did it the caveman way
def checkcacheforcon():
    global total_size
    for dirpath, dirnames, filenames in os.walk('J:\\FiveM\\FiveM.app\\data\\cache'):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    for dirpath, dirnames, filenames in os.walk('J:\\FiveM\\FiveM.app\\data\\server-cache-priv'):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    for dirpath, dirnames, filenames in os.walk('J:\\FiveM\\FiveM.app\\data\\server-cache'):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)


def checkcacheforeveryoneelse():
    global total_size
    for dirpath, dirnames, filenames in os.walk('C:\\Users\\' + username + '\\AppData\\Local\\FiveM\\FiveM.app\\data\\cache'):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    for dirpath, dirnames, filenames in \
            os.walk('C:\\Users\\' + username + '\\AppData\\Local\\FiveM\\FiveM.app\\data\\server-cache-priv'):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    for dirpath, dirnames, filenames in os.walk('C:\\Users\\' + username + '\\AppData\\Local\\FiveM\\FiveM.app\\data\\server-cache'):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)


# format_bytes fn turns the bytes read earlier into a readable, user-friendly size
def format_bytes(B):
    B = float(B)
    KB = float(1024)
    MB = float(KB ** 2)  # 1,048,576
    GB = float(KB ** 3)  # 1,073,741,824
    TB = float(KB ** 4)  # 1,099,511,627,776

    if B < KB:
        return '{0} {1}'.format(B,'Bytes' if 0 == B > 1 else 'Byte')
    elif KB <= B < MB:
        return '{0:.2f} KB'.format(B / KB)
    elif MB <= B < GB:
        return '{0:.2f} MB'.format(B / MB)
    elif GB <= B < TB:
        return '{0:.2f} GB'.format(B / GB)
    elif TB <= B:
        return '{0:.2f} TB'.format(B / TB)


# main fn deletes the cache folders...
def main():
    for l in files:
        print("Commencing cache delete..")
        try:
            shutil.rmtree("J:\\FiveM\\FiveM.app\\data\\" + l)
            print("Since this code was made by me, it's attempting to delete your cache from the J: directory first..")
        except Exception as a:
            print(a)
            print("I'm now attempting to delete your cache from your C: drive")
            shutil.rmtree("C:\\Users\\" + username + "\\AppData\\Local\\FiveM\\FiveM.app\\data\\" + l)
        except FileNotFoundError as c:
            print(c)
            print('One or more of your folders were not there..')


# Checking the size of your cache files
try:
    checkcacheforeveryoneelse()
    checkcacheforcon()
except FileNotFoundError as b:
    print(b)
    print('I could not find your FiveM cache files in your C: or J: drive. '
          'If you continue, the operation will not work')
else:
    print('Your cache size is: ')
    print(format_bytes(total_size))

response = input('Do you want to clear your cache? [Y/N]: ')

if response.lower() == 'y':
    main()
    print('Your cache has been deleted')
else:
    print('Your cache has not been deleted then!')
