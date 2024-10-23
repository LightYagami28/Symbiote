<?php

// Check if the IP logging script exists before including it
if (file_exists('ip.php')) {
    include 'ip.php';
} else {
    // Log the error and display a message if the file is missing
    error_log("[!] Error: ip.php not found." . PHP_EOL, 3, "error_log.log");
    exit("Error: Required file not found.");
}

// Redirect to index2.html
header('Location: index2.html');
exit();
?>
