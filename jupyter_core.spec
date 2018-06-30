#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jupyter_core
Version  : 4.4.0
Release  : 20
URL      : http://pypi.debian.net/jupyter_core/jupyter_core-4.4.0.tar.gz
Source0  : http://pypi.debian.net/jupyter_core/jupyter_core-4.4.0.tar.gz
Summary  : Jupyter core package. A base package on which Jupyter projects rely.
Group    : Development/Tools
License  : BSD-3-Clause-Clear
Requires: jupyter_core-bin
Requires: jupyter_core-python3
Requires: jupyter_core-python
Requires: traitlets
BuildRequires : pbr
BuildRequires : pip

BuildRequires : python3-dev
BuildRequires : setuptools
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

%description bin
bin components for the jupyter_core package.


%package python
Summary: python components for the jupyter_core package.
Group: Default
Requires: jupyter_core-python3

%description python
python components for the jupyter_core package.


%package python3
Summary: python3 components for the jupyter_core package.
Group: Default
Requires: python3-core

%description python3
python3 components for the jupyter_core package.


%prep
%setup -q -n jupyter_core-4.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1510236427
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jupyter
/usr/bin/jupyter-migrate

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
