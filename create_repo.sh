cd ../build
gh repo create $1 -y --public
echo 'Created repo'
git init
git add .
echo 'Added template'
git commit -m'init'
git branch gh-pages
git checkout gh-pages
echo 'Setting remote'
#git remote remove origin
git remote add origin https://MachineUserHallicopter:$2@github.com/MachineUserHallicopter/$1.git
git push -u origin gh-pages
echo 'Pushed and done'