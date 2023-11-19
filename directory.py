class Directory:
    def __init__(self) -> None:
        self.dir = [{"state": 2, "owner": 0, "sharer_list": [0 for _ in range(4)]} for _ in range(64)]

class DirectoryController:
    def __init__(self) -> None:
        self.dir = Directory()

    