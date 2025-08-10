def save_file(file, path):
    with open(path, 'wb') as f:
        f.write(file.read())
