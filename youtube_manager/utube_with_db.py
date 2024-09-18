import sqlite3

conn = sqlite3.connect("youtube_videos.db")
cursor = conn.cursor()
cursor.execute(
    """
    create table if not exists videos(
        id integer primary key,
        name text not null,
        time text not null
    )
"""
)


def list_all_videos():
    cursor.execute(
        "select * from videos"
    )  # if there are no records to show display something
    for row in cursor.fetchall():
        print(row)


def add_video():
    name = input("enter video name: ")
    time = input("enter video time: ")
    cursor.execute("insert into videos(name,time) values (?,?)", (name, time))
    conn.commit()


def update_video():
    list_all_videos()
    id = int(input("enter the video number you want to update: "))
    name = input("enter the new video name: ")
    time = input("enter the new video time: ")
    cursor.execute("update videos set name=?,time=? where id=?", (name, time, id))
    conn.commit()


def delete_video():
    list_all_videos()
    id = int(input("enter the video number you want to delete: "))
    cursor.execute(
        "delete from videos where id=?", (id,)
    )  # (id,) comma here is important as it only takes tuple as input


def main():
    while True:
        print("utube manager with db")
        print("\n1. list fav videos")
        print("2. add a youtube video")
        print("3. update a youtube video")
        print("4. delete a youtube video")
        print("5. exit the app")
        choice = input("enter ur choice: ")
        match choice:
            case "1":
                list_all_videos()
            case "2":
                add_video()
            case "3":
                update_video()
            case "4":
                delete_video()
            case "5":
                break
            case _:
                print("invalid choice")
    conn.close()


if __name__ == "__main__":
    main()
