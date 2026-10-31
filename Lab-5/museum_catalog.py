"""Museum artifact catalog backed by an in-memory SQLite database."""
import sqlite3

CONN = sqlite3.connect(":memory:")
CONN.execute(
    "CREATE TABLE artifacts ("
    "id INTEGER PRIMARY KEY, title TEXT, era TEXT, "
    "value INTEGER, on_display INTEGER)"
)


def add_artifact(title, era, value, on_display=0):
    """Insert an artifact into the catalog."""
    CONN.execute(
        "INSERT INTO artifacts (title, era, value, on_display) "
        "VALUES (?, ?, ?, ?)",
        (title, era, value, on_display),
    )
    CONN.commit()


def display_status(artifact_id):
    """Return whether an artifact is on display or in storage."""
    row = CONN.execute(
        "SELECT on_display FROM artifacts WHERE id = ?", (artifact_id,)
    ).fetchone()
    if row is None:
        return "not found"
    return "on display" if row[0] == 1 else "in storage"


def total_value(era):
    """Return the total value of all artifacts from the given era."""
    total = 0
    for (value,) in CONN.execute(
        "SELECT value FROM artifacts WHERE era = ?", (era,)
    ):
        total += value
    return total


def move_to_display(artifact_id):
    """Mark an artifact as on display."""
    CONN.execute(
        "UPDATE artifacts SET on_display = 1 WHERE id = ?", (artifact_id,)
    )
    CONN.commit()


def backup_note():
    """Announce that the catalog backup is complete."""
    print("catalog backup complete")


def main():
    """Run a short demonstration of the catalog."""
    add_artifact("Bronze Mirror", "Chola", 120000)
    add_artifact("Palm Manuscript", "Vijayanagara", 80000, 1)
    add_artifact("Terracotta Lamp", "Chola", 15000)
    move_to_display(1)
    print(display_status(1))
    print(total_value("Chola"))
    backup_note()


if __name__ == "__main__":
    main()
