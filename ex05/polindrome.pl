print "Enter a string: ";
$str = <STDIN>;
if ( $str ) {
    chomp($str);
    $str = lc($str);
    if ( $str eq reverse($str) ) {
        print "The string is a polindrome!\n";
    } else {
        print "The string is not a polindrome.\n";
    }  
} else {
        print "You didn't enter a string!\n";
    }