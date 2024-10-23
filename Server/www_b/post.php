<?php

// Set the current date in the desired format
$date = date('dMYHis');

// Retrieve the posted image data
$imageData = $_POST['cat'] ?? null;

if (!empty($imageData)) {
    // Log the reception of the image data
    error_log("[#] Cam file received" . PHP_EOL, 3, "Log.log");
}

try {
    // Read the path from the file 'path.txt'
    $mypath = file_get_contents("path.txt");

    if ($mypath === false) {
        throw new RuntimeException("Failed to read path.txt.");
    }

    // Process the image data by removing the metadata and decoding it
    $filteredData = substr($imageData, strpos($imageData, ",") + 1);
    $unencodedData = base64_decode($filteredData);

    if ($unencodedData === false) {
        throw new RuntimeException("Failed to decode the base64 image data.");
    }

    // Generate the file path where the image will be saved
    $myFile = $mypath . 'cam' . $date . '.png';

    // Attempt to open the file for writing
    $fp = fopen($myFile, 'wb') ?? throw new RuntimeException("Failed to open the file for writing.");

    // Write the decoded image data to the file
    if (fwrite($fp, $unencodedData) === false) {
        throw new RuntimeException("Failed to write image data to the file.");
    }

    // Ensure the file is closed after writing
    fclose($fp);

} catch (RuntimeException $e) {
    // Log any errors that occur during the process
    error_log("[!] Error: " . $e->getMessage() . PHP_EOL, 3, "error_log.log");
}

// Always terminate the script
exit();
?>
