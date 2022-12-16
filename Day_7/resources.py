from functools import reduce

class Dir:
    def __init__(self, name: str, parent_dir: 'Dir' = None):
        self.name = name
        self.parent_dir = parent_dir
        self.subdirs = []
        self.files = []

    def __repr__(self):
        return f'Name: {self.name} - Size: {self.getSize()}'

    def getParentDir(self) -> 'Dir':
        return self.parent_dir
    
    def getSubdir(self, dir_name: str) -> 'Dir':
        return next(dir for dir in self.subdirs if dir.hasName(dir_name))

    def hasName(self, dir_name: str) -> bool:
        return self.name == dir_name

    def addSubdir(self, subdir_name: str):
        new_dir = Dir(subdir_name, self)
        self.subdirs.append(new_dir)

    def addFile(self, file_name: str, file_size: int):
        new_file = File(file_name, file_size)
        self.files.append(new_file)

    def getSize(self) -> int:
        sub_resources = self.subdirs + self.files
        return reduce(lambda total_size, resource: total_size + resource.getSize(), sub_resources, 0)

    def getAllSubdirs(self) -> list:
        # Get a list of lists, needs flatting
        indirect_subdirs_lists = [subdir.getAllSubdirs() for subdir in self.subdirs]
        indirect_subdirs = [indirect_subdir for subdir_list in indirect_subdirs_lists for indirect_subdir in subdir_list ]

        return self.subdirs + indirect_subdirs

class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def getSize(self) -> int:
        return self.size
