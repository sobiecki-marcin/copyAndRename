import os, sys
import shutil
import time, datetime


print('Create new package with Anderungsblatter, Choose: Station[1] or Robot[2]')


chose = input("Choose 1 or 2 : ")
if chose == "1":
    new_folder_name = input("New Station: ")
    path = new_folder_name
    os.makedirs(path, 493) 

    baseFolder = 'DefaultStation' 
    os.chdir(baseFolder)
    print("If standart, press ENTER")
    f_anlagaIN = input("Anlage(Standart 11A112): ")
    f_stationIN = input("Station(Standart S1253): ")
    f_werkzeugIN = input("Werkzeug(Standart Spannwerkzeug): ")
    f_versionIN =input("Version(Standart v1.0): ")
    f_dateIN = datetime.datetime.today().strftime('%Y.%m.%d')

    for f in os.listdir():
        f_name, f_ext = os.path.splitext(f)
        f_anlaga, f_station, f_werkzeug, f_kind, f_version, f_date = f_name.split('_')


        f_anlaga = "11A112" if f_anlagaIN == "" else f_anlagaIN
        f_station = "S1253" if f_stationIN == "" else f_stationIN
        f_werkzeug = "Spannwerkzeug" if f_werkzeugIN == "" else f_werkzeugIN
        f_version = "v1.0" if f_versionIN == "" else f_versionIN
        f_date= f_dateIN
    
        new_name = '{}_{}_{}_{}_{}_{}{}'.format(f_anlaga, f_station, f_werkzeug, f_kind, f_version, f_date, f_ext)
        os.rename(f, new_name)



elif chose == "2":    
    new_folder_name = input("New Robot: ")
    path = new_folder_name
    os.makedirs(path, 493) 
    baseFolder = 'DefaultRobot'
    os.chdir(baseFolder)

    print("If standart, press ENTER")
    f_anlagaIN = input("Anlage(Standart 11A112): ")
    f_robotIN = input("Robot(Standart R01): ")
    f_stationIN = input("Station(Standart 1251): ")
    f_modulIN = input("Modul(Standart RHA001): ")
    f_versionIN =input("Version(Standart v1.0): ")
    f_dateIN = datetime.datetime.today().strftime('%Y.%m.%d')

    for f in os.listdir():
        f_name, f_ext = os.path.splitext(f)
        f_anlaga, f_robot, f_station, f_modul, f_kind, f_version, f_date = f_name.split('_')


        f_anlaga = "11A112" if f_anlagaIN == "" else f_anlagaIN
        f_robot = "R01" if f_robotIN == "" else f_robotIN
        f_station = "1251" if f_stationIN == "" else f_stationIN
        f_modul = "RHA001" if f_modulIN == "" else f_modulIN
        f_version = "v1.0" if f_versionIN == "" else f_versionIN
        f_date= f_dateIN
    
        new_name = '{}_{}_{}_{}_{}_{}_{}{}'.format(f_anlaga, f_robot, f_station, f_modul, f_kind, f_version, f_date, f_ext)

        os.rename(f, new_name)    

else:
    print("Try again!!")



os.chdir('..')
pwd = os.getcwd()
dest = os.path.join(pwd, path)
src = os.path.join(pwd, baseFolder)

src_files = os.listdir(src)
for file_name in src_files:
    full_file_name = os.path.join(src, file_name)
    if (os.path.isfile(full_file_name)):
        shutil.copy(full_file_name, dest)

 

    
    