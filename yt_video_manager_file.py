import json 


text_file = "youtube.txt"

def list_all_videos(videos):
    print("\n")
    print("*" * 80)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration:{video['time']} ")
        
    print("\n")
    print("*" * 80)  
    print("here are all the videos")
    
def save_data_helper(videos):
    with open('text_file','w') as file:
        json.dump(videos,file)
        
        
def add_video(videos):
    name = input("enter video name : ")
    time = input("enter video time : ")
    videos.append({'name' : name, 'time' : time})
    save_data_helper(videos)
    print("*" * 80)
    print("\n")
    print("the video is added")
    print("*" * 80)
def update_video(videos):
    list_all_videos(videos)
    index = int(input("enter video no. to update "))
    if 1 <= index <= len(videos):
        name = input("enter the new video name : ")
        time = input("enter the new video time : ")
        videos[index - 1] = {'name':name ,'time': time }
        save_data_helper(videos)
        print("*" * 80)
        print("the video is updated")
        print("*" * 80)
    else:
        print("*" * 80)
        print("Invalid index selected")
        print("*" * 80)
def delete_video(videos):
    list_all_videos(videos)
    index = int(input("enter a video no. to be deleted : "))
    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data_helper(videos)
        print("*" * 80)
        print("the video is deleted")
        print("*" * 80)
    else:
        print("*" * 80)
        print("Invalid index selected")
        print("*" * 80)
        

def load_data():
    try:
        with open('text_file','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def main():
    videos = load_data()
    while True:
        print("\n Youtube manager App")
        print("1. List all videos")
        print("2. Add a new videos")
        print("3. Update a videos")
        print("4. Delete a videos")
        print("5. Exit the app")
        choice = input("Enter your choice: ")
        
        match choice:
            case '1':
                list_all_videos(videos)
                
            case '2':
                add_video(videos)
                
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice")
                
                
if __name__ == "__main__":
    main()
    
