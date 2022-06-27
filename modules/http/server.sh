
echo "Enter your ip address: "
read ip

python -m http.server 8000 -b $ip
