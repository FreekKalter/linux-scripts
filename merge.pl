#!/home/fkalter/perl

use v5.16;
use strict;
use warnings;

use Cwd;
use File::Find;
use Path::Class;
use File::Copy;

my $baseDir = shift || getcwd;
$baseDir = dir( File::Spec->rel2abs($baseDir) );
chdir $baseDir;

finddepth( \&wanted, $baseDir );

sub wanted {
## Please see file perltidy.ERR
    if ( -d && /^\.{1,2}./ ) {
        $File::Find::prune = 1;
        return;
    }

    if ( -f && !/^\.{1,2}/ ) {
        move( $File::Find::name, $baseDir ) or die "Could not move $_: $!";
    }

    if ( -d && !/^\.{1,2}$/ ) {
        rmdir($File::Find::name) or die "Could not remove $_ :$!";
    }
}
