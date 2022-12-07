from dataclasses import dataclass, field


@dataclass
class File:
    name: str
    size: int


@dataclass
class Directory:
    name: str
    parent_directory: 'Directory'
    files: dict[str, File] = field(default_factory=dict)
    directories: dict[str, 'Directory'] = field(default_factory=dict)

    def total_size(self) -> int:
        return sum(f.size for f in self.files.values()) + sum(d.total_size() for d in self.directories.values())

    def get_all_subdirectories(self) -> list['Directory']:
        result = []
        for directory in self.directories.values():
            result.append(directory)
            result.extend(directory.get_all_subdirectories())
        return result


class FileSystem:
    def __init__(self):
        self._root_directory = Directory('/', None)
        self.current_directory = self._root_directory

    def change_directory(self, path: str):
        match path:
            case '/':
                self.current_directory = self._root_directory
            case '..':
                self.current_directory = self.current_directory.parent_directory
            case name:
                self.current_directory = self.current_directory.directories[name]

    def create_directory(self, dir_name: str):
        if dir_name not in self.current_directory.directories:
            self.current_directory.directories[dir_name] = Directory(dir_name, self.current_directory)

    def create_file(self, file_name: str, file_size: int):
        if file_name not in self.current_directory.files:
            self.current_directory.files[file_name] = File(file_name, file_size)

    def get_all_directories(self) -> list[Directory]:
        return [self._root_directory] + self._root_directory.get_all_subdirectories()


with open('input') as f:
    terminal_output = [line.strip() for line in f]

fs = FileSystem()
current_line_num = 0
while current_line_num < len(terminal_output):
    current_line = terminal_output[current_line_num]
    match current_line.split():
        case ['$', 'cd', path]:
            fs.change_directory(path)
            current_line_num += 1
        case ['$', 'ls']:
            current_line_num += 1
            while current_line_num < len(terminal_output) and (current_line := terminal_output[current_line_num])[0] != '$':
                match current_line.split():
                    case ['dir', dir_name]:
                        fs.create_directory(dir_name)
                    case [num, file_name]:
                        fs.create_file(file_name, int(num))

                current_line_num += 1

all_directories = fs.get_all_directories()
print(f'Part 1: {sum(d.total_size() for d in fs.get_all_directories() if d.total_size() <= 100000)}')

all_directories.sort(key=lambda d: d.total_size())
used_disk_space = all_directories[-1].total_size()  # Last element is the root
minimum_space_to_free = 30000000 - (70000000 - used_disk_space)
first_matching_directory = next(d for d in all_directories if d.total_size() > minimum_space_to_free)

print(f'Part 2: {first_matching_directory.total_size()}')