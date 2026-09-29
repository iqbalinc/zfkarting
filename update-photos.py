import os, json
photos = sorted(['photos/' + f for f in os.listdir('photos')
                 if f.lower().endswith(('jpg', 'jpeg', 'png', 'gif', 'webp'))], reverse=True)
json.dump({'photos': photos}, open('photos.json', 'w'), indent=2)
print(len(photos), 'photos listed')
