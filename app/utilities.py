ALLOWED_EXTENSIONS = ['txt', 'xml']


# function to check whether a file is a type of file that is acceptable
def file_allowed(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS





