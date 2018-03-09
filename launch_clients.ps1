$first = $args[0]

For ($i=0; $i -lt $first; $i++) {
    start powershell "python spawn_client.py"
}