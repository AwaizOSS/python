import json

youtube_file = "youtube.txt"


def load_data():
    try:
        with open(youtube_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_data_helper(videos):
    with open(youtube_file, "w") as file:
        json.dump(videos, file)


def list_all_videos(videos):
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, duration: {video['time']}")


def add_video(videos):
    name = input("enter video name: ")
    time = input("enter video time: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)


def update_video(videos):
    list_all_videos(videos)
    index = int(input("enter the video number you want to update: "))
    if 1 <= index <= len(videos):
        name = input("enter the new video name: ")
        time = input("enter the new video time: ")
        videos[index - 1] = {"name": name, "time": time}
        save_data_helper(videos)
    else:
        print("invalid index selected")


def delete_video(videos):
    list_all_videos(videos)
    index = int(input("enter the video number you want to delete: "))
    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data_helper(videos)
    else:
        print("invalid index selected")


def main():
    # videos = [] working with this will be an assignment
    videos = load_data()
    while True:
        print("Youtube manager")
        print("\n1. list fav videos")
        print("2. add a youtube video")
        print("3. update a youtube video")
        print("4. delete a youtube video")
        print("5. exit the app")
        choice = input("enter ur choice: ")
        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("invalid choice")


if __name__ == "__main__":
    main()
