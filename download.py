import urllib.request as request
import bz2
import os

# ctrl + F5 : run
# for 2005 ~ 2008
# for i in range(2005, 2009):
#     url="http://192.168.0.57/Hadoop/data/{}.csv.bz2".format(i)
#     outname="{}.csv.bz2".format(i)
#     request.urlretrieve(url, outname)
#     print("downloaded file : {}".format(outname))

# for i in range(2005, 2009):
#     outname = "{}.csv.bz2".format(i)
#     finalname = "{}.csv".format(i)

#     with bz2.open(outname,"rb") as infile, open(finalname, "w") as outfile:
#         data=infile.read().decode('utf-8').split('\n')[1:] # 첫번째 줄 잘라, 1번째부터끝까지 넣겠다
#         data="\n".join(data) # "\n" 을 구분자로 다시 넣겠다
#         outfile.write(data)
#     print("wrote file : {}".format(finalname))

# for item in os.listdir('./'):
#     if item.endswith('.bz2'):
#         os.remove(os.path.join('./',item))
#         print("removed file : {}".format(item))

for i in range(2005, 2009):
	url = "http://192.168.0.57/Hadoop/data/{}.csv.bz2".format(i)
	out_fname = "./{}.csv.bz2".format(i)
	final_fname = "./{}.csv".format(i)
	request.urlretrieve(url, out_fname)
	print("downloaded file: {}".format(out_fname))
	with bz2.open(out_fname, "rb") as in_file, open(final_fname, "w") as out_file:
		data = in_file.read().decode('utf-8').split('\n')[1:]
		data = "\n".join(data)
		out_file.write(data)
	print("wrote file: {}".format(final_fname))

for item in os.listdir('./'):
    if item.endswith('.bz2'):
        os.remove(os.path.join('./', item))
        print("removed file: {}".format(item))
