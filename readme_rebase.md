# How to rebase with wendlers branch

`git remote add wendlers https://github.com/wendlers/mpfshell.git`
`git remove -v`
origin  https://github.com/hmaerki/mpfshell2.git (fetch)
origin  https://github.com/hmaerki/mpfshell2.git (push)
wendlers        https://github.com/wendlers/mpfshell.git (fetch)
wendlers        https://github.com/wendlers/mpfshell.git (push)

`git fetch wendlers`

`git rebase wendlers/master`
`git push --force`
