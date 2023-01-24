function sshi () {
    if ($null -ne $query){
        python cat_sshhost.py | fzf --query " $query $args"
    }else{
        python cat_sshhost.py | fzf
    }
    Write-Host ssh $target
    ssh $target
}