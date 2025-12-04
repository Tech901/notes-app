"""
This program implements a simple command-line note-taking
app that stores its data in an SQLite database.

To create your database, run `sqlite3 notes.db`, then run the following SQL command:

    CREATE TABLE IF NOT EXISTS 'notes' (
        'id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
        'content' TEXT, 
        'added_on' DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
    CREATE TABLE sqlite_sequence(name,seq);

---- 

"""
import argparse
import sqlite3


class Notes:

    def __init__(self):
        self._db_name = "notes.db"
        self.conn = sqlite3.connect(self._db_name)
        self.cursor = self.conn.cursor()

    def close(self):  # Closes our database
        self.cursor.close()
        self.conn.close()

    def get_notes(self): # get all of our notes
        sql = "select * from notes"
        self.cursor.execute(sql)
        results = self.cursor.fetchall()  # [(1, 'note here', '2025-12-01...'), ]
        return results

    def print_notes(self): # print all of our notes
        for id, content, date in self.get_notes():
            print(f"{id}:{date} {content}")

    def get_note(self, note_id):  # get a *single* note
        sql = "select * from notes where id = ?"
        values = (note_id, )
        self.cursor.execute(sql, values)
        note = self.cursor.fetchone() # (id, content, date)
        return {
            "id": note[0],
            "content": note[1],
            "added_on": note[2],
        }

    def add_note(self, content): # add a *single* note
        sql = "insert into notes (content) values (?)"
        values = (content, ) # This is a tuple!
        self.cursor.execute(sql, values)
        self.conn.commit()
        print("Note saved.")

    def remove_note(self, note_id): # remove a *single* note
        sql = "delete from notes where id = ?"
        values = (note_id, )
        self.cursor.execute(sql, values)
        self.conn.commit()
        print(f"Note {note_id} was removed")


# Main program...
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Do stuff with notes")
    parser.add_argument(
        "-c",
        "--content",
        action="store",
        type=str,
        default=None,
        help="The content of the note to add."
    )
    parser.add_argument(
        "-d",
        "--delete",
        action="store",
        type=int,
        default=None,
        help="The ID of the note to delete."
    )
    parser.add_argument(
        "-n",
        "--note",
        action="store",
        type=int,
        default=None,
        help="The ID of the note you want to view."
    )

    args = parser.parse_args()

    # Create a Notes object
    notes = Notes()
    if args.content is not None:
        notes.add_note(args.content)
    elif args.delete is not None:
        notes.remove_note(args.delete)
    elif args.note is not None: #show the single note.
        n = notes.get_note(args.note)
        print(f"Note ID: {n['id']}")
        print(n['content'])
        print(f"Saved on: {n['added_on']}")
    else:
        notes.print_notes()
    notes.close()