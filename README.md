#End2End-MLOps

-e . in requirements #(to automatically trigger setup.py)

python3 -m venv /Users/dushyantsharma/Desktop/awsfreetier/Data-science-projects/End2End-ML-Deployment-Ops/venv
python3 --version (Python 3.9.6)


git config --global user.name "dushyant"
git config --global user.email "dushyant.singh.civ16@itbhu.ac.in"


ls -al ~/.ssh (Check if your SSH key exists)
ssh-keygen -t rsa -b 4096 -C "dushyant.singh.civ16@itbhu.ac.in" (If you do not see id_rsa.pub, generate a new key)

eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa (SSH key is loaded for authentication.)


Go to GitHub → Settings → SSH and GPG keys → New SSH Key
cat ~/.ssh/id_rsa.pub 
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDSwwTt7X++/qaeBSVNXoCpG//K7+/++yLjlg3//++/JhCwd4Av93FiSQOErtjE4cFPKXtnJhwXKQK0kW0aKfRiT7D/+++== dushyant.singh.civ16@itbhu.ac.in

ssh -T git@github.com ->Hi dushyant4342! You've successfully authenticated, but GitHub does not provide shell access.


Start without Readme.md file on Github 
echo "# mlopsproject" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:dushyant4342/mlopsproject.git   --( git remote remove origin    )
git push -u origin main

git add .
