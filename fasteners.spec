#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : fasteners
Version  : 0.13.0
Release  : 7
URL      : https://pypi.python.org/packages/source/f/fasteners/fasteners-0.13.0.tar.gz
Source0  : https://pypi.python.org/packages/source/f/fasteners/fasteners-0.13.0.tar.gz
Summary  : A python package that provides useful locks.
Group    : Development/Tools
License  : Apache-2.0
Requires: fasteners-python
BuildRequires : extras
BuildRequires : monotonic-python
BuildRequires : nose
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six-python
BuildRequires : testtools

%description
Fasteners
=========
.. image:: https://travis-ci.org/harlowja/fasteners.png?branch=master
:target: https://travis-ci.org/harlowja/fasteners

%package python
Summary: python components for the fasteners package.
Group: Default

%description python
python components for the fasteners package.


%prep
%setup -q -n fasteners-0.13.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
nosetests-3.4
%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
