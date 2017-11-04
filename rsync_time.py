#!/usr/bin/env python3

from datetime import datetime
import sys
import re

start = None
end = None

for line in sys.stdin:
	#print(line)
	timestamp = " ".join(line.split()[:2])
	if re.search("building file list", line):
		#print("building")
		start = timestamp
	if re.search("total size", line):
		#print("totalling")
		end = timestamp

if start and end:
	#print(start, "###", end)
	start = datetime.strptime(start, "%Y/%m/%d %H:%M:%S")
	end = datetime.strptime(end, "%Y/%m/%d %H:%M:%S")
	duration = end - start
	print("{0:.1f} hrs".format(duration.total_seconds() / 3600))
else:
	start = datetime.strptime(start, "%Y/%m/%d %H:%M:%S")
	last = datetime.strptime(timestamp, "%Y/%m/%d %H:%M:%S")
	duration = last - start
	print(">{0:.1f} hrs".format(duration.total_seconds() / 3600))
