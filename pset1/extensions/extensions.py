file = input("File name: ").lower().strip()

index = file.rfind(".")
ending = file[index:]
match ending:
    case ".gif":
        print("image/gif")
    case ".jpg":
        print("image/jpeg")
    case ".jpeg":
        print("image/jpeg")
    case ".png":
        print("image/png")
    case ".txt":
        print("text/plain")
    case ".pdf":
        print("application/pdf")
    case ".zip":
        print("application/zip")
    case _:
        print("application/octet-stream")
    #make cases

    #use the file index as ending and then check to see in cases if exists and use accordingly
