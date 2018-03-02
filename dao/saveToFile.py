

class SaveToFile(object):
    """docstring for saveToFile"""
    def __init__(self):
        super(SaveToFile, self).__init__()

    @classmethod
    def saveToFileAsHtml(cls, file_name, contents):
        fh = open(file_name, 'w')
        fh.write(contents)
        fh.close()

    @classmethod
    def saveToFileAsLog(cls, file_name, contents):
        fh = open(file_name, 'a')
        currentTime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        fh.write(currentTime+'\n')
        fh.write(contents+'\n')
        fh.write('\n')
        fh.close()
