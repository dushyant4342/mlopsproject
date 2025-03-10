#End2End-MLOps

python3 -m venv /Users/dushyantsharma/Desktop/awsfreetier/Data-science-projects/End2End-ML-Deployment-Ops/venv
python3 --version (Python 3.9.6)


git config --global user.name "dushyant"
git config --global user.email "dushyant@fplabs.tech"


ls -al ~/.ssh (Check if your SSH key exists)
ssh-keygen -t rsa -b 4096 -C "dushyant.singh.civ16@itbhu.ac.in" (If you do not see id_rsa.pub, generate a new key)

Start without Readme.md file on Github
echo "# mlopsproject" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:dushyant4342/mlopsproject.git   --( git remote remove origin    )
git push -u origin main

