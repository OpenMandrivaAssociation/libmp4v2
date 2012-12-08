%define major 2
%define libname %mklibname mp4v2_ %{major}
%define develname %mklibname -d mp4v2
%define olddevelname %mklibname -d mpeg4ip
%define oname mp4v2

Summary:	Library for working with files using the mp4 container format
Name:		libmp4v2
Version:	2.0.0
Release:	2
Epoch:		1
License:	MPLv1.1
Group:		Sound
URL:		http://code.google.com/p/mp4v2/
Source0:	http://mp4v2.googlecode.com/files/%{oname}-%{version}.tar.bz2

%description
The libmp4v2 library provides an abstraction layer for working with files
using the mp4 container format. This library is developed by mpeg4ip project
and is an exact copy of the library distributed in the mpeg4ip package.

%package -n %{libname}
Group:		System/Libraries
Summary:	Library for working with files using the mp4 container format

%description -n %{libname}
The libmp4v2 library provides an abstraction layer for working with files
using the mp4 container format. This library is developed by mpeg4ip project
and is an exact copy of the library distributed in the mpeg4ip package.

%package -n %{develname}
Summary:	Development files for the mp4v2 library
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Provides:	libmp4v2-devel = %{EVRD}

%description -n %{develname}
Development files and documentation needed to develop and compile programs
using the libmp4v2 library.

%package utils
Group:		Sound
Summary:	Command line utils to handle MP4 metadata

%description utils
The libmp4v2 library provides an abstraction layer for working with files
using the mp4 container format. This library is developed by mpeg4ip project
and is an exact copy of the library distributed in the mpeg4ip package.

This contains the command line example utilities.

%prep
%setup -q -n %{oname}-%{version}

%build
%configure2_5x \
    --disable-static \
    --disable-dependency-tracking
%make


%install
%makeinstall_std

%files utils
%doc COPYING
%{_bindir}/*

%files -n %{libname}
%doc COPYING
%{_libdir}/libmp4v2.so.%{major}*

%files -n %{develname}
%doc doc/*.txt
%{_includedir}/mp4v2/
%{_libdir}/*.so
%{_mandir}/man?/*


%changelog
* Wed Jun 06 2012 Götz Waschk <waschk@mandriva.org> 1:2.0.0-1mdv2012.0
+ Revision: 802872
- new version
- new major
- drop patch
- spec cleanup

* Thu May 03 2012 Götz Waschk <waschk@mandriva.org> 1:1.9.1-5
+ Revision: 795247
- yearly rebuild

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1:1.9.1-4
+ Revision: 661498
- mass rebuild

* Mon Nov 29 2010 Funda Wang <fwang@mandriva.org> 1:1.9.1-3mdv2011.0
+ Revision: 602823
- update file list

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1:1.9.1-2mdv2010.1
+ Revision: 520886
- rebuilt for 2010.1

* Wed Jul 15 2009 Götz Waschk <waschk@mandriva.org> 1:1.9.1-1mdv2010.0
+ Revision: 396216
- update to new version 1.9.1

* Wed May 27 2009 Götz Waschk <waschk@mandriva.org> 1:1.9.0-1mdv2010.0
+ Revision: 380197
- new version
- add epoch

* Mon May 18 2009 Götz Waschk <waschk@mandriva.org> 2.0-0.20090515.1mdv2010.0
+ Revision: 376833
- new snapshot

* Mon Jan 12 2009 Götz Waschk <waschk@mandriva.org> 2.0-0.20090110.1mdv2009.1
+ Revision: 328531
- switch to new fork
- update file list
- fix format strings

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 1.5.0.1-2mdv2009.0
+ Revision: 264840
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Apr 08 2008 Götz Waschk <waschk@mandriva.org> 1.5.0.1-1mdv2009.0
+ Revision: 192388
- import libmp4v2


* Mon Mar 31 2008 Götz Waschk <waschk@mandriva.org> 1.5.0.1-1mdv2008.1
- initial Mandriva package based on the Fedora spec

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.5.0.1-6
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 Matthias Saou <http://freshrpms.net/> 1.5.0.1-5
- Rebuild for new BuildID feature.

* Sun Aug  5 2007 Matthias Saou <http://freshrpms.net/> 1.5.0.1-4
- Update License field.

* Fri Dec 15 2006 Matthias Saou <http://freshrpms.net/> 1.5.0.1-3
- Spec file cleanup (habits, mostly) preparing to submit for Extras inclusion.

* Fri Oct 06 2006 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 1.5.0.1-2
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Jul 18 2006 Noa Resare <noa@resare.com> 1.5.0.1-1
- new upstream release

* Sat May 13 2006 Noa Resare <noa@resare.com> 1.4.1-3
- disabled static lib
- use DESTDIR
- disable-dependency-tracking for faster builds
- removed a manpage template file apt.mpt.gz

* Mon May 08 2006 Noa Resare <noa@resare.com> 1.4.1-2
- specfile cleanups

* Fri May 05 2006 Noa Resare <noa@resare.com> 1.4.1-1.lvn5
- initial release

