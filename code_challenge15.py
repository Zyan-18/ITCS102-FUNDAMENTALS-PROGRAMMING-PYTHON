con = True
anime_list = []

while con == True:
    anime = input("Enter the title of the anime you wanted to add to your list (type 'exit' to finish): ")

    if anime.lower() == "exit":
        print("You have exited the anime entry program.")
        break
    else:
        print(f"'{anime}' has been added to your anime list.")
        anime_list.append(anime)

print("Your anime list includes:")
for title in anime_list:
    print(f"- {title}")