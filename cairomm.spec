Summary:	C++ wrapper for cairo
Summary(pl.UTF-8):	Interfejs C++ do cairo
Name:		cairomm
Version:	1.8.2
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://cairographics.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	24aa46a4f92bdb2af7cd80e6b335f07f
URL:		http://cairographics.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cairo-devel >= 1.8.0
BuildRequires:	doxygen
BuildRequires:	graphviz
BuildRequires:	libsigc++-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
Requires:	cairo >= 1.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ wrapper for cairo.

%description -l pl.UTF-8
Interfejs C++ do cairo.

%package devel
Summary:	Development files for cairomm library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki cairomm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cairo-devel >= 1.8.0
Requires:	libstdc++-devel

%description devel
Development files for cairomm library.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki cairomm.

%package static
Summary:	Static cairomm library
Summary(pl.UTF-8):	Statyczna biblioteka cairomm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static cairomm library.

%description static -l pl.UTF-8
Statyczna biblioteka cairomm.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_docdir}/libcairomm-1.0

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%attr(755,root,root) %{_libdir}/libcairomm-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcairomm-1.0.so.1

%files devel
%defattr(644,root,root,755)
%doc docs/reference/html/*
%attr(755,root,root) %{_libdir}/libcairomm-1.0.so
%{_libdir}/libcairomm-1.0.la
%{_includedir}/cairomm-1.0
%{_pkgconfigdir}/cairomm-1.0.pc
%{_pkgconfigdir}/cairomm-ft-1.0.pc
%{_pkgconfigdir}/cairomm-pdf-1.0.pc
%{_pkgconfigdir}/cairomm-png-1.0.pc
%{_pkgconfigdir}/cairomm-ps-1.0.pc
%{_pkgconfigdir}/cairomm-svg-1.0.pc
%{_pkgconfigdir}/cairomm-xlib-1.0.pc
%{_pkgconfigdir}/cairomm-xlib-xrender-1.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libcairomm-1.0.a
