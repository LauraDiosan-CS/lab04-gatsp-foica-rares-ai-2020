class Writer:
    def __init__(self, fileLocation):
        self.__fileLocation = fileLocation
        with open(self.__fileLocation, "w") as f:
            f.write("")

    def append(self, *lines):
        with open(self.__fileLocation, "a") as f:
            f.writelines(lines)