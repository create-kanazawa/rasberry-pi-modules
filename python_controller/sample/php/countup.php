<?php
$fileName = './count.txt';
$count = 0;
if(is_readable($fileName)){
    $count = file_get_contents($fileName);
}
$count++;
echo $count;
file_put_contents($fileName, $count);
?>
