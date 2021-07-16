gh repo create $1 -y --public
cd $1/
cp -r template/* .
git add .
git commit -m'init'
git branch gh-pages
git checkout gh-pages
git remote set-url origin https://MachineUserHallicopter:$2@github.com/MachineUserHallicopter/$1.git
git push -u origin gh-pages