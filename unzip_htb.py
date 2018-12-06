from zipfile import ZipFile


def getArchiveName(zip_file):
    #This function return the list of names in the archive.
    with ZipFile(zip_file, 'r') as f:
        names = f.namelist()
    return str(names[0])


   


def main():
    zip_file = "Eternal_Loop.zip"
    password = "hackthebox"

    while True:
        print("[+]Extracting \033[35m {0} \033[0m with password \033[36m {1}\
              \033[0m".format(zip_file, password))
        with ZipFile(zip_file) as archive:
            archive.extractall(pwd=bytes(password, "utf8"))

        zip_file = getArchiveName(zip_file)
        password = getArchiveName(zip_file)
        password = password.replace('.zip', '').replace('\n', '')

if __name__ == "__main__":
    main()
