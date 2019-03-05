from setuptools import setup, find_packages

version = '0.1.0'

LONG_DESCRIPTION = """
Introduction
------------

NZB is an XML-based file format for retrieving posts from NNTP (Usenet) servers.
Since NZB is XML-based, it's relatively easy to build one-off parsers to parse
NZB files.  This project is an attempt to consolidate those many one-off NZB
parsers into one simple interface.

This package includes three implementations: one based on expat, another based
on ElementTree, and a final implementation based on lxml.  The order in which
they were listed is in order of compatibility.  The lxml version will work on all versions > 3.4, 
and lxml will only work if you have lxml installed.


A Note on Installing lxml
-------------------------

While lxml is not a requirement, I have had a hard time installing lxml in the
past.  I have found this set of commands to work perfectly::

    STATIC_DEPS=true easy_install 'lxml>=2.2beta4'
    STATIC_DEPS=true sudo easy_install 'lxml>=2.2beta4'


API Documentation
-----------------


Accessing the Default Parser
============================

Simply import nzb_parser from the pynzb package.  It's an instantiated version
of the fastest available parser that your system can support.


Other Parser Locations
======================

``ExpatNZBParser``:
    Available in the ``pynzb.expat_nzb`` namespace.

``ETreeNZBParser``:
    Available in the ``pynzb.etree_nzb`` namespace.

``LXMLNZBParser``:
    Available in the ``pynzb.lxml_nzb`` namespace.


Using the NZB Parser
====================

If you're using a specific parser, like the ``ETreeNZBParser``, you will first
have to instantiate it::

    nzb_parser = ETreeNZBParser()


Otherwise, you can just import the default parser for your system::

    from pynzb import nzb_parser


Then, simply call the ``parse`` method, giving it the xml string as the only
argument::

    files = nzb_parser.parse('<?xml ... my nzb file here ... </nzb>')


This will return a list of ``NZBFiles`` for you to use.


NZBFile Objects
===============

All of the parsers return ``NZBFile`` objects, which are objects with the
following properties:

``poster``:
    The name of the user who posted the file to the newsgroup.

``date``:
    A ``datetime.date`` representation of when the server first saw the file.

``subject``:
    The subject used when the user posted the file to the newsgroup.

``groups``:
    A list of strings representing the newsgroups in which this file may be
    found.

``segments``:
    A list of ``NZBSegment`` objects talking about where to get the contents
    of this file.


NZBSegment Objects
==================

Each ``NZBFile`` has a list of ``NZBSegment`` objects, which include information
on how to retrieve a part of a file.  Here's what you can find on an
``NZBSegment`` object:

``number``:
    The number of the segment in the list of files.

``bytes``:
    The size of the segment, in bytes.

``message_id``:
    The Message-ID of the segment (useful for retrieving the full contents)


Example
--------

In this example, we will grab an Ubuntu NZB and parse the file, printing out
some information about each file and its segments::

    from pynzb import nzb_parser
    from urllib2 import urlopen

    # Grab a sample Ubuntu NZB
    ubuntu_nzb = urlopen('http://media.eflorenzano.com/misc/sample-ubuntu-nzb.nzb').read()

    # Parse the NZB into files
    files = nzb_parser.parse(ubuntu_nzb)

    # Print out each file's subject and the first two segment message ids
    for nzb_file in files:
        print nzb_file.subject
        for segment in nzb_file.segments[:2]:
            print '    ' + segment.message_id
        if len(nzb_file.segments) > 2:
            print '    ...'
"""

setup(
    name='pynzb3',
    version=version,
    description="pynzb is a unified API for parsing NZB files, with several concrete implementations included",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='nzb,parser,xml',
    author='Eric Florenzano',
    author_email='floguy@gmail.com',
    url='http://github.com/pl77/pynzb3/tree/master',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools'],
)
