import requests
from dataclasses import dataclass


@dataclass
class data_structure:
        user_dictionnary : dict[int,list[list]] # int for user, list for list of content

def dict_isempty(d:data_structure)-> bool:
        return d.user_dictionnary == {} 

def dict_size_user(d:data_structure) -> int :
        
    if dict_isempty(d):
        return 0
    
    else :
        return len(d.user_dictionnary)
    
def dict_new() -> data_structure:

    new_user_dictionnary : dict[int, list] = {}

    new_data_structure : data_structure = data_structure(
         user_dictionnary=new_user_dictionnary
    )

    return new_data_structure
            

def dict_fetch_all(d:data_structure,url): # we asssume url is /posts and not /posts/1 or smth
    url = url              
    response = requests.get(url)
    data = response.json() # si on utilise posts seulement, data devient une liste de dictionaire

    for e in data:
        #print(e,'\n') # e est un dictionnaire

        user_id : int = e['userId'] #on récupère  les éléments du dictionnaire
        id : int = e['id']
        title : str = e['title']
        body : str = e['body']

        #print(user_id,id,title,'\n','content : ',body,'\n')

        new_user_content = [id,title,body] # on les mets dans une liste

        user_content : list[list] = []

        if user_id not in d.user_dictionnary: 

            d.user_dictionnary[user_id] =user_content  # on met la liste de liste dans le dictionnaire
            d.user_dictionnary[user_id].append(new_user_content)  

        else :
            d.user_dictionnary[user_id].append(new_user_content)     

        
def dict_post(d: data_structure, url, userId : int, id: int,title:str,body:str):
     
     new_post = {
          
        "UserId" : userId,
        "id" : id,
        "title" : title,
        "body" : body
     }

     response = requests.post(url,new_post)

     if response.status_code == 201:
          
        if userId not in d.user_dictionnary:
             
             d.user_dictionnary[userId] = []
             d.user_dictionnary[userId].append([str(id),title,body])

             print( d.user_dictionnary[userId])

        else :
            d.user_dictionnary[userId].append([str(id),title,body])
            print( d.user_dictionnary[userId])

     else :
          
          raise ValueError("request not accepted")

     
         


if __name__=='__main__':
    
    url = 'https://jsonplaceholder.typicode.com/posts'

    a = dict_new()
    dict_fetch_all(a,url)

    dict_post(a,url,1,11,"lol","lmao")

    pass