
Summary:	Download news from remote NNTP server
Name:		suck
Version:	4.3.4
Release:	1
Source:		https://github.com/lazarus-pkgs/suck/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz
URL:		http://home.comcast.net/~bobyetman/index.html
BuildRoot:	%{_tmppath}/%{name}-buildroot
License:	Public Domain
Group:		Networking/News

%description
This package contains software for copying news from an NNTP server to your
local machine, and copying replies back up to an NNTP server.  It works
with most standard NNTP servers, including INN, CNEWS, DNEWS, and typhoon.

%prep
%setup -q

export CFLAGS="$RPM_OPT_FLAGS -I/usr/include/db1"

#configure --bindir=$RPM_BUILD_ROOT%{_bindir} --mandir=$RPM_BUILD_ROOT%{_mandir}

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


%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 4.3.2-10mdv2011.0
+ Revision: 615029
- the mass rebuild of 2010.1 packages

* Tue Feb 09 2010 Sandro Cazzaniga <kharec@mandriva.org> 4.3.2-9mdv2010.1
+ Revision: 502911
- clean, fix spec and build

* Tue Sep 08 2009 Thierry Vignaud <tv@mandriva.org> 4.3.2-8mdv2010.0
+ Revision: 434162
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 4.3.2-7mdv2009.0
+ Revision: 261212
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 4.3.2-6mdv2009.0
+ Revision: 253653
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 4.3.2-4mdv2008.1
+ Revision: 128041
- kill re-definition of %%buildroot on Pixel's request

  + Pascal Terjan <pterjan@mandriva.org>
    - Import suck



* Thu Apr 20 2006 Lenny Cartier <lenny@mandriva.com> 4.3.2-4mdk
- rebuild for dependencies

* Wed Jul 06 2005 Lenny Cartier <lenny@mandriva.com> 4.3.2-3mdk
- rebuild

* Sat May 01 2004 Marcel Pol <mpol@mandrake.org> 4.3.2-2mdk
- new url
- don't clean buildroot at %%prep
- quiet setup

* Mon Mar 31 2003 Lenny Cartier <lenny@mandrakesoft.com> 4.3.2-1mdk
- 4.3.2

* Mon Jan 27 2003 Lenny Cartier <lenny@mandrakesoft.com> 4.3.1-2mdk
- rebuild

* Wed Sep 25 2002 Lenny Cartier <lenny@mandrakesoft.com> 4.3.1-1mdk
- fix build
- 4.3.1

* Fri Nov 09 2001 Lenny Cartier <lenny@mandrakesoft.com> 4.3.0-1mdk
- 4.3.0

* Tue Aug 28 2001 Lenny Cartier <lenny@mandrakesoft.com> 4.2.5-1mdk
- 4.2.5

* Tue Jan 30 2001 Lenny Cartier <lenny@mandrakesoft.com> 4.2.4-2mdk
- rebuild

* Mon Sep 18 2000 Lenny Cartier <lenny@mandrakesoft.com> 4.2.4-1mdk
- updated to 4.2.4
- BM
- macros
