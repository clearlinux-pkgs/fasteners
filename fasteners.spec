#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : fasteners
Version  : 0.14.1
Release  : 24
URL      : http://pypi.debian.net/fasteners/fasteners-0.14.1.tar.gz
Source0  : http://pypi.debian.net/fasteners/fasteners-0.14.1.tar.gz
Summary  : A python package that provides useful locks.
Group    : Development/Tools
License  : Apache-2.0
Requires: fasteners-python3
Requires: fasteners-python
Requires: six
BuildRequires : extras
BuildRequires : nose
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : testtools
Patch1: deps.patch

%description
=========

%package python
Summary: python components for the fasteners package.
Group: Default
Requires: fasteners-python3

%description python
python components for the fasteners package.


%package python3
Summary: python3 components for the fasteners package.
Group: Default
Requires: python3-core

%description python3
python3 components for the fasteners package.


%prep
%setup -q -n fasteners-0.14.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1517765408
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
