import sqlite3

conn = sqlite3.connect('yt_videos.db')

cursor = conn.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS videos (
                   id INTEGER PRIMARY KEY ,
                   name TEXT NOT NULL,
                   time TEXT NOT NULL
               )
               ''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    table = cursor.fetchall()
    if len(table) == 0 :
        print("\n there is no video")
    for row in table:
        print(f"{row[0]}. {row[1]}  {row[2]}")

def add_videos(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)" , (name, time))
    conn.commit()

def update_videos(name, time, vid_id):
    cursor.execute(" UPDATE videos SET name = ? time = ? WHERE id = ?",(name, time, vid_id))
    conn.commit()

def delete_videos(del_id):
    cursor.execute("DELETE FROM videos WHERE id = ?",(del_id,))
    conn.commit()

def renumber_ids():
    cursor.execute("SELECT id FROM videos ORDER BY id")
    ids = [row[0] for row in cursor.fetchall()]
    for new_id, old_id in enumerate(ids, start=1):
        if new_id != old_id:
            cursor.execute("UPDATE videos SET id = ? WHERE id = ?", (new_id, old_id))
    conn.commit()
    
def main():
    while True:
        print("\n Youtube manager App")
        print("1. List all videos")
        print("2. Add a new videos")
        print("3. Update a videos")
        print("4. Delete a videos")
        print("5. Exit the app")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("enter the video name: ")
            time = input("enter the video time: ")
            add_videos(name, time)
        elif choice == '3':
            list_videos()
            vid_id = input("enter the video id to update")
            name = input('enter video name: ')
            time = input('enter video time: ')
            update_videos(vid_id, name, time)
        elif choice == '4':
            list_videos()
            vid_id = input("enter id to delete: ")
            delete_videos(vid_id)
            renumber_ids()
        elif choice == '5':
            break
        else :
            print("INVALID CHOICE")
    conn.close()

if __name__ == "__main__":
    main()
