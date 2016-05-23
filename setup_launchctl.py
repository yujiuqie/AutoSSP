#coding=utf-8

import subprocess
import getpass

execute_file = 'start_auto_ssp'
operation_file = 'auto_ssp.py'

target_file_path = '/Users/'+ getpass.getuser() + '/'
launch_daemons_path = target_file_path + 'Library/LaunchAgents/'

# launch_daemons_path = '/Library/LaunchDaemons/'

def format_plist(info_plist,file_path,hour,minute):

    file_handle = open(file_path + info_plist, 'w')

    program_arguments = target_file_path + execute_file

    format_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">',
        '<plist version="1.0">',
        '<dict>',
        '<key>Label</key>',
        '<string>'+ info_plist +'</string>',
        '<key>ProgramArguments</key>',
        '<array>',
        '<string>'+ program_arguments +'</string>',
        '</array>',
        '<key>StartCalendarInterval</key>',
        '<dict>',
        '<key>Minute</key>',
        '<integer>'+ minute +'</integer>',
        '<key>Hour</key>',
        '<integer>'+ hour +'</integer>',
        '</dict>',
        '<key>KeepAlive</key>',
        '<false/>',
        '<key>RunAtLoad</key>',
        '<true/>',
        '</dict>',
        '</plist>'
    ]

    result_list = [line+'\n' for line in format_lines]
    file_handle.writelines(result_list)
    file_handle.close()

def reload_plist(time_list):

    plist_name = 'auto.ssp.'+ time_list[0] + time_list[1] +'.plist'

    plist_full_path = launch_daemons_path + plist_name

    print(plist_full_path)

    format_plist(plist_name,launch_daemons_path,time_list[0],time_list[1])

    subprocess.Popen('cp %s %s'%(execute_file,target_file_path), shell=True).wait()

    subprocess.Popen('cp %s %s'%(operation_file,target_file_path), shell=True).wait()

    subprocess.Popen('cp %s %s'%('base64_codec.py',target_file_path), shell=True).wait()

    # subprocess.Popen('chmod 666 %s%s'%(target_file_path,operation_file), shell=True).wait()

    subprocess.Popen('launchctl unload %s'%(plist_full_path), shell=True).wait()

    subprocess.Popen('launchctl load %s'%(plist_full_path), shell=True).wait()

def main():

    time_list_0 = ['17','04'];

    reload_plist(time_list_0)

if __name__ == '__main__':
    main()