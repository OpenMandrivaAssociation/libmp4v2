%define oname	mp4v2
%define major	2
%define libname	%mklibname mp4v2
%define devname	%mklibname -d mp4v2

%define _disable_lto 1

Summary:	Library for working with files using the mp4 container format
Name:		libmp4v2
Version:	2.1.3
Release:	1
License:	MPLv1.1
Group:		Sound
Url:		http://mp4v2.org/
Source0:	https://github.com/enzo1982/mp4v2/releases/download/v%{version}/mp4v2-%{version}.tar.bz2

%description
The libmp4v2 library provides an abstraction layer for working with files
using the mp4 container format. This library is developed by mpeg4ip project
and is an exact copy of the library distributed in the mpeg4ip package.

%package -n %{libname}
Group:		System/Libraries
Summary:	Library for working with files using the mp4 container format

%description -n %{libname}
This package contains the shared library for %{name}.

%package -n %{devname}
Summary:	Development files for the mp4v2 library
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Provides:	libmp4v2-devel = %{EVRD}

%description -n %{devname}
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
%autosetup -n %{oname}-%{version} -p1

%build
%configure \
	--disable-static \
	--disable-dependency-tracking
%make_build


%install
%make_install

%files utils
%doc COPYING
%{_bindir}/*
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/libmp4v2.so.%{major}*

%files -n %{devname}
%doc doc/*.txt
%{_includedir}/mp4v2/
%{_libdir}/*.so
%{_libdir}/pkgconfig/mp4v2.pc
