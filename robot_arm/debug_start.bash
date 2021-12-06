TIME=$(date)
echo "LOG is start from:"$TIME"-----------" | sudo tee -a std_out.log>/dev/null
python3 processControlMain.py &