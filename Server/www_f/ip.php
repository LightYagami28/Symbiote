<?php

// Function to get the client's IP address
function getClientIp() {
    if (!empty($_SERVER['HTTP_CLIENT_IP'])) {
        return $_SERVER['HTTP_CLIENT_IP'];
    } elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR'])) {
        return $_SERVER['HTTP_X_FORWARDED_FOR'];
    } else {
        return $_SERVER['REMOTE_ADDR'];
    }
}

// Gather user agent information
$userAgent = $_SERVER['HTTP_USER_AGENT'];

// Prepare data to be logged
$ipAddress = getClientIp();
$logEntry = sprintf("IP: %s\nUser-Agent: %s\n", $ipAddress, $userAgent);

// File to log the IP and User-Agent
$logFile = 'ip.txt';

// Log the information
file_put_contents($logFile, $logEntry, FILE_APPEND | LOCK_EX);
?>
