def file_print(file):
	console.set_color(1, 1, 1)
	if file[-7:] == '.cl.txt' or file[-6:] == '.cl.md':
		rfile = open(file, 'r')
		rlist = rfile.readlines()
		for i in rlist:
			for r in range(21):
				for g in range(21):
					for b in range(21):
						if i[0:15] == '`~'+str('{0:0>3}'.format(r*5))+','+str('{0:0>3}'.format(g*5))+','+str('{0:0>3}'.format(b*5))+'~`':
							console.set_color(r/20, g/20, b/20)
							i = re.sub('\n', '', i)
							print(i[-(len(i) - 15):])
						else:
							pass
		rfile.close()
	else:
		x = [a for a in file.split('.') if a]
		y = '.'.join(x[-2:])
		console.set_color(1, 0, 0)
		print('Traceback (most recent call last):\n  File "<string>", line 8, in <module>\nFileFormarError:\n  Unsupported file extension, use\n  ".cl.txt" or ".cl.md" instead of\n  ".'+y+'"')
	console.set_color(1, 1, 1)
