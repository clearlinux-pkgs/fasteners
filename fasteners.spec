#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : fasteners
Version  : 0.16.3
Release  : 57
URL      : https://files.pythonhosted.org/packages/28/e4/2888d41cdbd405828ccdb9a8536c5919939c2f4c6ab9b2ba63e9bd2570d5/fasteners-0.16.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/28/e4/2888d41cdbd405828ccdb9a8536c5919939c2f4c6ab9b2ba63e9bd2570d5/fasteners-0.16.3.tar.gz
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
Requires: pypi(six)

%description python3
python3 components for the fasteners package.


%prep
%setup -q -n fasteners-0.16.3
cd %{_builddir}/fasteners-0.16.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1636476284
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
cp %{_builddir}/fasteners-0.16.3/LICENSE %{buildroot}/usr/share/package-licenses/fasteners/987f2e77cc1fa9c15dc5b849c5fbd7534407bb2a
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
