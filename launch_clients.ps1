$first = $args[0]
$second = $args[1]
For ($i=0; $i -lt $first; $i++) {
    start powershell "python spawn_client.py $second"
}