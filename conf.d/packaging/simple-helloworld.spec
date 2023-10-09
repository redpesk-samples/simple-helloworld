%global debug_package %{nil}

Name:           simple-helloworld
Version:        1.0
Release:        1%{?dist}
Summary:        Simple hello world program

License:        Apache
URL:            https://github.com/redpesk-samples/simple-helloworld
Source:         %{name}-%{version}.tar.gz

BuildRequires: gcc

%description
The most simple hello program of the world !

%package redtest
Summary:        Redtest subpackage of simple helloworld package
Requires:       %{name} = %{version}

%description redtest
The tests for the most simple hello program of the world !

%prep
%setup

%build
%make_build

%install
%make_install

%clean
rm -rf %{buildroot}

%files
%{_bindir}/helloworld

%files redtest
%{_libexecdir}/redtest/%{name}/*
