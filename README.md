# RecipeProject
## Introduction
RecipeProject is a desktop app which allows user to add, edit, filter and read detailed info about meal recipes. I often tend to write my recipes in many different places (text files, notebooks, etc.) instead of saving them in one easily accessible place, so I decided to create an app that would allow me to keep all of my stuff in one place. This app was written in Python with usage of MVC design pattern. GUI was made with TKinter and serialization uses Python Pickle library.

Each recipe is represented by name, short description, type (breakfast, dinner, etc.), preparation time in minutes, calories, description, instruction and list of ingredients. Each ingredient has its own name, count and unit (tbs, cup, etc.).

## Example of usage
After running the application we will be presented with following window:

![image](https://user-images.githubusercontent.com/49364059/111043539-62c9ce00-8443-11eb-8917-c1c810f6cbaa.png)

On the top of the user interface you can see navigation bar and a button with "File" text. After clicking on this button user can choose to load or save recipes.
This window's main purpose is to filter and search recipes that were already saved. 
User can also choose different actions here:

Search - searches recipes with given boundaries and displays them on the list

Select - displays detailed information about selected recipe

Add new - displays window where user can create new recipe

### Creating recipes
After clicking on add new the following view will be presented to the user:

![image](https://user-images.githubusercontent.com/49364059/111043765-9c4f0900-8444-11eb-9479-df344f374437.png)

Here user can put desired information about this recipe, add and delete some ingredients (clicking + and - button) and choose picture (clicking picture button) and save the recipe (clicking tick button):

![image](https://user-images.githubusercontent.com/49364059/111043818-010a6380-8445-11eb-8c06-7363e19afb49.png)
![image](https://user-images.githubusercontent.com/49364059/111043821-04055400-8445-11eb-99df-9bd223257ce5.png)
![image](https://user-images.githubusercontent.com/49364059/111043824-08317180-8445-11eb-9347-5622457f2b8e.png)

### Filtering recipes
Now by entering some filter boundaries and clicking search button user can see all recipes that match given parameters:

![image](https://user-images.githubusercontent.com/49364059/111043954-f00e2200-8445-11eb-9ca3-ecd0d045aa38.png)

If none boundaries were given, all saved recipes will be displayed:

![image](https://user-images.githubusercontent.com/49364059/111043980-103de100-8446-11eb-8dd9-988d3073de49.png)

### Selecting, editing and deleting recipes
When recipes are displayed on the list (treeview), user can select desired recipe (selecting and clicking select) in order to get detailed information about it:

![image](https://user-images.githubusercontent.com/49364059/111044008-43807000-8446-11eb-9a7b-9d751001aa92.png)

After clicking on pencil icon user will be able to edit given recipe (change text, add and delete ingredients, change picture):

![image](https://user-images.githubusercontent.com/49364059/111044062-978b5480-8446-11eb-94e3-9f1a366bba5e.png)
![image](https://user-images.githubusercontent.com/49364059/111044064-9a864500-8446-11eb-9fab-5742b4770c5c.png)

Clicking tick button will save changes:

![image](https://user-images.githubusercontent.com/49364059/111044074-a6720700-8446-11eb-91ad-01965b516d73.png)

From here user can delete permanently chosen recipe by clicking trash bin button.
After deleting it can be seen that this recipe will no longer be displayed when searched:

![image](https://user-images.githubusercontent.com/49364059/111044102-d8836900-8446-11eb-9326-49efe95dc0d9.png)



