# git 无法push远程仓库 Note about fast-forwards 问题解决





```bash
git remote add origin https://github.com/blime4/MyNote.git 
git branch --set-upstream-to=origin/master master
git pull origin master --allow-unrelated-histories
git push origin master
```

