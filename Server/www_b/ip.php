<?php

// Function to get the client's IP address with proper validation
function getUserIP(): string {
    if (!empty($_SERVER['HTTP_CLIENT_IP']) && filter_var($_SERVER['HTTP_CLIENT_IP'], FILTER_VALIDATE_IP)) {
        return $_SERVER['HTTP_CLIENT_IP'];
    } elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR'])) {
        // In case there are multiple forwarded IPs, take the first valid one
        $forwardedFor = explode(',', $_SERVER['HTTP_X_FORWARDED_FOR']);
        foreach ($forwardedFor as $ip) {
            $trimmedIp = trim($ip);
            if (filter_var($trimmedIp, FILTER_VALIDATE_IP)) {
                return $trimmedIp;
            }
        }
    }
    return $_SERVER['REMOTE_ADDR'] ?? 'UNKNOWN';
}

// Get user's IP address
$ipAddress = getUserIP() . "\r\n";

// Get and sanitize User-Agent using htmlspecialchars to prevent XSS
$userAgent = "User-Agent: " . htmlspecialchars($_SERVER['HTTP_USER_AGENT'] ?? 'Unknown') . "\r\n";

// File path to log IP and User-Agent
$file = 'ip.txt';

// Log entry combining IP and User-Agent
$logEntry = "IP: " . $ipAddress . $userAgent;

try {
    // Use nullsafe operator (PHP 8) to avoid warnings if fopen fails
    $fp = fopen($file, 'a') ?? throw new RuntimeException("Failed to open the file.");
    
    // Write the log entry and handle potential errors in writing
    if (fwrite($fp, $logEntry) === false) {
        throw new RuntimeException("Failed to write to the file.");
    }
    
    // Ensure the file is closed after writing
    fclose($fp);
} catch (RuntimeException $e) {
    // Log the error if something goes wrong
    error_log($e->getMessage());
}

?>
