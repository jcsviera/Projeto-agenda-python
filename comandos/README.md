iniciar o projeto Django

py - m venv venv 
.\venv\Scripts\activate
pip install django
django-admin startproject project . 
py manage.py


configurar o git 
git config --global user.name  'Seu nome'
git config --global user.email 'seu email'
git config --global init.defaultBranch main

#configure o gitignore
git init 
git add . 
git commit -m 'messagem'


#cria um novo repositorio no git hub 
git remote add origin 'nomeprojeto'
#apenas na primeira vez depois pode usar só o git push
git push origin main -u


