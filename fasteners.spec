#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : fasteners
Version  : 0.15
Release  : 52
URL      : https://files.pythonhosted.org/packages/15/d7/1e8b3270f21dffcaaf5a2889675e8b2fa35f8a43a5817a31d3820e8e9495/fasteners-0.15.tar.gz
Source0  : https://files.pythonhosted.org/packages/15/d7/1e8b3270f21dffcaaf5a2889675e8b2fa35f8a43a5817a31d3820e8e9495/fasteners-0.15.tar.gz
Summary  : A python package that provides useful locks.
Group    : Development/Tools
License  : Apache-2.0
Requires: fasteners-license = %{version}-%{release}
Requires: fasteners-python = %{version}-%{release}
Requires: fasteners-python3 = %{version}-%{release}
Requires: monotonic
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : extras
BuildRequires : monotonic
BuildRequires : nose
BuildRequires : six
BuildRequires : testtools
Patch1: deps.patch

%description
=========

%package license
Summary: license components for the fasteners package.
Group: Default

%description license
license components for the fasteners package.


%package python
Summary: python components for the fasteners package.
Group: Default
Requires: fasteners-python3 = %{version}-%{release}

%description python
python components for the fasteners package.


%package python3
Summary: python3 components for the fasteners package.
Group: Default
Requires: python3-core
Provides: pypi(fasteners)
Requires: pypi(monotonic)
Requires: pypi(six)

%description python3
python3 components for the fasteners package.


%prep
%setup -q -n fasteners-0.15
cd %{_builddir}/fasteners-0.15
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603391945
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/fasteners
cp %{_builddir}/fasteners-0.15/LICENSE %{buildroot}/usr/share/package-licenses/fasteners/987f2e77cc1fa9c15dc5b849c5fbd7534407bb2a
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/fasteners/987f2e77cc1fa9c15dc5b849c5fbd7534407bb2a

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
