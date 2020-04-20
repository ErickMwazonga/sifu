<?php 
/**
 * You need to create a function that will validate if given parameters are valid geographical coordinates.
 * Valid coordinates look like the following: "23.32353342, -32.543534534". 
 * The return value should be either true or false.
 
 * Latitude (which is first float) can be between 0 and 90, positive or negative. 
 * Longitude (which is second float) can be between 0 and 180, positive or negative.
 
 * Coordinates can only contain digits, or one of the following symbols (including space after comma) _ -, . _
 * There should be no space between the minus "-" sign and the digit after it.
 
 * Here are some valid coordinates:
 * -23, 25
 * 24.53525235, 23.45235
 * 04, -23.234235
 * 43.91343345, 143
 * 4, -3
 
 * And some invalid ones:
 * 23.234, - 23.4234
 * 2342.43536, 34.324236
 * N23.43345, E32.6457
 * 99.234, 12.324
 * 6.325624, 43.34345.345
 * 0, 1,2
 * 0.342q0832, 1.2324
 */

function isValidCoordinates2($coordinates) {
    $valid = true;

    foreach ($coordinates as $key => $coordinate) {
        $has_space_after_dash = preg_match('/- +/', $coordinate);
        $has_underscore = preg_match('/_/', $coordinate);
        $has_invalid_chars = preg_match('/(_|- +)/', $coordinate);

        if ($has_space_after_dash or $has_underscore) {
            $valid = false;
            break;
        }

        list($latitude, $longitude) = explode(',', $coordinate);

        if(!is_numeric($latitude) or !is_numeric($longitude)) {
            $valid = false;
            break;
        }
        
        $valid_latitude = $latitude >= -90 and $latitude <= 90;
        $valid_longitude = $latitude >= -180 and $latitude <= 180;

        if (!$valid_latitude or !$valid_longitude) {
            $valid = false;
            break;
        }
    }

    echo($valid);
    return $valid;
}


$invalidCoords = [
    "23.234, - 23.4234",
    "2342.43536, 34.324236",
    "N23.43345, E32.6457",
    "99.234, 12.324",
    "6.325624, 43.34345.345",
    "0, 1,2",
    "0.342q0832, 1.2324",
    "23.245, 1e1"
  ];

$validCoords = [
    '-23, 25',
    '24.53525235, 23.45235',
    '04, -23.234235',
    '43.91343345, 143',
    '4, -3'
];

// isValidCoordinates2($invalidCoords);
// isValidCoordinates2($validCoords);

// foreach($invalidCoords as $c){
//     isValidCoordinates2($c);
//  }

echo(preg_match('/(_|- +)/', 'asa- sa'));
// $has_space_after_dash = preg_match('/- +/', $coordinate);
// $has_underscore = preg_match('/_/', $coordinate);

// echo(preg_match('/_/', 'asa_sa'));