print "Enter a string: ";
$str = <STDIN>;
print $str;
if ( $str =~ /\w/) {
    chomp($str);
    $str =~ s/\W//g;
    $str = lc($str);
    if ( $str eq reverse($str) ) {
        print "The string is a polindrome!\n";
    } else {
        print "The string is not a polindrome.\n";
    }  
} else {
        print "You didn't enter a string!\n";
    }