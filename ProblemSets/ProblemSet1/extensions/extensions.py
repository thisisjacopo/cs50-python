file_name = input("Enter a file name: ")
file_name = file_name.lower().strip()

extension = file_name.split(".")[-1]

match extension:
    case "jpeg":
        print("image/jpeg")
    case "jpg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "gif":
        print("image/gif")
    case "txt":
        print("text/plain")
    case "pdf":
        print("application/pdf")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")
