%global commit0 38ecbaf8ece45edd907994660ecd50f0db817b98
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

Name:           vid.stab
Version:        1.1.0
Release:        8%{?gver}%{?dist}
Summary:        Video stabilize library for fmpeg, mlt or transcode
License:        GPLv2+
URL:            http://public.hronopik.de/vid.stab
Source0:        https://github.com/georgmartius/vid.stab/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  orc-devel
Requires:       glibc
Obsoletes:	%{name}-libs 

%description
Vidstab is a video stabilization library which can be plugged-in with Ffmpeg
and Transcode.

%package devel
Summary:        Development files for vid.stab
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the development files (library and header files).

%prep
%autosetup -n %{name}-%{commit0}

%build
%cmake .
%make_build

# build the tests program
pushd tests
%cmake .
%make_build
popd

%install
%make_install

%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir} tests/tests || :

%post -n %{name} -p /sbin/ldconfig
%postun -n %{name} -p /sbin/ldconfig

%files
%doc README.md
%license LICENSE
%{_libdir}/libvidstab.so.*

%files devel
%{_includedir}/vid.stab/
%{_libdir}/libvidstab.so
%{_libdir}/pkgconfig/vidstab.pc

%changelog

* Sun Sep 23 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.1.0-8.git38ecbaf 
- Updated to current commit
- Compatibility changes

* Sat Oct 07 2017 David Vasquez <davidjeremias82 at gmail dot com> 1.1.0-2.gitafc8ea9
- Included old changes missed

* Sat Sep 30 2017 Sérgio Basto <sergio@serjux.com> - 1.1.0-1
- Update 1.1.0

* Mon Jul 6 2015 Fredrik Fornstad <fredrik.fornstad@gmail.com> 0.98a-20150706-97c6ae2-1
- New upstream release
- Introduced separate devel and libs rpms to enable future API updates without breaking dependencies

* Fri Apr 24 2015 David Vasquez <davidjeremias82 at gmail dot com> 0.98a-1-20150424git4ec5be1
- Updated to 0.98a-20150424-4ec5be1
- Included snapshot

* Mon Sep 1 2014 David Vasquez <davidjeremias82 at gmail dot com> 0.98b-1
- Initial build rpm
