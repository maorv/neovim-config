import sys
import os
import re



def newCLanguageFile( filename ):
    LICENSE = '''/*
 * Copyright (c) 2016 Lightbit Labs Inc.
 *
 * This program is free software; you can redistribute it and/or modify it
 * under the terms and conditions of the GNU General Public License,
 * version 2, as published by the Free Software Foundation.
 *
 * This program is distributed in the hope it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
 * FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
 * more details.
 */'''

    assert filename.endswith( ".h" ) or filename.endswith( ".c" )
    withoutExtension = os.path.splitext( filename )[ 0 ]
    parts = withoutExtension.split( os.path.sep )
    className = parts[-1]
    assert className.replace( "Test_", "test_" ) == className.lower(), \
            "directories and filenames in the 'c/' folder should only contain lower case letters and underscores"
    protectMacro = "__" + className.upper() + "_H__"

    def printNewHeaderFile():
        print LICENSE
        print "#ifndef %s" % protectMacro
        print "#define %s" % protectMacro
        print "#endif /* %s */" % protectMacro
    
    def printNewCFile():
        print LICENSE

    if filename.endswith( ".c" ):
        printNewCFile()
    elif parts[ -1 ].startswith( "Test_" ):
        printNewTestSuiteFile( "Test_" + className )
    else:
        printNewHeaderFile()

def printNewTestSuiteFile( className ):
    print "#include <cxxtest/TestSuite.h>"
    print ""
    print "#define VOODOO_EXPECT_"
    print ""
    print '#include "TestLibrariesThatHave VOODOO_EXPECT"'
    print ''
    print '#include "TestedFile"'
    print ''
    print '#include "TestLibraries"'
    print ''
    print 'using namespace VoodooCommon::Expect;'
    print 'using namespace VoodooCommon::Expect::Parameter;'
    print ''
    print 'class %s : public CxxTest::TestSuite' % className
    print '{'
    print 'public:'
    print '\tAlways * always;'
    print ''
    print '\tvoid setUp()'
    print '\t{'
    print '\t\talways = new Always;'
    print '\t}'
    print ''
    print '\tvoid tearDown()'
    print '\t{'
    print '\t\tdelete always;'
    print '\t}'
    print ''
    print '\tvoid test_Normal()'
    print '\t{'
    print '\t}'
    print '};'

def newHFile( filename ):
    def makeWords( parts ):
        result = []
        for part in parts:
            result += re.findall( r"[A-Z]+[^A-Z]*", part )
        return result

    assert filename.endswith( ".hpp" )
    filename = os.path.splitext( filename )[ 0 ]
    parts = filename.split( os.path.sep )
    words = makeWords( parts )
    project = os.environ.get( "PROJECT_NAME", None )
    words = words if project is None else [ project ] + words

    protectMacro = "__" + "_".join( [ w.upper() for w in words ] ) + "_HPP__"
    className = parts[ -1 ]
    namespaces = parts[ 1 : -1 ] if project is None else [ project ] + parts[ 1 : -1 ]

    def printNewHeaderFile():
        print "#ifndef %s" % protectMacro
        print "#define %s" % protectMacro
        print ""
        for namespace in namespaces[ : -1 ]:
            print 'namespace %s {' % namespace
        if len( parts ) > 1:
            print 'namespace %s\n{' % parts[ -2 ]
        print ""
        print "class %s" % className
        print "{"
        print "public:"
        print "private:\n"
        print "\t%s( const %s & rhs ) = delete;" % ( className, className )
        print "\t%s & operator= ( const %s & rhs ) = delete;" % ( className, className )
        print "};"
        print ""
        for namespace in reversed( namespaces ):
            print "} // namespace %s" % namespace
        print ""
        print "#endif // %s" % protectMacro

    if className.startswith( "Test_" ):
        printNewTestSuiteFile( className )
    else:
        printNewHeaderFile()

filename = sys.argv[ 1 ]
if filename.endswith( ".h" ) or filename.endswith( ".c" ):
    newCLanguageFile( filename )
else:
    newHFile( filename )
