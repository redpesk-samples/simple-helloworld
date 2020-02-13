%global debug_package %{nil}
Name:           testpackage-helloworld
Version:        1.0
Release:        1%{?dist}
Summary:        A hello world program

License:        Apache
URL:            http://git.ovh.iot/iotbzh/testpackage-helloworld
Source0:        testpackage-helloworld-1.0.tar.gz

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
