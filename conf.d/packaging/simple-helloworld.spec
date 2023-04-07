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
