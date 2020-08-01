import os,glob

# list_of_files = ['/home/pravesh/THM/Cyber-Challenges/hacktivityCon2020/popsi/dec.py','/home/pravesh/THM/Cyber-Challenges/hacktivityCon2020/popsi/dec.sh']

while True:
    # n_list_of_files = glob.glob("/home/pravesh/THM/Cyber-Challenges/hacktivityCon2020/popsi/*")
    # f = list(set(n_list_of_files) - set(list_of_files))
    # print(f) 
    # e = f[0]
    e = "73bd8e.zip"
    if len(e.split('.')) != 2:
        print("renaming file")
        header = open(e,"rb").read()[0:4].hex().lower()
        if header == "1f8b0808":
            print("gzip ...")
            os.rename(e,e+".gz")
            e += ".gz"
        elif header == "fd377a58":
            print("xz ...")
            os.rename(e,e+".xz")
            e += ".xz"
        elif header == "425a6839":
            print("bzip2 ...")
            os.rename(e,e+".bz2")
            e += ".bz2"
        elif header == "504b0304":
            print("zip ...")
            os.rename(e,e+".zip")
            e += ".zip"

    print("Decompressing" + e)
    os.system("./dec.sh "+e)

    # list_of_files = n_list_of_files





