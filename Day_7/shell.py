from resources import Dir

class Shell:
    def __init__(self):
        self.main_dir = Dir("/")
        self.current_dir = self.main_dir

    def command(self, command: str):
        if command.startswith("$ cd"):
            dir_name = command.split(" ").pop()
            self.changeDirectory(dir_name)
        
        elif not command.startswith("$ ls"):
            if command.startswith("dir "):
                dir_name = command.split(" ").pop()
                self.current_dir.addSubdir(dir_name)
            else:
                file_data = command.split(" ")
                file_size = int(file_data[0])
                file_name = file_data[1]
                self.current_dir.addFile(file_name, file_size)

    def changeDirectory(self, dir_name: str):
        if dir_name == "/":
            self.current_dir = self.main_dir
        elif dir_name == "..":
            self.current_dir = self.current_dir.getParentDir()
        else:
            self.current_dir = self.current_dir.getSubdir(dir_name)
