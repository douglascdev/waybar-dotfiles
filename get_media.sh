media=$(playerctl metadata --player=spotify,firefox,%any -f "({{playerName}}) {{artist}} - {{title}}")
player_status=$(playerctl status --player=spotify,firefox,%any)

if [[ $player_status = "Playing" ]]
then
    song_status=''
elif [[ $player_status = "Paused" ]]
then
    song_status=''
else
    song_status='Music stopped'
fi

echo -e "$song_status $media"
