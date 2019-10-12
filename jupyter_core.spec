#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jupyter_core
Version  : 4.6.0
Release  : 27
URL      : https://files.pythonhosted.org/packages/a4/47/e852cd00ae811939201b7f8118a856f2c6a52db3b31c4185ffbc098405c7/jupyter_core-4.6.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/a4/47/e852cd00ae811939201b7f8118a856f2c6a52db3b31c4185ffbc098405c7/jupyter_core-4.6.0.tar.gz
Summary  : Jupyter core package. A base package on which Jupyter projects rely.
Group    : Development/Tools
License  : BSD-3-Clause-Clear
Requires: jupyter_core-bin = %{version}-%{release}
Requires: jupyter_core-license = %{version}-%{release}
Requires: jupyter_core-python = %{version}-%{release}
Requires: jupyter_core-python3 = %{version}-%{release}
Requires: traitlets
BuildRequires : buildreq-distutils3
BuildRequires : traitlets
BuildRequires : traitlets-python

%description
# Jupyter Core
Core common functionality of Jupyter projects.
This package contains base application classes and configuration inherited by other projects.
It doesn't do much on its own.

%package bin
Summary: bin components for the jupyter_core package.
Group: Binaries
Requires: jupyter_core-license = %{version}-%{release}

%description bin
bin components for the jupyter_core package.


%package license
Summary: license components for the jupyter_core package.
Group: Default

%description license
license components for the jupyter_core package.


%package python
Summary: python components for the jupyter_core package.
Group: Default
Requires: jupyter_core-python3 = %{version}-%{release}

%description python
python components for the jupyter_core package.


%package python3
Summary: python3 components for the jupyter_core package.
Group: Default
Requires: python3-core

%description python3
python3 components for the jupyter_core package.


%prep
%setup -q -n jupyter_core-4.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1570907025
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/jupyter_core
cp COPYING.md %{buildroot}/usr/share/package-licenses/jupyter_core/COPYING.md
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jupyter
/usr/bin/jupyter-migrate
/usr/bin/jupyter-troubleshoot

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/jupyter_core/COPYING.md

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
