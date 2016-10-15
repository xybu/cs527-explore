 #!/usr/bin/python3

import os
import sys
import shutil
import subprocess

try:
	os.mkdir(sys.argv[2])
except Exception as e:
	print(e)

for dir_name, subdirs, files in os.walk(sys.argv[1]):
	for fname in files:
		if fname.startswith('id:') and ('crash' in  dir_name or 'hang' in dir_name):
			path = dir_name + '/' + fname
			print(path)
			try:
				subprocess.check_call(['/root/suricata/src/suricata', '--afl-rules', dir_name + '/' + fname], stderr=subprocess.STDOUT, timeout=5)
			except subprocess.CalledProcessError as e:
				shutil.copy(path, sys.argv[2] + '/' + fname)
				with open(sys.argv[2] + '/' + fname + '.out', 'w') as f:
					print('Exception: ' + str(e), file=f)
					print('Command: ' + str(e.cmd), file=f)
					print('Return code: ' + str(e.returncode), file=f)
					print('Output: ', file=f)
					print(e.output, file=f)
				print('\033[91m' + path + ' Crashed!\033[0m')
			except subprocess.TimeoutExpired as e:
				shutil.copy(path, sys.argv[2] + '/' + fname)
				with open(sys.argv[2] + '/' + fname + '.out', 'w') as f:
					print('Exception: ' + str(e), file=f)
					print('Command: ' + str(e.cmd), file=f)
					print('Timeout: ' + str(e.timeout), file=f)
					print('Output: ', file=f)
					print(e.output, file=f)
				print('\033[91m' + path + ' Hung!\033[0m')

