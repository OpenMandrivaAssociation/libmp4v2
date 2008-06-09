%define major 0
%define libname %mklibname mp4v2_ %major
%define develname %mklibname -d mp4v2
%define oldlibname %mklibname mpeg4ip 0
%define olddevelname %mklibname -d mpeg4ip
Summary: Library for working with files using the mp4 container format
Name: libmp4v2
Version: 1.5.0.1
Release: %mkrel 1
License: MPLv1.1
Group: Sound
URL: http://resare.com/libmp4v2/
Source0: http://resare.com/libmp4v2/dist/libmp4v2-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
The libmp4v2 library provides an abstraction layer for working with files
using the mp4 container format. This library is developed by mpeg4ip project
and is an exact copy of the library distributed in the mpeg4ip package.


%package -n %libname
Group: System/Libraries
Summary: Library for working with files using the mp4 container format
Conflicts: %oldlibname < 1.6.1-0.20070928.3

%description -n %libname
The libmp4v2 library provides an abstraction layer for working with files
using the mp4 container format. This library is developed by mpeg4ip project
and is an exact copy of the library distributed in the mpeg4ip package.

%package -n %develname
Summary: Development files for the mp4v2 library
Group: Development/C++
Requires: %{libname} = %{version}-%{release}
Provides: libmp4v2-devel = %{version}-%{release}
Conflicts: %olddevelname < 1.6.1-0.20070928.3

%description -n %develname
Development files and documentation needed to develop and compile programs
using the libmp4v2 library.

%package utils
Group: Sound
Summary: Command line utils to handle MP4 metadata
Conflicts: mpeg4ip < 1.6.1-0.20070928.3

%description utils
The libmp4v2 library provides an abstraction layer for working with files
using the mp4 container format. This library is developed by mpeg4ip project
and is an exact copy of the library distributed in the mpeg4ip package.

This contains the command line example utilities.

%prep
%setup -q

%build
%configure2_5x \
    --disable-static \
    --disable-dependency-tracking
%make


%install
rm -rf %{buildroot}
%makeinstall_std
rm -rf %{buildroot}%{_mandir}/manm/


%clean
rm -rf %{buildroot}


%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif


%files utils
%defattr(-,root,root,0755)
%doc COPYING
%{_bindir}/*

%files -n %libname
%defattr(-,root,root,0755)
%doc COPYING
%{_libdir}/libmp4v2.so.%{major}*

%files -n %develname
%defattr(-,root,root,0755)
%doc README TODO INTERNALS API_CHANGES
%{_includedir}/*.h
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_mandir}/man?/*


