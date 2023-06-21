# Daz Assert ABFD (All In One)

This repo allows you to download and manage all Assert projects needed for 3D development of ABFD.

## Installation 
Install [Git](https://git-scm.com/)
```shell
git clone https://github.com/DRincs-Productions/daz-assert-ABFD-all-in-one 'DAZ_3D'
cd DAZ_3D
git submodule update --init --recursive
```
After that use [GitHub Desktop](https://desktop.github.com/) and [open the folder](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/adding-and-cloning-repositories/adding-a-repository-from-your-local-computer-to-github-desktop).

## Connect them to daz:
1) In Daz Open `Edit/Preferences/Content/Content Dictionary Manager...`      
 ![image](https://user-images.githubusercontent.com/67595890/187970556-73c7c9a1-7def-4efe-ab4e-24f6a12e0f1e.png)      
 ![image](https://user-images.githubusercontent.com/67595890/215262986-ae27c921-87e4-48d1-9414-bdf3acad6625.png)         
2) creates a working environment
3) select it
4) click on Daz Studio Format
5) Add all the assert paths you downloaded. (make sure they are all) + **'My DAZ 3D Library'** folder (the deafult folder of daz)
![image](https://user-images.githubusercontent.com/67595890/190847307-1c821678-2014-4d54-af2a-709c373c6abe.png)
 
## Test
Now in the folder 'ABFD assert' open  MC       
![image](https://user-images.githubusercontent.com/67595890/190847401-7fa7b8e8-d41e-4f5d-a0a0-c36b0027d59f.png)     
it doesn't see give you errors otherwise you did something wrong.      




## Add assert
`git submodule add <link> '<Neme Folder>'`

## Update assert
`git submodule update --remote`

## Remove assert
`git rm '<Neme Folder>'`
