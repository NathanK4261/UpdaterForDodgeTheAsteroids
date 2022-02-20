'''
Updater for Dodge The Asteroids
Built By: Nathan Daniel Keidel
'''
import socket
import sys
import getpass
import time

usrname = getpass.getuser()
print(f'Username is {usrname}')
type(usrname)

UPDATE_lsock = socket.socket()

host = '192.168.158.155'
port = 4444

UPDATE_lsock.connect((host, port))
print('Connected to update server')

UPDATE_request = 'asuiawlf893742jklwegt98e7gwe__'
UPDATE_request = UPDATE_request.encode()

UPDATE_lsock.send(UPDATE_request)
print('Sent update request')

UPDATE_lsock_RECV = UPDATE_lsock.recv(1024)
UPDATE_lsock_RECV = UPDATE_lsock_RECV.decode()

print(f'Latest version is "Version:{UPDATE_lsock_RECV}", updating now...')

# Update the "installer.command file"
print('Locating files in "/Desktop" for "installer.command"...')

with open(f'/Users/{usrname}/Desktop/installer.command', 'r+') as UPDATE_installer_file:
    UPDATE_installer_file.truncate(0)
    print('File "/Users/{usrname}/Desktop/installer.command" has been truncated(0)')
    print('Begining rewrite process...')
    time.sleep(3)
    UPDATE_installer_file.write(f'''pip3 install pygame
git clone https://github.com/NathanK4261/DodgeTheAsteroids.git
cd DodgeTheAsteroids
unzip BETA{UPDATE_lsock_RECV}.zip
rm -dPRrvW __MACOSX
rm -f BETA{UPDATE_lsock_RECV}.zip
ls
cd BETA{UPDATE_lsock_RECV}
python3 __buildgame__.py
cd 
cd Desktop
chmod +x DodgeTheAsteroids.command
''')
    UPDATE_installer_file.close()

print('Finished! Returning to terminal. Once in terminal, you can safely exit the window!')
sys.exit()
