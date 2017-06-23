import os, sys
import shutil
import time, datetime


print('Create new package with Anderungsblatter')
new_folder_name = input("New Station: ")
path = new_folder_name
os.makedirs(path, 493)  
# chose = input("Chose 1 or 2 : ")
# if chose == "1":
#     os.chdir('DefaultStation')
# else:    
#     os.chdir('DefaultRobot')
baseFolder = 'DefaultStation'
os.chdir(baseFolder)

f_anlagaIN = input("Anlaga: ")
f_stationIN = input("Station: ")
f_werkzeugIN = input("Werkzeug: ")
f_versionIN =input("Version: ")
f_dateIN = datetime.datetime.today().strftime('%Y.%m.%d')

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    f_anlaga, f_station, f_werkzeug, f_kind, f_version, f_date = f_name.split('_')


    f_anlaga = f_anlaga if f_anlagaIN == "" else f_anlagaIN
    f_station = f_station if f_stationIN == "" else f_stationIN
    f_werkzeug = f_werkzeug if f_werkzeugIN == "" else f_werkzeugIN
    f_version = f_version if f_versionIN == "" else f_versionIN
    f_date= f_dateIN
    
    new_name = '{}_{}_{}_{}_{}_{}{}'.format(f_anlaga, f_station, f_werkzeug, f_kind, f_version, f_date, f_ext)

    os.rename(f, new_name)



os.chdir('..')
pwd = os.getcwd()
dest = os.path.join(pwd, path)
src = os.path.join(pwd, baseFolder)

src_files = os.listdir(src)
for file_name in src_files:
    full_file_name = os.path.join(src, file_name)
    if (os.path.isfile(full_file_name)):
        shutil.copy(full_file_name, dest)

 

    
    