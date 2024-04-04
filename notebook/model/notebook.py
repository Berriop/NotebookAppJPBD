import dataclasses
from datetime import datetime


@dataclasses.dataclass
class Note:
    def __init__(self, code: int, title: str, text: str, importance: str):
        self.HIGH: str = "HIGH"
        self.MEDIUM: str = "MEDIUM"
        self.LOW: str = "LOW"
        self.code: int = code
        self.title: str = title
        self.text: str = text
        self.importance: str = importance
        self.creation_date: datetime = dataclasses.field(default_factory=datetime.now)
        self.tags: list[str] = dataclasses.field(default_factory=list)

    def __str__(self) -> str:
        return f"Code: {self.code} \nCreation date: {self.creation_date} \n{self.title}: {self.text}"

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)


@dataclasses.dataclass
class Notebook:
    def __init__(self):
        self.note_counter = 0
        self.tags = None
        self.notes = None

    def add_note(self, title: str, text: str, importance: str):
        self.note_counter += 1
        note = Note(
            code=self.note_counter,
            title=title,
            text=text,
            importance=importance
        )
        self.notes.append(note)
        return self.note_counter

    def important_notes(self) -> list[Note]:
        return [note for note in self.notes if note.importance == "HIGH" or note.importance == "MEDIUM"]

    def tags_note_count(self) -> dict[str, int]:
        note_count = dict()
        for note in self.tags:
            note_count[note] = note_count.get(note, 0) + 1
        return note_count
