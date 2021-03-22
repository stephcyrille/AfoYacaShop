def read_file(file):
    file_path = file
    text = ""
    with open(file_path) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            line = fp.readline()
            text += line
            cnt += 1
    return text
