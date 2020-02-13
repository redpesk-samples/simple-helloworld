%global debug_package %{nil}

Name:           simple-helloworld
Version:        1.0
Release:        1%{?dist}
Summary:        A hello world program

License:        Apache
URL:            http://git.ovh.iot/redpesk/simple-helloworld
Source0:        simple-helloworld-1.0.tar.gz

BuildRequires: gcc

%description
A helloworld program

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
