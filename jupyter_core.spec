#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jupyter_core
Version  : 4.9.1
Release  : 51
URL      : https://files.pythonhosted.org/packages/78/fa/a949d1f0d2aaaef1890c2ab7fee9e58ed7cc6301ebc26c0afbffff4ea6e3/jupyter_core-4.9.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/78/fa/a949d1f0d2aaaef1890c2ab7fee9e58ed7cc6301ebc26c0afbffff4ea6e3/jupyter_core-4.9.1.tar.gz
Summary  : Jupyter core package. A base package on which Jupyter projects rely.
Group    : Development/Tools
License  : BSD-3-Clause BSD-3-Clause-Clear
Requires: jupyter_core-bin = %{version}-%{release}
Requires: jupyter_core-license = %{version}-%{release}
Requires: jupyter_core-python = %{version}-%{release}
Requires: jupyter_core-python3 = %{version}-%{release}
Requires: traitlets
BuildRequires : buildreq-distutils3
BuildRequires : jupyter_core
BuildRequires : pytest
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
Provides: pypi(jupyter_core)
Requires: pypi(traitlets)

%description python3
python3 components for the jupyter_core package.


%prep
%setup -q -n jupyter_core-4.9.1
cd %{_builddir}/jupyter_core-4.9.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635431206
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/jupyter_core
cp %{_builddir}/jupyter_core-4.9.1/COPYING.md %{buildroot}/usr/share/package-licenses/jupyter_core/caf2cfb9faff40412b9975dec725e241814cc46b
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
/usr/share/package-licenses/jupyter_core/caf2cfb9faff40412b9975dec725e241814cc46b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
