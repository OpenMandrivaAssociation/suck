%define name suck
%define version 4.3.2
%define release %mkrel 4

Summary: Suck - download news from remote NNTP server
Name: %{name}
Version: %{version}
Release: %{release}
Source: %{name}-%{version}.tar.bz2
URL: http://home.comcast.net/~bobyetman/index.html
BuildRoot: %{_tmppath}/%{name}-buildroot
License: Public Domain
Group: Networking/News

%description
This package contains software for copying news from an NNTP server to your
local machine, and copying replies back up to an NNTP server.  It works
with most standard NNTP servers, including INN, CNEWS, DNEWS, and typhoon.

%prep
%setup -q

export CFLAGS="$RPM_OPT_FLAGS -I/usr/include/db1"

%configure --bindir=$RPM_BUILD_ROOT%{_bindir} --mandir=$RPM_BUILD_ROOT%{_mandir}

%build
make

%install
make install

%clean
rm -rf $RPM_BUILD_ROOT 

%files
%defattr (-,root,root)
%doc README CHANGELOG
%{_bindir}/*
%{_mandir}/man1/*
