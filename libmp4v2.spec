%define oname	mp4v2
%define major	2
%define libname	%mklibname mp4v2_ %{major}
%define devname	%mklibname -d mp4v2

Summary:	Library for working with files using the mp4 container format
Name:		libmp4v2
Epoch:		1
Version:	2.0.0
Release:	3
License:	MPLv1.1
Group:		Sound
Url:		http://code.google.com/p/mp4v2/
Source0:	http://mp4v2.googlecode.com/files/%{oname}-%{version}.tar.bz2

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
%setup -qn %{oname}-%{version}

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
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/libmp4v2.so.%{major}*

%files -n %{devname}
%doc doc/*.txt
%{_includedir}/mp4v2/
%{_libdir}/*.so

