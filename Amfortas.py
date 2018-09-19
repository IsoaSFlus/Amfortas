import torrent_parser as tp
import sys

t = tp.parse_torrent_file(sys.argv[1])
fl = t['info']['files']
fl.sort(key=lambda x: -x['length'])

for i in range(0, 5):
    print("{}. {} {:.2f}MB".format(i+1, fl[i]['path.utf-8'][0], fl[i]['length']/1024/1024))

num = input('Input number you want: ')
num = int(num)
print("ed2k://|file|{}|{}|{}|/".format(fl[num-1]['path.utf-8'][0], fl[num-1]['length'], fl[num-1]['ed2k']))
